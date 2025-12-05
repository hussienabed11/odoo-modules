from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = "courses.course"
    _description = "Course"

    name = fields.Char(required=True)
    description = fields.Text()
    duration = fields.Char()
    active = fields.Boolean(default=True)
    instructor_id = fields.Many2many('courses.instructor', string='Instructor')
    student_ids = fields.Many2many('courses.student', string='Students')

    # ===== new fields =====
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], string='Level', default='beginner')

    published = fields.Boolean(string='Published', default=False)
    # ======================

    # ===== price / discount / final_price /profit =====
    # pricing fields
    price = fields.Float(string="Price", digits=(16, 2), default=0.0)
    discount = fields.Float(string="Discount", digits=(16, 2), default=0.0)

    tax =fields.Float(string="Tax (14%)",compute="_compute_tax",store=True)
    final_price = fields.Float(string="Final Price",compute="_compute_final_price",inverse="_inverse_final_price",store=True,digits=(16,2))

    #profit
    profit = fields.Float(string="Profit",compute="_compute_profit",store=True)
    profit_preview = fields.Float(string='Profit Preview', compute='_compute_profit_preview', store=False, digits=(16,2))

    # limits & flags
    max_students = fields.Integer(string='Max Students', default=50)


    #Methods
    def action_publish(self):
        """Set the course as published."""
        for rec in self:
            rec.published = True
        return True
    
    #final_price
    @api.depends('price', 'discount')
    def _compute_final_price(self):
        for rec in self:
            rec.final_price = max((rec.price or 0.0) - (rec.discount or 0.0), 0.0)

    def _inverse_final_price(self):
        for rec in self:
            fp = rec.final_price or 0.0
            if fp < 0.0:
                fp = 0.0
                rec.final_price = 0.0
            rec.discount = (rec.price or 0.0) - fp
            if rec.discount < 0.0:
                rec.discount = 0.0
                rec.final_price = rec.price or 0.0

       
    
    @api.onchange('price', 'discount')
    def _onchange_price_discount(self):
        for rec in self:
            if rec.price is not None and rec.price < 0:
                rec.price = 0.0
                return {
                    'warning': {
                        'title': "Invalid price",
                        'message': "Price cannot be negative. It was reset to 0."
                    }
                }
            if rec.discount is not None and rec.discount < 0:
                rec.discount = 0.0
                return {
                    'warning': {
                        'title': "Invalid discount",
                        'message': "Discount cannot be negative. It was reset to 0."
                    }
                }

            if (rec.discount or 0.0) > (rec.price or 0.0):
                rec.discount = rec.price or 0.0
                return {
                    'warning': {
                        'title': "Discount capped",
                        'message': "Discount cannot exceed Price — it was set to the Price value."
                    }
                }

    
    #Tax
    @api.depends('price')
    def _compute_tax(self):
        for rec in self:
            rec.tax=(rec.price or 0.0) * 0.14

    #profit
    @api.depends('final_price', 'tax')
    def _compute_profit(self):
        for rec in self:
            rec.profit = (rec.final_price or 0.0) + (rec.tax or 0.0)


    #_compute_profit_preview
    @api.depends('price','discount')
    def _compute_profit_preview(self):
        for rec in self:
            price = rec.price or 0.0
            discount = rec.discount or 0.0
            tax = price * 0.14
            rec.profit_preview = max(price - discount, 0.0) + tax

    #level
    @api.onchange('level')
    def _onchange_level(self):
        for rec in self:
            if rec.level == 'beginner':
                rec.discount = 10.0
            elif rec.level == 'advanced':
                rec.price = 2000.0

    @api.onchange('student_ids')
    def _onchange_student_ids(self):
        for rec in self:
            if rec.max_students and len(rec.student_ids) > rec.max_students:
                return {
                    'warning': {
                        'title': "Max students exceeded",
                        'message': f"Number of students exceeds the maximum ({rec.max_students})."
                    }
                }
            
    @api.constrains('price', 'discount')
    def _check_price_discount(self):
        for rec in self:
            if rec.price is None:
                continue
            if rec.price < 0:
                raise ValidationError("Price cannot be negative.")
            if rec.discount is None:
                continue
            if rec.discount < 0:
                raise ValidationError("Discount cannot be negative.")
            if rec.discount > rec.price:
                raise ValidationError("Discount cannot exceed Price.")
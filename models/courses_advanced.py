from odoo import models, fields

class AdvancedCourse(models.Model):
    _name = "courses.advanced"
    _inherit = "courses.course"    # classical inheritance
    _description = "Advanced Course"

    level = fields.Selection([
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], string="Level")

    certificate = fields.Boolean(string="Certificate Included", default=True)

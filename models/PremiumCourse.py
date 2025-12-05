from odoo import models,fields

class PremiumCourse (models.Model):
    _name = "courses.premium_course"
    _inherit ="courses.course" #calssical inheritance
    _description = "PremiumCourse"

    #New fields
    premium_level = fields.Selection([
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ], string="Premium Level")

    extra_material = fields.Boolean(string="Extra Material", default=False)
    bonus_certificate = fields.Boolean(string="Bonus Certificate", default=True)
    
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    # ربط Many2many إلى courses.course عبر جدول وسيط users_courses_rel
    property_ids = fields.Many2many(
        'courses.course',
        'users_courses_rel',     # اسم جدول العلاقة في DB
        'user_id',               # الحقل الذي يشير إلى res.users
        'course_id',             # الحقل الذي يشير إلى courses.course
        string='Properties / Courses'
    )

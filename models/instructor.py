from odoo import models,fields

class Instructor(models.Model):
    _name ="courses.instructor"
    _description = "Instructor"    
    
    name = fields.Char(required=True)
    email = fields.Char()
    bio = fields.Text()
    courses_id=fields.Many2many('courses.course' , 'instructor_id' , string='Courses Taught')
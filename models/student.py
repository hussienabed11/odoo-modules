from odoo import models, fields

class Student(models.Model):
    _name = "courses.student"
    _description = "Student"

    name = fields.Char(required=True)
    email = fields.Char()
    country = fields.Char()
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], string="Level")  #New field
    age = fields.Integer()
    course_ids = fields.Many2many('courses.course', string="Courses")

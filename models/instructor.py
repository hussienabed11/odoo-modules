from odoo import models, fields, api

class Instructor(models.Model):
    _name = "courses.instructor"
    _description = "Instructor"

    # -------------------- Fields --------------------
    name = fields.Char(required=True)
    email = fields.Char()
    bio = fields.Text()
    courses_id = fields.Many2many('courses.course', string='Courses Taught')

    # -------------------- Create Method --------------------
    @api.model
    def create_demo_instructors(self):
        """
        Create demo instructors for testing.
        """
        instructor1 = self.create({
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'bio': 'Expert in Python and AI',
        })

        instructor2 = self.create({
            'name': 'Bob Smith',
            'email': 'bob@example.com',
            'bio': 'JavaScript and Frontend Specialist',
        })

        return instructor1, instructor2

    # -------------------- Search + Write Method --------------------
    @api.model
    def update_instructor_email(self, instructor_name, new_email):
        """
        Search for an instructor by name and update their email.
        """
        instructor = self.search([('name', '=', instructor_name)], limit=1)
        if instructor:
            instructor.write({'email': new_email})
        return instructor

    # -------------------- Unlink Method --------------------
    @api.model
    def delete_instructor(self, instructor_name):
        """
        Search for an instructor by name and delete the record.
        """
        instructor = self.search([('name', '=', instructor_name)], limit=1)
        if instructor:
            instructor.unlink()
        return True

    # -------------------- Browse Example --------------------
    @api.model
    def browse_instructor_courses(self, instructor_id):
        """
        Browse an instructor record by ID and return all linked courses.
        """
        instructor = self.browse(instructor_id)
        return instructor.courses_id

    # -------------------- Name_get Example --------------------
    @api.model
    def get_instructor_display_name(self):
        """
        Override name_get to customize how instructor names appear in dropdowns.
        """
        result = []
        for rec in self.search([]):
            result.append((rec.id, f"{rec.name} ({rec.email})"))
        return result

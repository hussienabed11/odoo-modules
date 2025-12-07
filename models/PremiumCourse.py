from odoo import models, fields, api

class PremiumCourse(models.Model):
    _name = "courses.premium_course"
    _inherit = "courses.course"
    _description = "PremiumCourse"

    # -------------------- Fields --------------------
    premium_level = fields.Selection([
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ], string="Premium Level")
    extra_material = fields.Boolean(default=False)
    bonus_certificate = fields.Boolean(default=True)
    students_ids = fields.Many2many('courses.student', string="Students")

    # -------------------- Create Methods --------------------
    @api.model
    def create_demo_courses(self):
        """
        Create demo courses for testing purposes.
        Returns the names of the created courses.
        """
        gold_course = self.create({
            'name': 'Advanced Python',
            'description': 'Deep dive into Python',
            'duration': '3 months',
            'premium_level': 'gold',
            'extra_material': True,
            'bonus_certificate': True
        })

        silver_course = self.create({
            'name': 'Intermediate JavaScript',
            'description': 'JS intermediate concepts',
            'duration': '2 months',
            'premium_level': 'silver',
            'extra_material': False,
            'bonus_certificate': True
        })

        bronze_course = self.create({
            'name': 'Beginner HTML & CSS',
            'description': 'Learn the basics of web development',
            'duration': '1 month',
            'premium_level': 'bronze',
            'extra_material': False,
            'bonus_certificate': False
        })

        return gold_course.name, silver_course.name, bronze_course.name

    @api.model
    def create_course_with_students(self):
        """
        Create a course along with multiple student records.
        Links the students to the course using Many2many relation.
        Returns the created course and students.
        """
        # Define student data
        students_data = [
            {'name': "John Cena"},
            {'name': "Sara Mohamed"},
            {'name': "Ahmed Ali"},
        ]

        # Create student records
        students = self.env['courses.student'].create(students_data)

        # Create a new course
        course = self.create({
            'name': "AI Bootcamp",
            'description': "Intro to AI",
            'duration': "1 month",
        })

        # Link students to the course
        course.students_ids = [(6, 0, students.ids)]  # 6 = replace all existing records

        return course, students

    # -------------------- Write Method --------------------
    @api.model
    def update_ai_bootcamp_course(self):
        """
        Update an existing course's fields.
        If the course does not exist, create it first.
        Returns the updated course record.
        """
        # Search for the course
        course = self.search([('name', '=', 'AI Bootcamp')], limit=1)

        # Create course if not found
        if not course:
            course = self.create({
                'name': "AI Bootcamp",
                'description': "Intro to AI",
                'duration': "1 month",
            })

        # Update course fields
        course.write({
            'description': 'Advanced AI concepts',
            'duration': '2 months',
            'extra_material': True,
        })

        return course

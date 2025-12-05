{
    'name': 'Courses manager',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/advanced_course_views.xml',
        'views/courses_views.xml',
        'views/instructor_views.xml',
        'views/student_views.xml',
        'views/PremiumCourse_views.xml',
        'views/users_inherit_views.xml',
        'views/course_views_inherit.xml',
        'views/student_views_inherit.xml',
    ],
    'installable': True,
    'application': True,
}

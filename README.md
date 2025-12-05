#Courses_manager Module (Odoo 17)

## Overview
This custom Odoo module manages courses, instructors, students, and enrollment.  
It implements complete business logic including pricing, discounts, taxes, profits, and level-based rules.  
The module demonstrates advanced Odoo ORM usage, inheritance, computed fields, constraints, and custom views.

---

## Features

### Courses
- Name, Description, Duration, Level, Active Status
- Price, Discount, Final Price (computed with inverse), Tax (computed)
- Profit & Profit Preview (computed)
- Max students limit
- Published/unpublished flag
- Validation and warnings for price, discount, and student limits

### Instructors
- Name, Email, Bio
- One2many relation to courses
- Custom views (tree & form)

### Students
- Many2many relation with courses
- Applied onchange for max_students

### Pricing & Profit Logic
- Computed `final_price` with inverse method
- Tax computation (14%)
- Profit & Profit Preview computation
- Level-based pricing & discount logic
- Onchange warnings for invalid price/discount
- Constrains to prevent negative prices or discount exceeding price

### Views
- Form & Tree views for courses, instructors, and students
- Custom fields display
- Many2many widget for students
- Menus and actions for easy navigation

### Wizards
- Placeholder for future wizards (according to module structure)

### Security
- `ir.model.access.csv` for access control

---

## Technical Stack
- **Python**: Odoo ORM, computed fields, inverse, onchange, constraints
- **XML**: Form & Tree views, menus, actions
- **Odoo**: Model relations, security, menus, actions

---

## File Structure
courses_v2/
├── models/
│ ├── courses.py
│ ├── instructor.py
│ ├── student.py
│ ├── PremiumCourse.py
│ └── res_users.py
├── views/
│ ├── courses_views.xml
│ ├── instructor_views.xml
│ ├── student_views.xml
│ └── users_inherit_views.xml
├── security/
│ └── ir.model.access.csv
├── reports/
├── wizard/
├── init.py
└── manifest.py


---

## Usage
1. Install the module in Odoo 17.
2. Go to **Courses V2 → Courses** to manage courses.
3. Add instructors and students.
4. Pricing, discount, tax, and profit are computed automatically.
5. Onchange methods provide warnings for invalid data.

---

## Notes
- This module demonstrates the application of advanced Odoo development concepts.
- Suitable as a learning and portfolio project for showcasing ORM, Views, Wizards, Security, and business logic implementation.


# -*- coding: utf-8 -*-
{
    'name': 'PM & HR Suite - Employee Management',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Mo rong ho so nhan vien, hop dong, nghi phep va cham cong',
    'author': 'Antigravity AI',
    'depends': ['hr', 'hr_contract', 'hr_holidays', 'hr_attendance', 'pm_hr_base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_security.xml',
        'views/hr_employee_views.xml',
        'views/hr_leave_views.xml',
        'views/hr_attendance_views.xml',
        'views/hr_menus.xml',
    ],
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}

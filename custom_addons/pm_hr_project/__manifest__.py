# -*- coding: utf-8 -*-
{
    'name': 'PM & HR Suite - Project Management',
    'version': '17.0.1.0.0',
    'category': 'Services/Project',
    'summary': 'Mo rong quan ly du an: ngan sach, rui ro, milestone, visual dashboard',
    'author': 'Antigravity AI',
    'depends': ['project', 'hr_timesheet', 'pm_hr_base'],
    'data': [
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'data/project_stage_data.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/project_menus.xml',
    ],
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}

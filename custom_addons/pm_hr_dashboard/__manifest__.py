# -*- coding: utf-8 -*-
{
    'name': 'PM & HR Suite - Executive Dashboard',
    'version': '17.0.1.0.0',
    'category': 'Management',
    'summary': 'Dashboard dieu hanh tong hop PM & HR kieu dang hien dai',
    'author': 'Antigravity AI',
    'depends': ['pm_hr_project', 'pm_hr_employee'],
    'data': [
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pm_hr_dashboard/static/src/css/dashboard_style.css',
            'pm_hr_dashboard/static/src/js/dashboard_action.js',
            'pm_hr_dashboard/static/src/xml/dashboard_template.xml',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}

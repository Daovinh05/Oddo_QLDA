# -*- coding: utf-8 -*-
{
    'name': 'PM & HR Suite - Base',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Nen tang dinh nghia nhom quyen va danh muc chung cho PM & HR Suite',
    'author': 'Antigravity AI',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/pm_hr_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/pm_hr_menus.xml',
    ],
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
from odoo import models, fields

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    code = fields.Char(string='Ma phong ban', copy=False)
    description = fields.Text(string='Mo ta chuc nang')

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    interview_notes = fields.Text(string='Ghi chu phong van')
    rating_stars = fields.Selection([
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string='Danh gia ung vien', default='3')

    def action_create_employee(self):
        res = super(HrApplicant, self).create_employee_from_applicant()
        return res

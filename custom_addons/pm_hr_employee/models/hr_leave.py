# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    approval_stage = fields.Selection([
        ('draft', 'Nhap'),
        ('confirm', 'Cho Quan ly duyet'),
        ('refuse', 'Tu choi'),
        ('validate1', 'Cho HR duyet'),
        ('validate', 'Da duyet')
    ], string='Cap duyet', compute='_compute_approval_stage', store=True)

    @api.depends('state')
    def _compute_approval_stage(self):
        for leave in self:
            if leave.state == 'draft':
                leave.approval_stage = 'draft'
            elif leave.state == 'confirm':
                leave.approval_stage = 'confirm'
            elif leave.state == 'validate1':
                leave.approval_stage = 'validate1'
            elif leave.state == 'validate':
                leave.approval_stage = 'validate'
            elif leave.state == 'refuse':
                leave.approval_stage = 'refuse'
            else:
                leave.approval_stage = 'draft'

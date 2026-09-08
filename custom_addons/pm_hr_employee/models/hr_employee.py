# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_code = fields.Char(
        string='Ma nhan vien', 
        copy=False, 
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('hr.employee.code')
    )
    date_join = fields.Date(string='Ngay vao lam', default=fields.Date.today)
    employee_status = fields.Selection([
        ('probation', 'Thu viec'),
        ('official', 'Chinh thuc'),
        ('resigned', 'Da nghi viec')
    ], string='Trang thai nhan su', default='official')
    
    leave_balance = fields.Float(string='So ngay phep con lai', compute='_compute_leave_balance')
    project_ids = fields.Many2many('project.project', string='Du an dang tham gia', compute='_compute_project_ids')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('employee_code'):
                vals['employee_code'] = self.env['ir.sequence'].next_by_code('hr.employee.code') or '/'
        return super(HrEmployee, self).create(vals_list)

    def _compute_leave_balance(self):
        for emp in self:
            leaves = self.env['hr.leave'].search([
                ('employee_id', '=', emp.id),
                ('state', '=', 'validate')
            ])
            taken_days = sum(leaves.mapped('number_of_days'))
            emp.leave_balance = max(12.0 - taken_days, 0.0)

    def _compute_project_ids(self):
        for emp in self:
            if emp.user_id:
                projects = self.env['project.project'].search([
                    '|', ('user_id', '=', emp.user_id.id), ('member_ids', 'in', [emp.user_id.id])
                ])
                emp.project_ids = projects
            else:
                emp.project_ids = self.env['project.project']

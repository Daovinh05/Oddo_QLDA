# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    code = fields.Char(
        string='Ma du an', 
        copy=False, 
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('project.project.code')
    )
    department_id = fields.Many2one('hr.department', string='Phong ban chu tri')
    budget_planned = fields.Monetary(string='Ngan sach ke hoach', currency_field='currency_id')
    budget_actual = fields.Monetary(
        string='Ngan sach thuc te', 
        currency_field='currency_id', 
        compute='_compute_budget_actual', 
        store=True
    )
    priority = fields.Selection([
        ('low', 'Thap'),
        ('normal', 'Binh thuong'),
        ('high', 'Cao'),
        ('urgent', 'Khan cap')
    ], string='Muc do uu tien', default='normal')

    risk_level = fields.Selection([
        ('low', 'Thap'),
        ('medium', 'Trung binh'),
        ('high', 'Cao')
    ], string='Muc do rui ro', default='low')

    health_status = fields.Selection([
        ('on_track', 'Dung tien do'),
        ('at_risk', 'Co rui ro'),
        ('delayed', 'Cham tien do')
    ], string='Suc khoe du an', compute='_compute_health_status', store=True, default='on_track')

    progress = fields.Float(string='Tien do (%)', compute='_compute_progress', store=True)
    milestone_ids = fields.One2many('project.milestone', 'project_id', string='Moc du an')
    member_ids = fields.Many2many('res.users', string='Thanh vien du an')
    currency_id = fields.Many2one('res.currency', string='Tien te', default=lambda self: self.env.company.currency_id)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('code'):
                vals['code'] = self.env['ir.sequence'].next_by_code('project.project.code') or '/'
        return super(ProjectProject, self).create(vals_list)

    @api.depends('task_ids.stage_id', 'task_ids.date_deadline')
    def _compute_health_status(self):
        today = fields.Date.today()
        for project in self:
            tasks = project.task_ids
            if not tasks:
                project.health_status = 'on_track'
                continue
            
            overdue_count = 0
            for t in tasks:
                if t.date_deadline and t.stage_id and not t.stage_id.fold:
                    t_date = fields.Date.to_date(t.date_deadline)
                    if t_date < today:
                        overdue_count += 1

            ratio = overdue_count / len(tasks)
            if ratio > 0.3:
                project.health_status = 'delayed'
            elif ratio > 0.1:
                project.health_status = 'at_risk'
            else:
                project.health_status = 'on_track'

    @api.depends('task_ids.stage_id')
    def _compute_progress(self):
        for project in self:
            total_tasks = len(project.task_ids)
            if not total_tasks:
                project.progress = 0.0
                continue
            done_tasks = len(project.task_ids.filtered(lambda t: t.stage_id and (t.stage_id.fold or t.stage_id.name == 'Done')))
            project.progress = (done_tasks / total_tasks) * 100.0

    @api.depends('task_ids.timesheet_ids.unit_amount')
    def _compute_budget_actual(self):
        for project in self:
            total_hours = sum(project.task_ids.mapped('timesheet_ids.unit_amount'))
            project.budget_actual = total_hours * 50.0

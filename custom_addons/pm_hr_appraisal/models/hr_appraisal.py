# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PmHrAppraisal(models.Model):
    _name = 'pm.hr.appraisal'
    _description = 'Đánh giá hiệu suất nhân viên'
    _order = 'id desc'

    name = fields.Char(string='Mã / Tiêu đề', required=True, default='Đánh giá hiệu suất')
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    manager_id = fields.Many2one('hr.employee', string='Quản lý đánh giá', related='employee_id.parent_id', store=True)
    department_id = fields.Many2one('hr.department', string='Phòng ban', related='employee_id.department_id', store=True)
    period = fields.Char(string='Kỳ đánh giá (Ví dụ: Q3/2026)', required=True)
    date_close = fields.Date(string='Hạn đánh giá')

    state = fields.Selection([
        ('draft', 'Lên lịch'),
        ('self_eval', 'Tự đánh giá'),
        ('manager_eval', 'Quản lý đánh giá'),
        ('done', 'Hoàn tất')
    ], string='Trạng thái', default='draft')

    score_project = fields.Float(string='Điểm hoàn thành công việc (1-5)', default=3.0)
    score_competency = fields.Float(string='Điểm năng lực (1-5)', default=3.0)
    score_final = fields.Float(string='Điểm tổng kết', compute='_compute_score_final', store=True)

    self_comments = fields.Text(string='Ý kiến tự đánh giá')
    manager_comments = fields.Text(string='Nhận xét của quản lý')

    @api.depends('score_project', 'score_competency')
    def _compute_score_final(self):
        for record in self:
            record.score_final = round((record.score_project + record.score_competency) / 2.0, 2)

    def action_self_eval(self):
        self.write({'state': 'self_eval'})

    def action_manager_eval(self):
        self.write({'state': 'manager_eval'})

    def action_done(self):
        self.write({'state': 'done'})

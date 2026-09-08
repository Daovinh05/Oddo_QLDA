# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectMilestone(models.Model):
    _name = 'project.milestone'
    _description = 'Moc du an'
    _order = 'deadline ascii, id desc'

    name = fields.Char(string='Ten moc', required=True)
    project_id = fields.Many2one('project.project', string='Du an', required=True, ondelete='cascade')
    deadline = fields.Date(string='Han hoan thanh')
    is_reached = fields.Boolean(string='Da dat duoc', default=False)
    task_ids = fields.One2many('project.task', 'milestone_id', string='Cong viec liên quan')

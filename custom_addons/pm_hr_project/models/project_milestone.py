# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'
    _order = 'deadline asc, id desc'

    task_ids = fields.One2many('project.task', 'milestone_id', string='Cong viec liên quan')


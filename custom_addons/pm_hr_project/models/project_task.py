# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit = 'project.task'

    milestone_id = fields.Many2one('project.milestone', string='Moc du an', domain="[('project_id', '=', project_id)]")
    progress = fields.Float(string='Tien do (%)', default=0.0)
    depend_on_ids = fields.Many2many(
        'project.task',
        'project_task_dependency_rel',
        'task_id',
        'depend_id',
        string='Task phu thuoc (Blocking)'
    )

    @api.constrains('stage_id')
    def _check_dependencies_on_stage_change(self):
        for task in self:
            if task.stage_id and (task.stage_id.fold or task.stage_id.name == 'Done'):
                unfinished_deps = task.depend_on_ids.filtered(lambda t: not t.stage_id.fold and t.stage_id.name != 'Done')
                if unfinished_deps:
                    dep_names = ", ".join(unfinished_deps.mapped('name'))
                    raise ValidationError(_("Khong the chuyen task '%s' sang Done vi cac task phu thuoc chua hoan thanh: %s") % (task.name, dep_names))

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    punctuality_status = fields.Selection([
        ('on_time', 'Dung gio'),
        ('late', 'Di tre (>15p)'),
        ('early_leave', 'Ve som')
    ], string='Trang thai chuyen can', compute='_compute_punctuality_status', store=True)

    @api.depends('check_in', 'check_out')
    def _compute_punctuality_status(self):
        for att in self:
            if not att.check_in:
                att.punctuality_status = 'on_time'
                continue
            # Check-in time comparison: standard start time 08:30
            check_in_dt = fields.Datetime.context_timestamp(att, att.check_in)
            if check_in_dt.hour > 8 or (check_in_dt.hour == 8 and check_in_dt.minute > 45):
                att.punctuality_status = 'late'
            else:
                att.punctuality_status = 'on_time'

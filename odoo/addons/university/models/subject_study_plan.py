from odoo import models, fields, api

class SubjectStudyPlan(models.Model):
    _name = 'university.subject_study_plan'
    _description = 'Subject Study Plan'
    _rec_name = 'display_name'

    subject_id = fields.Many2one('university.subject', string='Subject')
    grade_id = fields.Many2one('university.grade', string='Grade')
    study_plan_id = fields.Many2one('university.study_plan', string='Study Plan')
    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('subject_id', 'grade_id', 'study_plan_id')
    def _compute_display_name(self):
        for rec in self:
            parts = []
            if rec.subject_id:
                parts.append(rec.subject_id.name)
            if rec.grade_id:
                parts.append(rec.grade_id.name)
            if rec.study_plan_id:
                parts.append(rec.study_plan_id.name)
            rec.display_name = ' - '.join(parts) if parts else ''
from odoo import models, fields

class SubjectStudyPlan(models.Model):
    _name = 'university.subject_study_plan'
    _description = 'Subject Study Plan'
    _rec_name = 'subject_id'

    subject_id = fields.Many2one('university.subject', string='Subject')
    grade_id = fields.Many2one('university.grade', string='Grade')
    study_plan_id = fields.Many2one('university.study_plan', string='Study Plan')

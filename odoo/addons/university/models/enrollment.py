from odoo import models, fields

class Enrollment(models.Model):
    _name = 'university.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('university.student', string='Student')
    study_plan_id = fields.Many2one('university.study_plan', string='Study Plan')
    career_id = fields.Many2one('university.career', string='Career')
    enrollment_date = fields.Date(string='Enrollment Date')
    subject_study_plan_ids = fields.Many2many('university.subject_study_plan', string='Subjects')
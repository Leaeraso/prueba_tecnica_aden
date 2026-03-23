from odoo import models, fields

class Enrollment(models.Model):
    _name = 'university.enrollment'
    _description = 'Enrollment'
    _rec_name = 'student_id'

    student_id = fields.Many2one('university.student', string='Student')
    study_plan_id = fields.Many2one('university.study_plan', string='Study Plan')
    career_id = fields.Many2one('university.career', string='Career')
    enrollment_date = fields.Date(string='Enrollment Date')
    enrollment_subject_classroom_ids = fields.One2many('university.enrollment_subject_classroom', 'enrollment_id', string='Subjects')
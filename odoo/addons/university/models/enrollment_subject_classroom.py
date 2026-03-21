from odoo import models, fields

class EnrollmentSubjectClassroom(models.Model):
    _name = 'university.enrollment_subject_classroom'
    _description = 'Enrollment Subject Classroom'

    enrollment_id = fields.Many2one('university.enrollment', string='Enrollment')
    subject_study_plan_id = fields.Many2one('university.subject_study_plan', string='Subject')
    classroom_id = fields.Many2one('university.classroom', string='Classroom')
    subject_id = fields.Many2one('university.subject', related='subject_study_plan_id.subject_id', string='Subject', readonly=True)
    grade_id = fields.Many2one('university.grade', related='subject_study_plan_id.grade_id', string='Grade', readonly=True)
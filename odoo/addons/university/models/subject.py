from odoo import models, fields, api

class Subject(models.Model):
    _name = 'university.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    professor_ids = fields.Many2many('university.professor', string='Professors')
    enrollment_count = fields.Integer(string='Enrollments', compute='_compute_enrollment_count')

    @api.depends()
    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = self.env['university.enrollment'].search_count([
                ('subject_study_plan_ids.subject_id', '=', record.id)
            ])
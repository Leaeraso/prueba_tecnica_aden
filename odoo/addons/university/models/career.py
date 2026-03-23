from odoo import models, fields, api

class Career(models.Model):
    _name = 'university.career'
    _description = 'Career'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    grade_ids = fields.Many2many('university.grade', string='Grades')
    enrollment_count = fields.Integer(string='Enrollments', compute='_compute_enrollment_count')

    @api.depends()
    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = self.env['university.enrollment'].search_count([('career_id', '=', record.id)])
from odoo import models, fields, api

class Student(models.Model):
    _name = 'university.student'
    _description = 'Student'

    student_number = fields.Char(string='Student Number', readonly=True, default='New')
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    dni = fields.Integer(string='DNI')
    date_of_birth = fields.Date(string='Date of Birth')
    student_status_id = fields.Many2one('university.student_status', string='Status')
    enrollment_ids = fields.One2many('university.enrollment', 'student_id', string='Enrollments')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('student_number', 'New') == 'New':
                vals['student_number'] = self.env['ir.sequence'].next_by_code('university.student')
        return super().create(vals_list)
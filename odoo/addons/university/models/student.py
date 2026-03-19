from odoo import models, fields

class Student(models.Model):
    _name = 'university.student'
    _description = 'Student'

    student_number = fields.Integer(string='Student Number')
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    dni = fields.Integer(string='DNI')
    date_of_birth = fields.Date(string='Date of Birth')
    student_status_id = fields.Many2one('university.student_status', string='Status')
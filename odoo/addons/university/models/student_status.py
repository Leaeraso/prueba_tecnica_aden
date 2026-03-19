from odoo import models, fields

class StudentStatus(models.Model):
    _name = 'university.student_status'
    _description = 'Student Status'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
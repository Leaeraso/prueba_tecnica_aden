from odoo import models, fields

class Professor(models.Model):
    _name = 'university.professor'
    _description = 'Professor'

    professor_number = fields.Integer(string='Professor Number')
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    cuit = fields.Integer(string='Cuit')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    subject_ids = fields.Many2many('university.subject', string='Subjects')
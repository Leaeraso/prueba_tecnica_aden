from odoo import models, fields

class Subject(models.Model):
    _name = 'university.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    professor_ids = fields.Many2many('university.professor', string='Professors')
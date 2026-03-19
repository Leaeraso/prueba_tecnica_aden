from odoo import models, fields

class Career(models.Model):
    _name = 'university.career'
    _description = 'Career'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    grade_ids = fields.Many2many('university.grade', string='Grades')
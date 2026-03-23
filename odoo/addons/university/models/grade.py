from odoo import models, fields

class Grade(models.Model):
    _name = 'university.grade'
    _description = 'Grade'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
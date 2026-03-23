from odoo import models, fields, api

class Professor(models.Model):
    _name = 'university.professor'
    _description = 'Professor'

    professor_number = fields.Char(string='Professor Number', readonly=True, default='New')
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    cuit = fields.Integer(string='Cuit')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    subject_ids = fields.Many2many('university.subject', string='Subjects')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('professor_number', 'New') == 'New':
                vals['professor_number'] = self.env['ir.sequence'].next_by_code('university.professor')
        return super().create(vals_list)
    
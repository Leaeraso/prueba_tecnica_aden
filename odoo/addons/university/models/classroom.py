from odoo import models, fields, api

class Classroom(models.Model):
    _name = 'university.classroom'
    _description = 'Classroom'
    _rec_name = 'classroom_number'
    
    classroom_number = fields.Char(string='Classroom Number', readonly=True, default='New')
    capacity = fields.Integer(string='Capacity', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('classroom_number', 'New') == 'New':
                vals['classroom_number'] = self.env['ir.sequence'].next_by_code('university.classroom')
        return super().create(vals_list)
    


from odoo import models, fields

class StudyPlan(models.Model):
    _name = 'university.study_plan'
    _description = 'Study Plan'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    career_id = fields.Many2one('university.career', string='Career')
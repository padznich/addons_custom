# -*- coding: utf-8 -*-
##############################################################################
#Add Project Section by Project Tasks
##############################################################################
from openerp import models, fields, api

class SectionByTask(models.Model):
    _inherit = 'project.task'

    section_id = fields.Many2one('project.section', string='Раздел')
    w_rate = fields.Float(related='section_id.wage_rate', string='Ставка')
    lab = fields.Float(related='section_id.labor', string='План. трудоемкость')
    pl_cost = fields.Float(related='section_id.planned_cost', string='План. стоимость')
    #Фактическая стоимость (Computed fields)
    fact_cost = fields.Float(string="Факт. стоимость", compute='_taken_cost')

    @api.depends('effective_hours', 'w_rate')
    def _taken_cost(self):
        for record in self:
            record.fact_cost = record.w_rate * record.effective_hours
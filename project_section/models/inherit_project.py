# -*- coding: utf-8 -*-
##############################################################################
#   Add Project Section by Project
##############################################################################
from openerp import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    section_line = fields.One2many('project.section', 'project_id',
                                   string='Section Lines', copy=True)

    #Подсчет полных трудозатрат и стоимости
    @api.depends('section_line')
    def _amount_all(self):
        for project in self:
            amount_total_cost = amount_total_labor = 0.0

            for section in project.section_line:
                amount_total_cost += section.planned_cost
                amount_total_labor += section.labor

            project.update({
                'amount_total_labor': project.currency_id.round(amount_total_labor),
                'amount_total_cost': project.currency_id.round(amount_total_cost),
            })

    amount_total_labor = fields.Monetary(string='Полная трудоемкость', store=True,
                                      readonly=True, compute='_amount_all')
    amount_total_cost = fields.Monetary(string='Полная план. стоимость', store=True,
                                      readonly=True, compute='_amount_all')
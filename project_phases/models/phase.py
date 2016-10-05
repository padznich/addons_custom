# -*- coding: utf-8 -*-

from openerp import models, fields, api


class CatalogPhases(models.Model):

    _name = 'catalog.phases'
    _description = 'Catalog of Project Phases'
    _rec_name = 'name'

    name = fields.Char(required=True, string='Фаза')
    description = fields.Char(string='Описание')
    sequence = fields.Integer('Sequence')


class ProjectPhases(models.Model):

    _name = 'project.phases'
    _description = 'Project Phases'
    _rec_name = 'phase_id'

    phase_id = fields.Many2one('catalog.phases', string='Фаза', ondelete='restrict', relation='data_section_rel')
    project_phase_line_id = fields.Many2one('project.project', string=_('Project'), ondelete='cascade')

    date_contract = fields.Date(string='Дата по контракту',
                              help="Planing date for the Project Phase")

    date_accomplish = fields.Date(string='Реальная Дата',
                              help="Real accomplish date for the Project Phase")

    currency_id = fields.Many2one('res.currency', string='Currency')
    revenue = fields.Monetary(string='Доходы', currency_field='currency_id',
                              help="Cost of the Project Phase")


class ProjectProject(models.Model):
    _inherit = 'project.project'

    phase_line = fields.One2many('project.phases', 'project_phase_line_id', string='Строка Фазы', copy=True)

    @api.depends('phase_line')
    def _amount_all(self):
        for project in self:
            amount_total_cost = 0.0
            #
            for phase in project.phase_line:
                amount_total_cost += phase.revenue

            project.update({
                'amount_total_cost': project.currency_id.round(amount_total_cost),
            })

    amount_total_cost = fields.Monetary(string='Суммарная Выручка', store=True,
                                      readonly=True, compute='_amount_all')


class TaskPhase(models.Model):
    _inherit = 'project.task'

    phase_id = fields.Many2one('project.phases', string='Phase',
                               help="Choose phase for the Task")

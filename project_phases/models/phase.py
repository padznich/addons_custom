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
    project_phase_line_id = fields.Many2one('project.project', string='Проект', ondelete='cascade')

    date_contract = fields.Date(string='Дата по контракту',
                                help="Planing date for the Project Phase")

    currency_id = fields.Many2one('res.currency', string='Currency')
    revenue = fields.Monetary(string='Доходы', currency_field='currency_id',
                              help="Cost of the Project Phase")

    gip = fields.Char(string='ГИП', related='project_phase_line_id.user_id.name', store=True)

    date_accomplish = fields.Char(string='Фактичекая дата', compute='_last_date')
    tasks_count = fields.Char(string='Число заданий в Фазе', store=True, readonly=True, compute='_last_date')
    tasks_completed = fields.Char(string='Число завершённых заданий в Фазе', store=True, readonly=True,
                                  compute='_last_date')
    accomplish = fields.Float(string="Выполнение", store=True, readonly=True, compute="_last_date")

    @api.depends('project_phase_line_id')
    def _last_date(self):

        for pp in self:
            last = None
            tasks_count = 0
            tasks_completed = 0
            for project in pp.project_phase_line_id:
                tasks_count = 0
                tasks_completed = 0
                for task in project.task_ids:
                    if pp.phase_id.name == task.phase_id.phase_id.name:
                        tasks_count += 1
                        if not last:
                            last = task.date_deadline
                        if last < task.date_deadline:
                            last = task.date_deadline
                        if task.stage_id.name == "Basic":
                            tasks_completed += 1

            try:
                accomplish = float(tasks_completed) / float(tasks_count) * 100.0
            except:
                accomplish = 0.0

            pp.update({
                'date_accomplish': last,
                'tasks_count': tasks_count,
                'tasks_completed': tasks_completed,
                'accomplish': accomplish,
            })




class ProjectProject(models.Model):
    _inherit = 'project.project'

    phase_line = fields.One2many('project.phases', 'project_phase_line_id', string='Строка Фазы', copy=True)

    @api.depends('phase_line')
    def _amount_all(self):
        for project in self:
            amount_total_cost = 0.0
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
                               help="Choose a phase for the Task")

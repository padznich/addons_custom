# -*- coding: utf-8 -*-

from datetime import datetime

from openerp import models, fields, api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP


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

    gip = fields.Char(string='ГИП', related='project_phase_line_id.user_id.name', store=True, readonly=True)

    date_accomplish = fields.Date(string='Фактичекая дата', compute='_last_date')
    tasks_count = fields.Integer(string='Число заданий в Фазе', readonly=True, compute='_last_date')
    tasks_completed = fields.Integer(string='Число завершённых заданий в Фазе', readonly=True,
                                     compute='_last_date')
    accomplish = fields.Float(string='Выполнение', readonly=True, compute="_last_date")

    diff_days = fields.Integer(string='Разница', compute="_last_date", readonly=True, store=True)

    @api.multi
    def sq(self):
        sql = ('SELECT country_id, array_agg(id) '
               'FROM res_partner '
               'WHERE active=true AND country_id IS NOT NULL '
               'GROUP BY country_id')
        self.env.cr.execute(sql)
        country_model = self.env['res.country']
        result = {}
        for country_id, partner_ids in self.env.cr.fetchall():
            country = country_model.browse(country_id)
        partners = self.search(
            [('id', 'in', tuple(partner_ids))]
        )
        result[country] = partners
        return result

    @api.multi
    def _last_date(self):

        for pp in self:
            for project in pp.project_phase_line_id:
                last = None
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
                except TypeError:
                    accomplish = 0.0    # BAD CODE
                except ZeroDivisionError:
                    accomplish = 0.0

                diff_days = (datetime.strptime(last, DEFAULT_SERVER_DATETIME_FORMAT) - datetime.strptime(pp.date_contract, DEFAULT_SERVER_DATETIME_FORMAT)).days
                # diff_days = (datetime.strptime(last, "%Y-%m-%d") - datetime.strptime(pp.date_contract, "%Y-%m-%d")).days

                # pp.date_accomplish = datetime.strptime(last, "%Y-%m-%d").date()
                # pp.diff_days = diff_days
                # pp.tasks_count = tasks_count
                # pp.tasks_completed = tasks_completed
                # pp.accomplish = accomplish
                pp.write({
                    "diff_days": diff_days,
                    "task_count": tasks_count,
                    "date_accomplish": datetime.strptime(last, DEFAULT_SERVER_DATETIME_FORMAT).strftime(DEFAULT_SERVER_DATE_FORMAT),
                    "tasks_completed": tasks_completed,
                    "accomplish": accomplish,
                })

                # sql = ('UPDATE project_phases '
                #        'SET diff_days = {diff_days} '
                #        'WHERE id = {id}'.format(
                #             diff_days=diff_days,
                #             id=pp.id
                # )
                # )
                # self.env.cr.execute(sql)

                # sql = ('UPDATE project_phases SET date_accomplish = {date_accomplish} WHERE id = {id}'.format(
                #     date_accomplish=datetime.strptime(last, "%Y-%m-%d"),
                    # date_accomplish=datetime.strptime(last, "%Y-%m-%d").date(),
                    # id=pp.id)
                # )
                # sql = (
                #     'INSERT INTO project_phases(date_accomplish) '
                #     'VALUES ({date_accomplish}) '
                #     'WHERE id = {id}'.format(
                #         date_accomplish=datetime.strptime(last, "%Y-%m-%d").date(),
                #         id=pp.id)
                # )
                # self.env.cr.execute(sql)

                # pp.update({
                #     'date_accomplish': last,
                #     'tasks_count': tasks_count,
                #     'tasks_completed': tasks_completed,
                #     'accomplish': accomplish,
                #     'diff_days': diff_days,
                # })


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

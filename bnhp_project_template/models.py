# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging


_logger = logging.getLogger(__name__)


class BNHP(models.Model):
    _inherit = 'project.project'
    _description = 'Adds new fields'

    code = fields.Char("Номер договора")
    contract_amount = fields.Float("Сумма по договору")
    gip = fields.Many2one('res.users', 'ГИП')
    priority = fields.Many2one('bnhp_project_template.priority', 'Приоритет', select=True)
    status = fields.Many2one('bnhp_project_template.status', 'Статус', select=True)
    # phase_ids = fields.Many2many('catalog.phases', 'Стадия', select=True)
    dead_line_date = fields.Date('Дата завершения')


class Status(models.Model):
    _name = 'bnhp_project_template.status'
    _description = 'Status catalog'

    number = fields.Integer("Код статуса")
    name = fields.Char("Название статуса")


class Priority(models.Model):
    _name = 'bnhp_project_template.priority'
    _description = 'Priority catalog'

    number = fields.Integer("Код приоритета")
    name = fields.Char("Название приоритета")


class Expertise(models.Model):
    _inherit = 'project.project'
    _description = 'Fields for Expertise'

    exp_code = fields.Char("№ договора с экспертизой")
    exp_date_to_pay = fields.Date("Дата оплаты экспертизы")
    exp_date_to_pass = fields.Date("Дата передачи на экспертизу")
    exp_date_to_finish = fields.Date("Срок окончания экспертизы")
    exp_number = fields.Integer("Номер заключения экспертизы")

    section_ids = fields.Many2many('project.section.list')
    exp_date_of_remark = fields.Date("Дата получения замечаний")
    exp_date_of_send = fields.Date("Дата отправки ответа")
    exp_date_of_unremark = fields.Date("Дата снятия замечаний")



class Agreement(models.Model):
    _inherit = 'project.project'
    _description = 'Fields for Agreement'

    agr_code = fields.Char("Код для согласования")
    agr_name = fields.Char("Наименование органа согласования")
    agr_date_to_send = fields.Date("Дата направления на согласования")
    agr_date_to_receive = fields.Date("Дата получения согласования")

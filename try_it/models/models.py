# -*- coding: utf-8 -*-

from openerp import models, fields, api


class TryIt(models.Model):
    _name = 'try_it.try_it'

    name = fields.Char()
    value = fields.Float()
    tax = fields.Float(string='Spam')
    total = fields.Float(compute='_compute_total', store=True)
    description = fields.Text()

    sub_revenue = fields.Many2one('try_it.sub', string='Best Choice', store=True)
    # sub_revenue = fields.Char(related='try_it.sub.name', string='Best Choice', store=True)
    # sub_revenue = fields.Char(related='user_id.partner_id')
    # sub_revenue = fields.Char()

    @api.depends('value', 'tax')
    def _compute_total(self):
        self.total = float(self.value) * (100 - float(self.tax)) / 100

    # @api.depends('value', 'tax')
    # def _compute_total(self):
    #     for record in self:
    #         record.total = record.value + record.value * record.tax


class SubTryIt(models.Model):
    _name = 'try_it.sub'

    name = fields.Char()
    date_from = fields.Date()
    date_to = fields.Date()

    revenue = fields.Float()


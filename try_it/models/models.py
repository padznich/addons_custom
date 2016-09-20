# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TryIt(models.Model):
    _name = 'try_it.try_it'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    sub_revenue = fields.Char(string='Best Choice',
                              store=True,
                              related='try_it.sub.name')

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100


class SubTryIt(models.Model):
    _name = 'try_it.sub'

    name = fields.Char()
    date_from = fields.Date()
    date_to = fields.Date()

    revenue = fields.Float()


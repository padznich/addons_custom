# -*- coding: utf-8 -*-

from openerp import models, fields


class CatalogPhases(models.Model):
    _name = 'catalog.phases'

    name = fields.Char(required=True, string='Phase Name')
    color = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
                             default=('1', '1'),
                             string='Color')
    priority = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                                default=('1', '1'),
                                string='Priority')
    description = fields.Char(string='Description')

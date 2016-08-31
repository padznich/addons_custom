# -*- coding: utf-8 -*-

from openerp import models, fields


class CatalogPhases(models.Model):

    _name = 'catalog.phases'

    name = fields.Char(required=True, default='Catalog name')
    color = fields.Integer(default=1)
    priority = fields.Integer(default=1)
    description = fields.Char()




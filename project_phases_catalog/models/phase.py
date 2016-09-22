# -*- coding: utf-8 -*-

from openerp import models, fields
from openerp.tools.translate import _


class CatalogPhases(models.Model):
    _name = 'catalog.phases'
    _description = 'Phases Catalog'

    name = fields.Char(required=True, string=_('Phase Name'))
    color = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
                             default='1',
                             string=_('Color'))
    priority = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                                default='1',
                                string=_('Priority'))
    description = fields.Char(string=_('Description'))


class ProjectPhasesRel(models.Model):
    _name = 'catalog.phase'
    _description = 'Extended Phases Catalog'

    project_id = fields.Many2one('project.project', string=_('Project'))
    phase_id = fields.Many2one('catalog.phases', string=_('Phase'))
    date_contract = fields.Date(string=_('Contract Date'))
    revenue = fields.Float(string=_('Revenue'))

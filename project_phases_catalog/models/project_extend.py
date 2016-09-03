# -*- coding: utf-8 -*-

from openerp import models, fields


class ProjectPhaseField(models.Model):

    _inherit = 'project.project'

    phase_id = fields.Many2many(comodel_name='catalog.phases',
                                column1='name', column2='color', string='Phase')
    # phase_id = fields.Many2many('catalog.phases', string='Phase')

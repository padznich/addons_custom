# -*- coding: utf-8 -*-

from openerp import models, fields
from openerp.tools.translate import _


class ProjectPhaseField(models.Model):

    _inherit = 'project.project'

    phase_id = fields.Many2many(comodel_name='catalog.phases',
                                column1=_('name'), column2=_('color'), string=_('Phase'))

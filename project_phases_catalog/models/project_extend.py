# -*- coding: utf-8 -*-

from openerp import models, fields
from openerp.tools.translate import _


class ProjectPhases(models.Model):

    _inherit = 'project.project'

    phase_ids = fields.Many2many('catalog.phase', string=_('Phases'))

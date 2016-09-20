# -*- coding: utf-8 -*-

from openerp import models, fields
from openerp.tools.translate import _


class TaskPhase(models.Model):

    _inherit = 'project.task'

    phase_id = fields.Many2one('catalog.phase', string=_('Phase'))

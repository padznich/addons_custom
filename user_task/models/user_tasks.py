# -*- coding: utf-8 -*-

from openerp import models, fields, api


class UserTasks(models.Model):

    _inherit = ['project.task']
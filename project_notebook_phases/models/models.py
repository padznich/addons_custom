# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Phase(models.Model):
    _inherit = 'project.project'
# class project_notebook_etapi(models.Model):
#     _name = 'project_notebook_etapi.project_notebook_etapi'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime
from openerp.exceptions import except_orm, Warning, RedirectWarning

class NewFolderChild(models.Model):

    _name = 'new_folder_child'

    _inherit = ['ir.needaction_mixin']

    
    file = fields.Many2many('ir.attachment')

    name = fields.Char()

    uploaded = fields.Many2many('new_folder_child','relation','name', string="uploaded")

    color = fields.Integer()


class NewFolder(models.Model):

    _name = 'new_folder'

    _inherit = ['ir.needaction_mixin']

    file = fields.Many2many('ir.attachment')

    name = fields.Char()

    uploaded = fields.Many2many('new_folder_child', 'name', string="uploaded")

    res_model = fields.Many2one('ir.model', string="Related Model")

    color = fields.Integer()

    @api.model
    def _needaction_count(self, domain=None):
        count = self.search_count([])
        return (count)

    @api.model
    def create(self, vals):
        name_list = []
        for folder in self.search([]):
            name_list.append(folder.name)
        if vals.get('name') in name_list:
            raise Warning("Folder name already exist !")
        folder = super(NewFolder, self).create(vals)
        return folder

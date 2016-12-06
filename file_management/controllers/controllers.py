# -*- coding: utf-8 -*-
from openerp import http

# class FolderManagement(http.Controller):
#     @http.route('/folder_management/folder_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/folder_management/folder_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('folder_management.listing', {
#             'root': '/folder_management/folder_management',
#             'objects': http.request.env['folder_management.folder_management'].search([]),
#         })

#     @http.route('/folder_management/folder_management/objects/<model("folder_management.folder_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('folder_management.object', {
#             'object': obj
#         })
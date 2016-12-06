# -*- coding: utf-8 -*-
from openerp import http

# class Addons/projectLeftsidePanel(http.Controller):
#     @http.route('/addons/project_leftside_panel/addons/project_leftside_panel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/project_leftside_panel/addons/project_leftside_panel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/project_leftside_panel.listing', {
#             'root': '/addons/project_leftside_panel/addons/project_leftside_panel',
#             'objects': http.request.env['addons/project_leftside_panel.addons/project_leftside_panel'].search([]),
#         })

#     @http.route('/addons/project_leftside_panel/addons/project_leftside_panel/objects/<model("addons/project_leftside_panel.addons/project_leftside_panel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/project_leftside_panel.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from openerp import http

# class Addons/budget(http.Controller):
#     @http.route('/addons/budget/addons/budget/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/budget/addons/budget/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/budget.listing', {
#             'root': '/addons/budget/addons/budget',
#             'objects': http.request.env['addons/budget.addons/budget'].search([]),
#         })

#     @http.route('/addons/budget/addons/budget/objects/<model("addons/budget.addons/budget"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/budget.object', {
#             'object': obj
#         })
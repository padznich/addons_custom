# -*- coding: utf-8 -*-
from openerp import http

# class TryIt(http.Controller):
#     @http.route('/try_it/try_it/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/try_it/try_it/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('try_it.listing', {
#             'root': '/try_it/try_it',
#             'objects': http.request.env['try_it.try_it'].search([]),
#         })

#     @http.route('/try_it/try_it/objects/<model("try_it.try_it"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('try_it.object', {
#             'object': obj
#         })
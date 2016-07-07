# -*- coding: utf-8 -*-
from openerp import http

# class Learn1(http.Controller):
#     @http.route('/learn1/learn1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/learn1/learn1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('learn1.listing', {
#             'root': '/learn1/learn1',
#             'objects': http.request.env['learn1.learn1'].search([]),
#         })

#     @http.route('/learn1/learn1/objects/<model("learn1.learn1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('learn1.object', {
#             'object': obj
#         })
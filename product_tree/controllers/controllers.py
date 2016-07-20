# -*- coding: utf-8 -*-
from openerp import http

# class Addons/productTree(http.Controller):
#     @http.route('/addons/product_tree/addons/product_tree/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/product_tree/addons/product_tree/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/product_tree.listing', {
#             'root': '/addons/product_tree/addons/product_tree',
#             'objects': http.request.env['addons/product_tree.addons/product_tree'].search([]),
#         })

#     @http.route('/addons/product_tree/addons/product_tree/objects/<model("addons/product_tree.addons/product_tree"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/product_tree.object', {
#             'object': obj
#         })
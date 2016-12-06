# -*- coding: utf-8 -*-
from openerp import http

# class UserTask(http.Controller):
#     @http.route('/user_task/user_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_task/user_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_task.listing', {
#             'root': '/user_task/user_task',
#             'objects': http.request.env['user_task.user_task'].search([]),
#         })

#     @http.route('/user_task/user_task/objects/<model("user_task.user_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_task.object', {
#             'object': obj
#         })
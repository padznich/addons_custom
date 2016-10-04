# -*- coding: utf-8 -*-
from openerp import http

# class ProjectNotebookEtapi(http.Controller):
#     @http.route('/project_notebook_etapi/project_notebook_etapi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_notebook_etapi/project_notebook_etapi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_notebook_etapi.listing', {
#             'root': '/project_notebook_etapi/project_notebook_etapi',
#             'objects': http.request.env['project_notebook_etapi.project_notebook_etapi'].search([]),
#         })

#     @http.route('/project_notebook_etapi/project_notebook_etapi/objects/<model("project_notebook_etapi.project_notebook_etapi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_notebook_etapi.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from openerp import http

# class ProjectPhases(http.Controller):
#     @http.route('/project_phases/project_phases/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_phases/project_phases/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_phases.listing', {
#             'root': '/project_phases/project_phases',
#             'objects': http.request.env['project_phases.project_phases'].search([]),
#         })

#     @http.route('/project_phases/project_phases/objects/<model("project_phases.project_phases"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_phases.object', {
#             'object': obj
#         })
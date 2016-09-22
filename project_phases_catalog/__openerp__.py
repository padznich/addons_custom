# -*- coding: utf-8 -*-
{
    'name': "Project Phases Catalog",

    'summary': """Project phases catalog""",

    'description': """Setting up a phases for project""",

    'author': "padznich",
    'website': "softin.cloud",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Phases',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/catalog_views.xml',
        'views/project_notebook.xml',
        'views/projects_tree_extended.xml',
        'views/task_extend.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
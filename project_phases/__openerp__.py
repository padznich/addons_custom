# -*- coding: utf-8 -*-
{
    'name': "Project Phases",

    'summary': """Project phases""",

    'description': """Setting up a phases for project""",

    'author': "padznich",
    'website': "softin.cloud",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'views/catalog_phases_view.xml',
        'views/project_phases_view.xml',
        'views/task_phase_view.xml',
        # 'views/phases_catalog_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
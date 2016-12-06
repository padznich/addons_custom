# -*- coding: utf-8 -*-
{
    'name': "User tasks",

    'summary': """
        Single user tasks
        """,

    'description': """
        Add user tasks on the main panel.
            """,

    'author': "padznich",
    'website': "http://softin.cloud",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/user_tasks_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
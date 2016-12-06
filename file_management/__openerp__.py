# -*- coding: utf-8 -*-
{
    'name': "Document Management System",

    'summary': """
        Manage Your Files Heirarchy.""",

    'description': """
        Manage your folders by create and store unlimited items inside a folder.
    """,

    'author': "CIS",
    'website': "https://www.cisin.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Document',
    'version': '9.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
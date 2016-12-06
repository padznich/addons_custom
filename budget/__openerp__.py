# -*- coding: utf-8 -*-
{
    'name': "Budget",

    'summary': """Budget for builders.""",

    'description': """It's really helps to your work!""",

    'author': "padznich",
    'website': "http://softin.cloud",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'purchase_requisition', 'purchase', 'account', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
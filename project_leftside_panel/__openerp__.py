# -*- coding: utf-8 -*-
{
    'name': "project_leftside_panel",

    'summary': """Добавлены собственные ссылки на вкладку Project""",

    'description': """Добавлены: Счета, Закупки, Проблемы, Бюджет""",

    'author': "padznich",
    'website': "http://www.yourcompany.com",

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
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
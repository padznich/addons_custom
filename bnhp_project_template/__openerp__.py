# -*- coding: utf-8 -*-
{
    'name': "bnhp_project_template",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'project_phases'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/main_view.xml',
        # 'views/expertise.xml',
        # 'views/agreement.xml',
        'data/data_priorities.xml',
        'data/data_statuses.xml',
    ],
}
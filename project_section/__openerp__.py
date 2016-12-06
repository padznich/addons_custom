# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': 'Project Sections',
    'version': '1.0.0',
    'category': 'Projects & Services',
    'sequence': 15,
    'summary': '',
    'description': """
Project Sections
==================
Add project sections
    """,
    'author':  'ShEV',
    'website': 'www',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'project',
        'project_timesheet',
        'decimal_precision',
    ],
    'data': [
        'views/project_view.xml',
        'views/project_data.xml',
        'views/project_section_view.xml',
        'views/project_section_list_view.xml',
        'views/project_task_section_view.xml',
        # 'report/project_report_view.xml',
        # 'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
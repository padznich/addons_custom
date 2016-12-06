# -*- coding: utf-8 -*-
from openerp import models, fields

class SectionByTaskReport(models.Model):
    _inherit = 'report.project.task.user'

    section_id = fields.Many2one('project.section', 'Раздел')

    def _select(self):
        select_str = """
             SELECT
                    t.section_id as section_id,
        """
        return select_str

    def _group_by(self):
        group_by_str = """
                GROUP BY
                    section_id
        """
# -*- coding: utf-8 -*-

from openerp import models, fields, api

import random
from random import randint
import string


class Learn1(models.Model):
    _name = 'learn1.learn1'

    name = fields.Char(required=True, default='Click on generate name!')
    description = fields.Char()

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)


    @api.multi
    def generate_record_name(self):
        self.ensure_one()
        self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                                    for _ in range(randint(9, 15)))
                    })

    @api.multi
    def generate_record_description(self):
        self.ensure_one()
        self.write({'description': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                                           for _ in range(randint(12, 15)))
                    })

    @api.multi
    def clear_record_data(self):
        self.ensure_one()
        self.write({'name': '', 'description': ''})


class Session(models.Model):
    _name = 'learn1.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()

    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=[('instructor', '=', True)])
    course_id = fields.Many2one('learn1.learn1', ondelete='cascade', string="Course", required=True)


# -*- coding: utf-8 -*-

from openerp import models, fields, api

import openerp.addons.decimal_precision as dp


class Document(models.Model):
    # _inherit = "account.invoice.line"
    _name = 'budget.document'

    author = fields.Many2one('res.users', string="Author", required=True)
    partner_id = fields.Many2one('res.partner', string="Client", required=True)
    currency_id = fields.Many2one('res.currency', related='invoice_id.currency_id', store=True)
    opportunity = fields.Many2one('crm.lead', string="Opportunity")
    create_date = fields.Datetime(required=True)

    # sequence = fields.Integer(default=10, help="Gives the sequence of this line when displaying the invoice.")
    product_id = fields.Many2one('product.product', string='Product', ondelete='restrict', index=True)
    quantity = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'),
                            required=True, default=1)

    invoice_id = fields.Many2one('account.invoice', string='Invoice', ondelete='cascade', index=True)
    invoice_line_ids = fields.One2many('account.invoice.line', 'invoice_id', string='Invoice Lines')
    company_id = fields.Many2one('res.partner', string="Vendor", required=True)
    uom_id = fields.Many2one('product.uom', string='Unit of Measure', ondelete='set null', index=True, oldname='uos_id')
    price_unit = fields.Float(string='Unit Price', required=True, digits=dp.get_precision('Product Price'))

    category = fields.Selection(selection=[('material', 'Material'),
                                           ('equipment', 'Equipment'),
                                           ('work', 'Work'),
                                           ('costs', 'Costs')])

    discount = fields.Float(string='Discount (%)', digits=dp.get_precision('Product Price'))
    nds = fields.Float(string='NDS (%)', digits=dp.get_precision('Product Price'))

    @api.one
    @api.depends('price_unit', 'discount', 'quantity')
    def _compute_price(self):
        self.price_subtotal = self.quantity * self.price_unit
        self.price_subtotal_disc = self.price_subtotal * (1 + (self.discount or 0.0) / 100.0)
        self.price_subtotal_nds = self.price_subtotal_disc * (1 + (self.nds or 0.0) / 100.0)
        return self

    price_subtotal = fields.Float(string='Amount', store=True, readonly=True,
                                  digits=dp.get_precision('Account'), compute='_compute_price',
                                  help="Total amount. unit_price * quantity")
    price_subtotal_disc = fields.Float(string='Amount with Discount', store=True, readonly=True,
                                       digits=dp.get_precision('Account'), compute='_compute_price',
                                       help="Amount * (1 + discount)")
    price_subtotal_nds = fields.Float(string='Amount with NDS', store=True, readonly=True,
                                      digits=dp.get_precision('Account'), compute='_compute_price',
                                      help="Amount * (1 + NDS)")

    @api.one
    @api.depends('quantity')
    def _compute_amount(self):
        self.int_sum = self.quantity
        return self

    int_sum = fields.Float(string='Subtotal',
                           digits=dp.get_precision('Account'),
                           store=True,
                           readonly=True,
                           compute='_compute_amount',
                           track_visibility='always')

    comment = fields.Text()
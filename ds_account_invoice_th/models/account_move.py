from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_ds_tax_invoice_date = fields.Date(
        string='Tax Invoice Date',
        index=True,
        copy=False,
    )

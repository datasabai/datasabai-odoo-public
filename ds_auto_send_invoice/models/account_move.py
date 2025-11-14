import logging
from odoo import models, fields
from odoo.tools import config

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    ds_auto_send = fields.Boolean(string='Auto-send', copy=False,    )
    
    def _post(self, soft=True):
        posted_moves = super()._post(soft=soft)
        posted_moves.filtered(lambda m: m.move_type in ('out_invoice', 'out_refund') 
                and m.state == "posted" 
                and m.auto_post 
                and m.ds_auto_send 
                and not m.is_move_sent
                and m._is_ready_to_be_sent()
        )._auto_send_invoice()

        return posted_moves

    def _auto_send_invoice(self):
        for invoice in self:
            if invoice.partner_id.invoice_sending_method != "email":
                invoice.message_post(body='Auto-send failed, since the customer`s default Invoice sending method is not by email')
            else:
                email_context = {**self.env.context.copy(), **{
                    'total_amount': self.amount_total,
                    'email_to': self.partner_id.email,
                    'currency': self.currency_id.name,
                    'no_new_invoice': True}}
                self.env['account.move.send'].with_context(email_context)._generate_and_send_invoices(
                        self,
                        allow_raising=False,
                        allow_fallback_pdf=True,
                    )
                
                # invoice.message_subscribe(invoice.partner_id.ids)

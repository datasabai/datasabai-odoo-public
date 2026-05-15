from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'
    
    ds_no_date = fields.Boolean('No date in the PDF', default=False, help="If checked, the date will not be printed in the PDF of the quotation or invoice.")

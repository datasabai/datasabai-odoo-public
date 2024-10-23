# -*- coding: utf-8 -*-

from odoo import _, models
from odoo.exceptions import UserError
from io import StringIO


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    def _import_bank_statement(self, attachments):
        # In case of CSV files, only one file can be imported at a time.
        if len(attachments) > 1:
            csv = [bool(self._check_file_format(att.name)) for att in attachments]
            if True in csv and False in csv:
                raise UserError(_('Mixing CSV files with other file types is not allowed.'))
            if csv.count(True) > 1:
                raise UserError(_('Only one CSV file can be selected.'))
            return super()._import_bank_statement(attachments)

        if not self._check_file_format(attachments.name):
            return super()._import_bank_statement(attachments)
        
        attachments.raw = self.x_ds_preprocess_statement_kbank (attachments.raw)
        # return super()._import_bank_statement(attachments)
        ctx = dict(self.env.context)
        import_wizard = self.env['base_import.import'].create({
            'res_model': 'account.bank.statement.line',
            'file': attachments.raw,
            'file_name': attachments.name,
            'file_type': attachments.mimetype,
        })
        ctx['wizard_id'] = import_wizard.id
        ctx['default_journal_id'] = self.id
        return {
            'type': 'ir.actions.client',
            'tag': 'import_bank_stmt',
            'params': {
                'model': 'account.bank.statement.line',
                'context': ctx,
                'filename': 'bank_statement_import.csv',
            }
        }

    def x_ds_preprocess_statement_kbank(self, raw):
        data_file = raw.decode('utf-8')
        if not data_file:
            return raw
        
        line = StringIO(data_file).readlines()[1]
        if not 'K-DEPOSIT STATEMENT' in line:
            return raw
            
        file_data = ""

        for line in StringIO(data_file).readlines()[11:]:
            old_line = line.index(",", 0)
            if old_line == 0:
                newstr = line[:old_line] + line[old_line+1:]
                file_data += newstr
            else:
                file_data += line

        return file_data

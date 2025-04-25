{
    "name": "Import Kasikorn bank statement in CSV file",
    'version': '18.0.0.0.1',
    'description': r'''
Module to import Kasikorn bank statements in CSV file.
======================================================

This module allows you to import CSV Files of Kasikorn bank statement in Odoo.

Important Note
---------------------------------------------
* Because of the CSV format limitation, the Date format might need to be adjusted manualy into DD-MM-YY
* Field mapping:    Date (Date); Withdrawal (Debit); Deposit (Credit); Outstanding Balance (Cumulative Balance); Details (Label)
''',
    # "description": "Allow Odoo to import Kasikorn bank statement",
    "author": "Weexa",
    "website": "http://www.weexa.com",
    'license': 'OEEL-1',
    "category": "Accounting/Accounting",
    "application": False,
    "installable": True,
    "auto_install": False,

    "depends": ['account_bank_statement_import_csv'],
    "data": [
    ],

}

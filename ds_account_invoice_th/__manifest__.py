{
    'name': 'Thailand Invoice',
    'version': '19.0.1.3',
    'summary': "Customizations for Compliance with Thai Invoice Regulations",
    'description': """
This module customizes the standard module to ensure compliance with Thai invoice regulations.
Key features include:
- Print Tax Invoice according to tax invoice date
- Allow Quotation and Invoice to be printed without Date per settings in Customer
    """,
    'author': "Datasabai",
    'website': "https://www.datasabai.com",
    "category": "Accounting/Accounting",
    'license': 'OEEL-1',
    'installable': True,
    'application': False,
    'auto_install': False,

    'depends': [
        'account', 'l10n_th', 'sale'
    ],
    'data': [
        'views/account_move_views.xml',
        'views/res_partner_views.xml',
        'reports/account_report_invoice.xml',
        'reports/sale_report_templates.xml',
    ]
}

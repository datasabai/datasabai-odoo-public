{
    'name': 'Thailand Invoice',
    'version': '0.2',
    'summary': "Customizations for Compliance with Thai Invoice Regulations",
    'description': """
This module customizes the standard module to ensure compliance with Thai invoice regulations.
    """,
    'author': "Datasabai",
    'website': "https://www.datasabai.com",
    "category": "Accounting/Accounting",
    'license': 'OEEL-1',
    'installable': True,
    'application': False,
    'auto_install': False,

    'depends': [
        'account', 'l10n_th'
    ],
    'data': [
        'views/account_report_invoice.xml',
        'views/account_move_views.xml',
    ]
}

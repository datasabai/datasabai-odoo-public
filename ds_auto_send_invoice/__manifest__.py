{
    'name': 'Auto-Send Customer Invoice',
    'version': '0.1',
    'category': 'Accounting/Accounting',
    'summary': "Automatically send customer invoice by email",
    'description': """
This module customizes the standard accounting to automatically send customer invoice by email.
    """,
    'author': "Datasabai",
    'website': "https://www.datasabai.com",
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,

    'depends': [
        'account'
    ],
    'data': [
        'views/account_move_views.xml',
    ]
}

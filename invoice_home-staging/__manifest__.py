# -*- coding: utf-8 -*-
{
    'name': "inovice_home-staging",

    'summary': """
        Modelo de factura personalizada de Home Staging""",

    'description': """
        Modelo de factura personalizada de Home Staging
    """,

    'author': "FJMR",
    'website': "https://www.enzo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/reportHOMESTAGING.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
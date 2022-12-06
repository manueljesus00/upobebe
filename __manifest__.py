# -*- coding: utf-8 -*-
{
    'name': "upobebe",

    'summary': """
        Modulo especifico para la gestion de articulos de UPOBEBE
        """,

    'description': """
        Modulo especifico para la gestion de articulos de UPOBEBE
    """,

    'author': "Manuel Jesus Flores",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/articulos.xml',
        'views/estadoArticulo_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

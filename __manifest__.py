# -*- coding: utf-8 -*-
# Version:      0.1.0
# Modelo:       Transaccion
# Editor:       Manuel Jesus Flores Montano (@manueljesus00) and Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    11/11/2022
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
    'version': '0.1.0',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/cliente_report.xml',
        'reports/empleados_report.xml',
        'views/cliente_view.xml',
        'views/suscripcion_view.xml',
        'views/tipoTransaccion_view.xml',
        'views/Transaccion.xml',
        'views/empleado.xml',
        'views/articulos.xml',
        'views/estadoArticulo_view.xml',
        'views/cargo_view.xml',
        'views/producto_view.xml',
        'views/categoria_view.xml',
        'views/financiacion_view.xml',
        'views/articulos.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

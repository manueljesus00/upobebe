# -*- coding: utf-8 -*-
# Version:      0.1.0
# Modelo:       Transaccion
# Editor:       Manuel Jesus Flores Montano (@manueljesus00) and Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    11/11/2022
{
    'name': "upobebe",
    'summary': """
        Modulo destinado a la gestion de una tienda de articulos para bebe""",

    'description': """
        Este modulo en especifico gestiona las transacciones realizadas dentro
        de la propia tienda. Tiene 6 claves foraneas y una clave primaria.
    """,

    'author': "Manuel Jesus Flores Montano",
    'website': "https://www.github.com/manueljesus00/upobebe",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.0',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/cliente_view.xml',
        'views/suscripcion_view.xml',
        #'views/tipoTransaccion_view.xml',
        'views/Transaccion.xml',
        'views/menu.xml',
        'views/empleado.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

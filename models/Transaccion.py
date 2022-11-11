# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Transaccion
# Editor:       Manuel Jesus Flores Montano (@manueljesus00)
# Fecha rev:    11/11/2022


# from odoo import models, fields, api

from odoo import models, fields, api
class Transaccion(models.Model):
    _name = 'upobebe.transaccion'
    _description = 'Transaccion en UPOBebe'

    idTransaccion =  fields.Integer("ID. de la transaccion",required=True)
    tipoTransaccion = fields.Many2one("upobebe.tipotransaccion",string="Tipo de transaccion",required=True)
    dniEmpleado = fields.Many2one("upobebe.empleado",string="Empleado",required=True)
    #idSeguimiento = fields.One2one("upobebe.seguimiento",string="Numero de seguimiento")   TODO = Ver como hago un 1 to 1
    idArticulo = fields.One2Many("upobebe.articulo","field_articulos",string="Articulos", required=True)
    idProveedor = fields.Many2one("upobebe.proveedor",string="Proveedor")
    dniCliente = fields.Many2one("upobebe.cliente", string="Cliente") # Puede ser que no haya cliente sino proveedor
    fechaTransaccion = fields.Datetime('Fecha de compra',required=True, autodate=True)


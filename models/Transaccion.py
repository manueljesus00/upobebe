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

    idTransaccion =  fields.Integer("ID. de la transaccion",required=True,store=True)
    # Mirar que funcione asi para un autoincremental, sino se hace computando el id
    # Pendiente de testing
    
    tipotransaccion_id = fields.Many2one("upobebe.tipotransaccion", required=True, string="Tipo de transaccion")
    dniEmpleado = fields.Many2one("upobebe.empleados",string="Empleado",required=True)
    id_financiacion = fields.Many2many("upobebe.financiacion", string="Financiacion", required=True)
    #idSeguimiento = fields.Integer(string="Numero de seguimiento") #Tienen que ser relaciones
    #idArticulo = fields.One2many("upobebe.articulo","field_articulos",string="Articulos", required=True)
    #idProveedor = fields.Many2one("upobebe.proveedor",string="Proveedor")
    #dniCliente = fields.Many2one("upobebe.cliente", string="Cliente", size=9)
    fechaTransaccion = fields.Datetime('Fecha de compra',required=True, autodate=True)
    
    _sql_constraints = [('transaccion_idTransaccion_unique','UNIQUE (idTransaccion)','El id de la transaccion debe ser único')]
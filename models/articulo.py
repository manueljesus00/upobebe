# -*- coding: utf-8 -*-

# Version:      0.2.1
# Modelo:       Articulo
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum) and Manuel Jesus Flores Montaño (@manueljesus00)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class articulo(models.Model):
    _name = 'upobebe.articulo'
    _description = 'upobebe.articulo'

    id_articulo = fields.Integer(required=True, readonly=True, copy=True, index=True, string="ID Articulo")
    photo = fields.Binary('Photo')
    precio = fields.Float(required=True)

    num_Almacen = fields.Many2one("upobebe.almacen","Numero de almacen", required=True)
    tipoEstado = fields.Many2one("upobebe.estadoarticulo", required=True,string="Estado")
    producto_id = fields.Many2one("upobebe.producto", required=True, string="Producto")

    
    _sql_constraints = [('articulo_id_Articulo_unique', 'UNIQUE (id_articulo)', 'El id del articulo debe ser unico')]

    @api.constrains("precio")
    def _check_precio(self):
        if len(self.precio) < 0 or len(self.precio) > 6:
            raise models.ValidationError("El precio debe tener como maximo 6 digitos")
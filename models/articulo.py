# -*- coding: utf-8 -*-

# Version:      0.2.1
# Modelo:       Articulo
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum) and Manuel Jesus Flores Montaño (@manueljesus00)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class articulo(models.Model):
    _name = 'upobebe.articulo'
    _description = 'upobebe.articulo'

    idArticulo = fields.Integer(required=True, readonly=True, copy=True, index=True, string="ID Articulo")
    photo = fields.Binary('Photo')
    precio = fields.Float(required=True)

    num_Almacen = fields.Many2one("upobebe.almacen","Numero de almacen", required=True)
    tipoEstado = fields.Many2one("upobebe.estadoarticulo", required=True,string="Estado")
    # nombreProducto = fields.Many2one("upobebe.articulo","Tipo de articulo", required=True)

    _sql_constraints = [('idArticulo_unique', 'unique(idArticulo)', 'El id del articulo debe ser unico')]

    @api.constrains("precio")
    def _check_precio(self):
        if len(self.precio) < 0 or len(self.precio) > 6:
            raise models.ValidationError("El precio debe tener como maximo 6 digitos")
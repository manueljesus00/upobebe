# -*- coding: utf-8 -*-

# Version:      0.2.0
# Modelo:       Articulo
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum) and Manuel Jesus Flores Montaño (@manueljesus00)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class articulo(models.Model):
    _name = 'upobebe.articulo'
    _description = 'upobebe.articulo'

    idArticulo = fields.Integer(required=True, readonly=True, copy=True, index=True, string="ID Articulo")
    photo = fields.Binary('Photo')
    precio = fields.Float(size=6, required=True)

    # numAlmacen = fields.Many2one("upobebe.almacen","Numero de almacen", required=True)
    tipoEstado = fields.Many2one("upobebe.estadoArticulo", required=True, string="Estado")
    # nombreProducto = fields.Many2one("upobebe.articulo","Tipo de articulo", required=True)

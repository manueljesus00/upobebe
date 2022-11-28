# -*- coding: utf-8 -*-

from odoo import models, fields, api


class articulo(models.Model):
    _name = 'upobebe.articulo'
    _description = 'upobebe.articulo'

    idArticulo = fields.Integer(required=True, readonly=True, copy=True, index=True, string="ID Articulo")
    numAlmacen = fields.Many2one("upobebe.almacen","Numero de almacen", required=True)
    tipoEstado = fields.Many2one("upobebe.estado","Estado del producto", required=True)
    nombreProducto = fields.Many2one("upobebe.articulo","Tipo de articulo", required=True)
    precio = fields.Float(size=6, required=True)

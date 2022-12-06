# -*- coding: utf-8 -*-

# Version:      0.1.1
# Modelo:       estadoArticulo
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    06/12/2022

from odoo import models, fields


class estadoArticulo(models.Model):
    _name = 'upobebe.estadoarticulo'
    _description = 'upobebe.estadoArticulo'

    name = fields.Char(string="Estado", required=True, help="Estado del articulo")

    articulo_ids = fields.One2many("upobebe.articulo", 'tipoEstado', 'Articulos')




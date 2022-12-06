# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       estadoArticulo
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class estadoArticulo(models.Model):
    _name = 'upobebe.estadoArticulo'
    _description = 'upobebe.estadoArticulo'

    estado = fields.Integer(string="Estado", required=True)

    articulo_ids = fields.One2many("upobebe.articulo", 'estado', 'Articulos')




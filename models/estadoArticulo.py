# -*- coding: utf-8 -*-

# Version:      0.1.1
# Modelo:       estadoArticulo
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class estadoArticulo(models.Model):
    _name = 'upobebe.estadoarticulo'
    _description = 'upobebe.estadoArticulo'

    name = fields.Char(string="Estado", required=True, help="Estado del articulo")
    descripcion = fields.Text(string="Descripcion", required=True, help="Descripcion del estado del articulo")

    articulo_ids = fields.One2many("upobebe.articulo", 'tipoEstado', 'Articulos')

    @api.constrains('name')
    def _check_name(self):
        if len(self.name) > 30:
            raise models.ValidationError("El nombre no debe tener mas de 30 caracteres")

    @api.constrains('descripcion')
    def _check_descripcion(self):
        if len(self.descripcion) > 120:
            raise models.ValidationError("La descripcion no debe tener mas de 120 caracteres")




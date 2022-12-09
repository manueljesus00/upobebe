# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Categoria
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    09/12/2022

from odoo import models, fields, api

class Categoria(models.Model):
    _name = "upobebe.categoria"
    _description = "Categorias de productos"

    name = fields.Char(string="Nombre", required=True, help="Nombre de la categoria")
    descripcion = fields.Text(string="Descripcion", required=True, help="Descripcion de la categoria")
    
    producto_ids = fields.One2many("upobebe.producto", 'categoria_id', 'Productos')

    _sql_constraints = [('categoria_name_unique', 'UNIQUE (name)', 'El nombre debe ser único')]
    
    @api.constrains('name')
    def _check_name(self):
        if len(self.name) > 50:
            raise models.ValidationError("El nombre no debe tener mas de 50 caracteres")


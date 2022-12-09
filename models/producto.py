# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Producto
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    09/12/2022

from odoo import models, fields, api

class Producto(models.Model):
    _name = "upobebe.producto"
    _description = "Productos de UPOBEBE"

    name = fields.Char(string="Nombre del Producto", required=True, help="Nombre del producto")
    stock = fields.Integer(string="Stock", required=True, help="Stock del producto")
    descripcion = fields.Char(string="Descripcion", required=True, help="Descripcion del producto")

    categoria_id = fields.Many2one("upobebe.categoria", required=True, string="Categoria")
    articulos = fields.One2many("upobebe.articulo", 'producto_id', 'Articulos')

    _sql_constraints = [('producto_name_unique', 'UNIQUE (name)', 'El nombre debe ser único')]

    @api.constrains('name')
    def _check_name(self):
        if len(self.name) > 50:
            raise models.ValidationError("El nombre no debe tener mas de 50 caracteres")

    @api.constrains('stock')
    def _check_stock(self):
        if self.stock < 0:
            raise models.ValidationError("El stock no puede ser negativo")
    
    @api.constrains('descripcion')
    def _check_descripcion(self):
        if len(self.descripcion) > 200:
            raise models.ValidationError("La descripcion no debe tener mas de 200 caracteres")
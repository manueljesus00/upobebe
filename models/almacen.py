# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Almacen
# Editor:       Manuel Jesus Flores Montaño (@manueljesus00)
# Fecha rev:    08/12/2022

from odoo import models, fields, api


class almacen(models.Model):
    _name = 'upobebe.almacen'
    _description = 'upobebe.almacen'

    num_almacen = fields.Integer(required=True, index=True, string="Numero de almacen")
    ubicacion = fields.Char(required=True, string="Ubicacion")
    capacidad = fields.Integer(required=True, string="Capacidad")

    articulos_ids = fields.One2many("upobebe.articulo", 'num_Almacen', 'Articulos')

    _sql_constraints = [('almacen_num_almacen_unique', 'INIQUE (num_almacen)', 'El numero de almacen debe ser unico')]
    
    @api.constrains("capacidad")
    def _check_capacidad(self):
        if self.capacidad < 0:
            raise models.ValidationError("La capacidad debe ser un valor positivo")
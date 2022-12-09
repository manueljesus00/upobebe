# -*- coding: utf-8 -*-

# Version:      0.2.2
# Modelo:       Suscripcion
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class Suscripcion(models.Model):
    _name = "upobebe.suscripcion"
    _description = "Suscripciones de clientes"

    name = fields.Char(string="Nombre", required=True, help="Nombre del suscripcion")
    descuento = fields.Float(string="Descuento", required=True, help="Porcentaje de descuento por la suscripcion")
    
    cliente_ids = fields.One2many("upobebe.cliente", 'suscripciones_ids', 'Clientes')


    _sql_constraints = [('suscripcion_name_unique', 'UNIQUE (name)', 'El nombre debe ser único')]

    @api.constrains('descuento')
    def _check_descuento(self):
        if self.descuento < 0.0 or self.descuento > 1.0:
            raise models.ValidationError("El descuento debe ser un valor entre 0 y 1")
    
   

# -*- coding: utf-8 -*-

# Version:      0.3.0
# Modelo:       Suscripcion
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    28/12/2022

from odoo import models, fields, api


class Suscripcion(models.Model):
    _name = "upobebe.suscripcion"
    _description = "Suscripciones de clientes"

    name = fields.Char(string="Nombre", required=True, help="Nombre del suscripcion")
    descuento = fields.Float(string="Descuento", required=True, size=4, help="Porcentaje de descuento por la suscripcion")
    cantidad = fields.Integer(compute='_cantidadTotal', string="Cantidad de clientes", help="Cantidad de clientes que tienen la suscripcion")
    
    cliente_ids = fields.One2many("upobebe.cliente", 'suscripciones_ids', 'Clientes')


    _sql_constraints = [('suscripcion_name_unique', 'UNIQUE (name)', 'El nombre debe ser único')]

    @api.constrains('descuento')
    def _check_descuento(self):
        if self.descuento < 0.0 or self.descuento > 1.0:
            raise models.ValidationError("El descuento debe ser un valor entre 0 y 1")

    @api.depends('cliente_ids')
    def _cantidadTotal(self):
        for record in self:
            record.cantidad = len(record.cliente_ids)

    def btn_desapuntarClientes(self):
        self.write({'cliente_ids': [(5,)]})


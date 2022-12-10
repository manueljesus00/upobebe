# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Cliente
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    10/12/2022

from odoo import models, fields, api

class Financiacion(models.Model):
    _name = 'upobebe.financiacion'
    _description = 'Financiacion'

    name = fields.Integer(string="Id_Financiacion", required=True, readonly=True, copy=True, index=True)
    plazos = fields.Integer(string="Plazos", required=True)
    porcetaje = fields.Float(string="Porcentaje", required=True)

    id_transaccion = fields.Many2one("upobebe.transaccion", string="Id_Transaccion", required=True)

    @api.constrains("plazos")
    def _check_plazos(self):
        if self.plazos < 0:
            raise models.ValidationError("El numero de plazos no puede ser negativo")

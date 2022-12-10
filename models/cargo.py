# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Cargo
# Editor:       Manuel Jesus Flores Montano (@manueljesus00)
# Fecha rev:    28/11/2022

from odoo import models, fields, api
class cargo(models.Model):
    _name = 'upobebe.cargo'
    _description = 'upobebe.cargo'

    name = fields.Char("Cargo del empleado",required=True)
    # Se modifica idCargo por name para comprobar si asi se ven los valores normalmente
    
    transacciones = fields.One2many("upobebe.empleados", 'tipoCargo', 'Cargo')

    _sql_constraints = [('cargo_name_unique', 'UNIQUE (name)', 'El identificador del cargo debe ser unico')]
# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Cargo
# Editor:       Manuel Jesus Flores Montano (@manueljesus00)
# Fecha rev:    28/11/2022

from odoo import models, fields, api
class cargo(models.Model):
    _name = 'upobebe.cargo'
    _description = 'upobebe.cargo'

    idCargo =  fields.Char("Cargo del empleado",required=True)

    _sql_constraints = [('idCargo_unique', 'unique(idCargo)', 'El identificador del cargo debe ser unico')]
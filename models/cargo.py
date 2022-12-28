# -*- coding: utf-8 -*-

# Version:      0.2.0
# Modelo:       Cargo
# Editor:       Manuel Jesus Flores Montano (@manueljesus00) && Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    28/12/2022

from odoo import models, fields
class cargo(models.Model):
    _name = 'upobebe.cargo'
    _description = 'upobebe.cargo'

    id_cargo = fields.Char("Cargo del empleado",required=True)
    
    empleados_ids = fields.One2many("upobebe.empleados", 'tipoCargo', 'Cargo')
    
    # Se modifica idCargo por name para comprobar si asi se ven los valores normalmente
    _rec_name = 'id_cargo'
    _sql_constraints = [('cargo_name_unique', 'UNIQUE (name)', 'El identificador del cargo debe ser unico')]

    def btn_desapuntarEmpleados(self):
          self.write({'empleados_ids':[(5,)]})
# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       EMPLEADO
# Editor:       Manuel Jesus Flores Montano (@manueljesus00)
# Fecha rev:    24/11/2022
from odoo import models, fields, api

class empleado(models.Model):
    _name = 'upobebe.empleados'
    _description = 'Clase empleados para el proyecto UPOBebe'

    dniEmpleado = fields.Char("DNI del empleado", size=9, required=True)
    tipoCargo = fields.Many2One(upobebe.cargo, string="Cargo del empleado", required=True)
    nombre = fields.Char("Nombre del empleado", size=60, required=True)
    apellidos = fields.Char("Apellidos del empleado", size=90, required=True)
    correo = fields.Char("Correo de contacto")
    fechaNacimiento = fields.Date("Fecha de nacimiento")
    fechaAlta = fields.Date("Fecha de alta")

# -*- coding: utf-8 -*-

# Version:      0.2.0
# Modelo:       EMPLEADO
# Editor:       Manuel Jesus Flores Montano (@manueljesus00)
# Fecha rev:    30/11/2022
from odoo import models, fields, api

class Empleados(models.Model):
    _name = 'upobebe.empleados'
    _description = 'Clase empleados para el proyecto UPOBebe'

    dniEmpleado = fields.Char("DNI del empleado", size=9, required=True, help="DNI del empleado")
    tipoCargo = fields.Many2one('upobebe.cargo', string="Cargo del empleado", required=True, help="Tipo de cargo")
    nombre = fields.Char("Nombre del empleado", size=60, required=True, help="Nombre del empleado")
    apellidos = fields.Char("Apellidos del empleado", size=90, required=True, help=" Apellidos del empleado")
    correo = fields.Char("Correo de contacto")
    fechaNacimiento = fields.Date("Fecha de nacimiento")
    fechaAlta = fields.Date("Fecha de alta")

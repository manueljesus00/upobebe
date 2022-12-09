# -*- coding: utf-8 -*-

# Version:      0.2.0
# Modelo:       EMPLEADO
# Editor:       Manuel Jesus Flores Montano (@manueljesus00)
# Fecha rev:    30/11/2022
from odoo import models, fields, api

class Empleados(models.Model):
    _name = 'upobebe.empleados'
    _description = 'Clase empleados para el proyecto UPOBebe'

    dni_empleado = fields.Char("DNI del empleado", size=9, required=True, help="DNI del empleado")
    nombre = fields.Char("Nombre del empleado", size=60, required=True, help="Nombre del empleado")
    apellidos = fields.Char("Apellidos del empleado", size=90, required=True, help=" Apellidos del empleado")
    correo = fields.Char("Correo de contacto")
    fechaNacimiento = fields.Date("Fecha de nacimiento")
    fechaAlta = fields.Date("Fecha de alta", required=True)
    
    transacciones = fields.One2many("upobebe.empleados", 'dni_empleado', 'Empleados')

    tipoCargo = fields.Many2one("upobebe.cargo", string="Cargo")

    #Aquí podriamos meter un voton que te pusiese la fecha de hoy para el Alta
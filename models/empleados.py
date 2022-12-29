# -*- coding: utf-8 -*-

# Version:      0.3.0
# Modelo:       EMPLEADO
# Editor:       Manuel Jesus Flores Montano (@manueljesus00) && Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    29/12/2022

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
    tipoCargo = fields.Many2one("upobebe.cargo", string="Cargo", required=True)

    _rec_name = 'dni_empleado'

    #Aquí podriamos meter un voton que te pusiese la fecha de hoy para el Alta

    def btn_onchange_fechaAlta_actual(self):
        self.fechaAlta = fields.Date.today()
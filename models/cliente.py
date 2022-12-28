# -*- coding: utf-8 -*-

# Version:      0.2.1
# Modelo:       Cliente
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    06/12/2022

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'upobebe.cliente'
    _description = 'Clientes de UPOBEBE'

    dni_cliente = fields.Char(string="DNI", size=9, required=True, help="DNI del cliente")
    name = fields.Char(string="Nombre", required=True, help="Nombre del cliente")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del cliente")
    correo = fields.Char(string="Correo", required=False, help="Correo del cliente")
    domicilio = fields.Char(string="Domicilio", required=False, help="Domicilio del cliente")
    fechaNacimiento = fields.Datetime("Fecha de nacimiento", autodate=True, help="Fecha de nacimiento del cliente")

    suscripciones_ids = fields.Many2one("upobebe.suscripcion", required=False, string="Suscripcion")
    idTransaccion = fields.Many2many("upobebe.transaccion", required=False, string="Transaccion")

    
    _sql_constraints = [('cliente_dni_cliente_unique','UNIQUE (dni_cliente)','El dni debe ser único')]

    def btn_generate_report(self):
        return self.env.ref('upobebe.cliente_report').report_action(self)
   
    @api.constrains('name')
    def _check_nombre(self):
        if len(self.name) > 60:
           raise models.ValidationError("La longitud de la cadena no puede ser superior a 60 caracteres")
    
    @api.constrains('apellidos')
    def _check_nombre(self):
        if len(self.apellidos) > 60:
            raise models.ValidationError(
                "La longitud de la cadena no puede ser superior a 60 caracteres")
    
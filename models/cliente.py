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
    name = fields.Char(string="Nombre", size=60, required=True, help="Nombre del cliente")
    apellidos = fields.Char(string="Apellidos", size=60, required=True, help="Apellidos del cliente")
    correo = fields.Char(string="Correo", required=False, help="Correo del cliente")
    domicilio = fields.Char(string="Domicilio", required=False, help="Domicilio del cliente")
    fechaNacimiento = fields.Datetime("Fecha de nacimiento", autodate=True, help="Fecha de nacimiento del cliente")

    suscripciones_ids = fields.Many2one("upobebe.suscripcion", required=False, string="Suscripcion")
    idTransaccion = fields.Many2many("upobebe.transaccion", required=False, string="Transaccion")

    
    _rec_name = 'dni_cliente'
    _sql_constraints = [('cliente_dni_cliente_unique','UNIQUE (dni_cliente)','El dni debe ser único')]

    def btn_generate_report(self):
        reporte = self.env['ir.actions.report'].search([('report_name', '=', 'upobebe.cliente_report')], limit=1)
        if reporte:
            return reporte.report_action(self)
        else:
            raise models.ValidationError('No se ha encontrado el reporte "upobebe.cliente_report".')


    @api.constrains('name')
    def _check_nombre(self):
        if len(self.name) > 60:
           raise models.ValidationError("La longitud de la cadena no puede ser superior a 60 caracteres")
    
    @api.constrains('apellidos')
    def _check_nombre(self):
        if len(self.apellidos) > 60:
            raise models.ValidationError(
                "La longitud de la cadena no puede ser superior a 60 caracteres")

    @api.constrains('fechaNacimiento')
    def _check_fechaNacimiento(self):
        if self.fechaNacimiento > fields.Datetime.now():
            raise models.ValidationError("La fecha de nacimiento no puede ser superior a la fecha actual")
    
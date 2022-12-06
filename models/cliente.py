# -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Cliente
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    23/11/2022

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'upobebe.cliente'
    _description = 'Clientes de UPOBEBE'

    dniCliente = fields.Char(string="DNI", required=True, help="DNI del cliente")
    name = fields.Char(string="Nombre", required=True, help="Nombre del cliente")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del cliente")
    correo = fields.Char(string="Correo", required=False, help="Correo del cliente")
    domicilio = fields.Char(string="Domicilio", required=False, help="Domicilio del cliente")
    fechaNacimiento = fields.Datetime("Fecha de nacimiento", autodate=True, help="Fecha de nacimiento del cliente")

    # La he intentado implementar pero me sale "No se encontró ningún campo inverso None para 'upobebe.cliente'"
    # suscripciones_ids = fields.Many2one("upobebe.suscripcion",required=False,string="Suscripcion")
    # Este de abajo no se si es asi
    #idTransaccion = fields.Meny2one("upobebe.transaccion",required=False,string="Transaccion")


    #_sql_constraints = [('dniClientes_name_unique','unique (dniCliente)','El dni debe ser único')]
    

   
    @api.constrains("name")
    def _check_nombre(self):
        if len(self.name) > 60:
           raise models.ValidationError("La longitud de la cadena no puede ser superior a 60 caracteres")
    
    @api.constrains("apellidos")
    def _check_nombre(self):
        if len(self.apellidos) > 60:
            raise models.ValidationError(
                "La longitud de la cadena no puede ser superior a 60 caracteres")
    
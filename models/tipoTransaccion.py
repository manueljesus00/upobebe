 # -*- coding: utf-8 -*-

# Version:      0.1.0
# Modelo:       Suscripcion
# Editor:       Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    24/11/2022

# Odoo me da un error diciendo que __name = tipoTransaccion no es valido y no he sido capaz de eliminar el error

from odoo import models, fields

class tipoTransaccion(models.Model):
    _name = "upobebe.tipoTransaccion"
    _description = "Tipos de transacciones"

    name = fields.Char(string="Tipo Transaccion", required=True, help="Nombre del tipo de transaccion")
    #transacciones = fields.One2meny("upobebe.transaccion",required=False,string="Transacciones")

    _sql_constraints = [("suscripcion_name_unique", "UNIQUE (name)", "El nombre debe ser único")]

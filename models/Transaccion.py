# -*- coding: utf-8 -*-

# Version:      0.2.0
# Modelo:       Transaccion
# Editor:       Manuel Jesus Flores Montano (@manueljesus00) && Pedro Jesus Lazaro Diaz (@vitalsum)
# Fecha rev:    28/12/2022


# from odoo import models, fields, api

from odoo import models, fields, api
class Transaccion(models.Model):
    _name = 'upobebe.transaccion'
    _description = 'Transaccion en UPOBebe'


    # Mirar que funcione asi para un autoincremental, sino se hace computando el id
    idTransaccion =  fields.Integer("ID. de la transaccion",required=True,store=True, default=lambda self: self.get_next_id())
    estado = fields.Selection([('pendiente', 'Pendiente'),
                               ('en_curso', 'En curso'),
                               ('finalizada', 'Finalizada'), ],
                                'Estado', default='pendiente')    
    tipotransaccion_id = fields.Many2one("upobebe.tipotransaccion", required=True, string="Tipo de transaccion")
    dniEmpleado = fields.Many2one("upobebe.empleados",string="Empleado",required=True)
    id_financiacion = fields.Many2many("upobebe.financiacion", string="Financiacion", required=True)
    #idSeguimiento = fields.Integer(string="Numero de seguimiento") #Tienen que ser relaciones
    #idArticulo = fields.One2many("upobebe.articulo","field_articulos",string="Articulos", required=True)
    #idProveedor = fields.Many2one("upobebe.proveedor",string="Proveedor")
    #dniCliente = fields.Many2one("upobebe.cliente", string="Cliente", size=9)
    fechaTransaccion = fields.Datetime('Fecha de compra',required=True, autodate=True)
    
    _rec_name = 'idTransaccion'
    _sql_constraints = [('transaccion_idTransaccion_unique','UNIQUE (idTransaccion)','El id de la transaccion debe ser único')]

    def btn_submit_to_pendiente(self):
        if self.estado != 'finalizada':
            self.write({'estado': 'pendiente'})
        else:
            raise models.ValidationError('Una transaccion finalizada no puede volver a estar pendiente')
    
    def btn_submit_to_en_curso(self):
        if self.estado != 'finalizada':
            self.write({'estado': 'en_curso'})
        else:
            raise models.ValidationError('Una transaccion finalizada no puede volver a estar en curso')
    
    def btn_submit_to_finalizada(self):
        self.write({'estado': 'finalizada'})
                
    
    # Funcion para sacar el ultimo id de transaccion y emplearlo
    def get_next_id(self):
        last_id = self.search([], order='idTransaccion desc', limit=1).idTransaccion
        if not last_id:
            return 1
        else:
            return last_id + 1

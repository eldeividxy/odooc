from odoo import models, fields, api

class transaccion_ext(models.Model):
    _inherit = 'transacciones.transaccion'

    compra_id = fields.Many2one(
        'compras.compra',
        string = "Compra"
    )

    @api.depends('compra_id')
    def _define_tipo(self):
        self.tipo = 0 #Se establece el tipo de transaccion 0 = Compra

    @api.onchange('producto_id')
    def _mod_producto(self):
        for i in self:
            if i.producto_id:
                i.iva = i.producto_id.iva
                i.ieps = i.producto_id.ieps
                if i.tipo == 1:
                    i.precio = i.producto_id.costo
                elif i.tipo == 0:
                    i.precio = i.producto_id.contado



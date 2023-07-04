from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    client_phone = fields.Char(string='Teléfono')
    client_email = fields.Char(string='Email')
    client_address = fields.Char(string='Dirección')
    client_city = fields.Char(string='Ciudad')

    def update_partner(self):
        for order in self:
            # Verificar si hay un socio comercial seleccionado
            if order.partner_id:
                order.partner_id.write({
                    'phone': order.client_phone,
                    'email': order.client_email,
                    'street': order.client_address,
                    'city': order.client_city,
                })

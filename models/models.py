from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    client_phone = fields.Char(string='Teléfono')
    client_email = fields.Char(string='Email')
    client_address = fields.Char(string='Dirección')
    client_city = fields.Char(string='Ciudad')
    client_province = fields.Many2one('res.country.state', string='Provincia', domain=lambda self: self._get_province_domain())

    def _get_province_domain(self):
        arg_country = self.env['res.country'].search([('name', '=', 'Argentina')], limit=1)
        if arg_country:
            return [('country_id', '=', arg_country.id)]
        return []

    def update_partner(self):
        for order in self:
            # Verificar si hay un socio comercial seleccionado
            if order.partner_id:
                order.partner_id.write({
                    'mobile': order.client_phone,
                    'email': order.client_email,
                    'street': order.client_address,
                    'city': order.client_city,
                    'state_id': order.client_province,
                    'property_product_pricelist': order.pricelist_id;
                })
    
    @api.onchange('client_province')
    def _onchange_client_province(self):
        if self.client_province:
            pricelist = self.env['product.pricelist'].search([('state_ids', 'in', self.client_province.id)], limit=1)
            if pricelist:
                self.pricelist_id = pricelist.id
            else:
                self.pricelist_id = False

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    state_ids = fields.Many2many('res.country.state', string='Provincias', domain=lambda self: self._get_state_domain())

    def _get_state_domain(self):
        arg_country = self.env['res.country'].search([('name', '=', 'Argentina')], limit=1)
        if arg_country:
            return [('country_id', '=', arg_country.id)]
        return []

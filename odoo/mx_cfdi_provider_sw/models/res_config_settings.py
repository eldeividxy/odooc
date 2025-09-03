from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mx_cfdi_sw_sandbox = fields.Boolean(string='SW Sandbox', default=True, config_parameter='mx_cfdi_sw.sandbox')
    mx_cfdi_sw_base_url = fields.Char(string='SW Base URL', config_parameter='mx_cfdi_sw.base_url')
    mx_cfdi_sw_token = fields.Char(string='SW Token', config_parameter='mx_cfdi_sw.token')
    mx_cfdi_sw_user = fields.Char(string='SW User', config_parameter='mx_cfdi_sw.user')
    mx_cfdi_sw_password = fields.Char(string='SW Password', config_parameter='mx_cfdi_sw.password')

    mx_cfdi_sw_rfc = fields.Char(string='RFC Emisor', config_parameter='mx_cfdi_sw.rfc')
    # ► Cambiados a Text
    mx_cfdi_sw_cer_pem = fields.Text(string='CSD Cert (PEM, pegado como texto)', config_parameter='mx_cfdi_sw.cer_pem')
    mx_cfdi_sw_key_pem = fields.Text(string='CSD Key (PEM, pegado como texto)', config_parameter='mx_cfdi_sw.key_pem')
    mx_cfdi_sw_key_password = fields.Char(string='CSD Key Password', config_parameter='mx_cfdi_sw.key_password')

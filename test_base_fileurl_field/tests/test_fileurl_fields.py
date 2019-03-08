# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
import base64

from odoo.tests import TransactionCase
from odoo.modules.module import get_module_resource


class TestFileUrlFields(TransactionCase):

    def test_fileurl_fields(self):
        file_path = get_module_resource('test_base_fileurl_field', 'data',
                                        'sample.txt')
        image_path = get_module_resource('test_base_fileurl_field', 'data',
                                         'pattern.png')
        partner = self.env.ref('base.main_partner')
        partner.write({
            'url_file': base64.b64encode(open(file_path, 'rb').read()),
            'url_file_fname': 'sample.txt',
            'url_image': base64.b64encode(open(image_path, 'rb').read()),
            'url_image_fname': 'pattern.png',
        })

        attachments = self.env['ir.attachment'].search([
            ('res_model', '=', partner._name),
            ('res_id', '=', partner.id),
        ])

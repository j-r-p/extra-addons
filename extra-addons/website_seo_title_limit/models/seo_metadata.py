# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class WebsiteSeoMetadata(models.AbstractModel):
    """Universal override for SEO metadata fields.

    The standard `website.seo.metadata` mixin defines `website_meta_title`
    with the default length of 60 or so.  This custom module overrides that
    field on the abstract model, increasing the `size` to 160 characters.

    Because the field is defined on the mixin, every concrete model that
    inherits from `website.seo.metadata` (product.template, product
    public category, website.page, blog.post, etc.) automatically picks up
    the new size when the module is installed and upgraded.
    """
    _inherit = 'website.seo.metadata'

    website_meta_title = fields.Char(
        string='SEO Meta Title',
        size=160,
        help='SEO title shown on the website. Limited to 160 characters.',
    )

    @api.constrains('website_meta_title')
    def _check_meta_title_length(self):
        for record in self:
            if record.website_meta_title and len(record.website_meta_title) > 160:
                raise ValidationError(
                    _('SEO Meta Title cannot exceed 160 characters (current length: %d)')
                    % len(record.website_meta_title)
                )

    @api.onchange('website_meta_title')
    def _onchange_meta_title(self):
        if self.website_meta_title and len(self.website_meta_title) > 160:
            # trim the value and warn the user in the form
            self.website_meta_title = self.website_meta_title[:160]
            return {
                'warning': {
                    'title': _('Maximum length reached'),
                    'message': _('SEO Meta Title has been truncated to 160 characters.'),
                }
            }

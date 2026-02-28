# -*- coding: utf-8 -*-
from odoo import fields, models


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

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_inline_comment.models import InlineComment


class InlineCommentPlugin(CMSPluginBase):
    model = InlineComment
    name = _("Inline comment")
    render_template = "djangocms_inline_comment/inline_comment.html"
    allow_children = True


plugin_pool.register_plugin(InlineCommentPlugin)

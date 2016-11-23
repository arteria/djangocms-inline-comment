from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


def _get_html_field_class():
    """
    Make the HTMLField used by InlineComment.body configurable.
    Default: djangocms_text_ckeditor.fields.HTMLField
    """
    if hasattr(settings, 'DJANGOCMS_INLINE_COMMENT_HTML_FIELD'):
        from django.utils.module_loading import import_string
        HTMLField = import_string(settings.DJANGOCMS_INLINE_COMMENT_HTML_FIELD)
    else:
        from djangocms_text_ckeditor.fields import HTMLField
    return HTMLField


class InlineComment(CMSPlugin):
    body = _get_html_field_class()(_("Comment"), null=True, blank=True)

    def get_short_description(self):
        if not self.body:
            return _("Inline Comment")
        return mark_safe(self.body)

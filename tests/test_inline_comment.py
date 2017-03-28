# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase

from cms import api as cms_api
from djangocms_helper.base_test import BaseTestCase
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from djangocms_inline_comment.cms_plugins import InlineCommentPlugin
from djangocms_inline_comment.models import InlineComment


class ModelTestCase(TestCase):

    def setUp(self):
        self.inline_comment = InlineComment.objects.create(
            body='<p>This is a comment</p>'
        )

    def test_inline_comment_instance(self):
        inline_comment = InlineComment.objects.first()
        self.assertEqual(inline_comment.body, '<p>This is a comment</p>')

    def test_short_description(self):
        self.assertEqual(self.inline_comment.get_short_description(), '<p>This is a comment</p>')


class PluginTestCase(BaseTestCase):

    _pages_data = (
        {
            'en': {
                'title': 'Inline Comments test',
                'template': 'page.html',
                'publish': True,
            }
        },
    )

    def setUp(self):
        self.page = self.get_pages()[0]
        self.language = 'en'
        self.user = User.objects.first()
        self.placeholder = self.page.placeholders.get(slot='content')
        self.text_plugin = cms_api.add_plugin(self.placeholder, TextPlugin, self.language, body='<p>Public text</p>')
        self.inline_comment_plugin = cms_api.add_plugin(self.placeholder, InlineCommentPlugin, self.language, body='<p>This is a comment</p>')
        cms_api.publish_page(self.page, self.user, self.language)

    def test_public_page(self):
        """
        Text plugin should be publicly visible, inline comment not
        """
        response = self.client.get(self.page.get_absolute_url())
        self.assertContains(response, '<p>Public text</p>')
        self.assertNotContains(response, '<p>This is a comment</p>')
        self.assertNotContains(response, 'opacity: 0.7')

    def test_edit_mode(self):
        """
        Both text plugin and inline comment should be visible to editor
        """
        with self.login_user_context(self.user):
            response = self.client.get(self.page.get_absolute_url(), data={'edit': True})
        self.assertContains(response, '<p>Public text</p>')
        self.assertContains(response, '<p>This is a comment</p>')
        self.assertContains(response, 'opacity: 0.7')

    def test_commenting_out(self):
        """
        Text plugin should be publicly invisible after moving below inline comment
        """
        # Before
        hidden_plugin = cms_api.add_plugin(self.placeholder, TextPlugin, self.language, body='<p>Hide me!</p>')
        cms_api.publish_page(self.page, self.user, self.language)
        response = self.client.get(self.page.get_absolute_url())
        self.assertContains(response, '<p>Hide me!</p>')

        # After
        hidden_plugin.delete()
        hidden_plugin = cms_api.add_plugin(self.placeholder, TextPlugin, self.language, body='<p>Hide me!</p>',
                                           target=self.inline_comment_plugin)
        cms_api.publish_page(self.page, self.user, self.language)
        response = self.client.get(self.page.get_absolute_url())
        self.assertNotContains(response, '<p>Hide me!</p>')

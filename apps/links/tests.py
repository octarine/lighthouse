from django.core.urlresolvers import reverse
from .models import Link

from django_webtest import WebTest

import pdb


class LinkTest(WebTest):
    def test_create_link(self):
        form = self.app.get(reverse('link-create')).form

        self.assertEquals(form['name'].value, '')
        self.assertEquals(form['description'].value,
                          '')
        self.assertEquals(form['destination'].value, '')

        form['name'] = 'Google'
        form['destination'] = 'https://google.com'
        response = form.submit().follow()
        response.mustcontain('<h1>Google</h1>')

    def test_edit_link_render(self):
        existing_link = Link(
            name='Wikimapia',
            description='A great mapping application',
            destination='https://wikimapia.org')
        existing_link.save()

        form = self.app.get(
            reverse('link-edit', kwargs={'pk': existing_link.pk})).form

        # pdb.set_trace()

        self.assertEquals(form['name'].value, 'Wikimapia')
        self.assertEquals(form['description'].value,
                          'A great mapping application')
        self.assertEquals(form['destination'].value, 'https://wikimapia.org')

    def test_edit_link_submit(self):
        existing_link = Link(
            name='Wikimapia',
            description='A great mapping application',
            destination='https://wikimapia.org')
        existing_link.save()

        form = self.app.get(
            reverse('link-edit', kwargs={'pk': existing_link.pk})).form

        form['name'].value = 'Bing Maps'
        form['description'].value = 'Another great mapping application'
        form['destination'].value = 'https://maps.bing.com'

        response = form.submit().follow()

        self.assertIn('Bing Maps', response)
        self.assertNotIn('Wikimapia', response)
        self.assertIn('Another great mapping application', response)
        self.assertNotIn('A great mapping application', response)
        self.assertIn('https://maps.bing.com', response)
        self.assertNotIn('https://wikimapia.org', response)

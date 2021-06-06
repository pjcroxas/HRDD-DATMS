from django.urls import reverse, resolve
from django.test import TestCase
from .views import request_site
from .models import Requestor


class HomeTests(TestCase):
    def setUp(self):
        self.request = Requestor.objects.create(name='request-details', description='Request Details.')
        url = reverse('request_page')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('request_page')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, request_site)

    def test_home_view_contains_link_to_topics_page(self):
        request_details_url = reverse('request_details', kwargs={'pk':self.request.pk})
        self.assertContains(self.response, 'href="{0}"'.format(request_details_url))

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/request/1/new_scholarship/')
        self.assertEquals(view.func, scholarship_app)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_scho_app_url = reverse('scholarship_application', kwargs={'pk': 1})
        request_detail_url = reverse('request_detail', kwargs={'pk': 1})
        response = self.client.get(new_scho_app_url)
        self.assertContains(response, 'href="{0}"'.format(request_detail_url))

class RequestDetailsTests(TestCase):
    def setUp(self):
        Requestor.objects.create(name='request-details', description='Request Details.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('request_details', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('request_details', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/request_details/1/')
        self.assertEquals(view.func, board_topics)

from menu.models import Dish, Order, Table
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
import json


class TestMenuView(TestCase):
    """
    Test the simplified menu views.
    """
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = APIClient()

    def test_index_dynamic_model_retrieval(self):
        """
        Test the dynamic retrieval of items from the database.
        """

        DISH_RETRIEVAL_URL = reverse('index', args=["dish", ])
        TABLE_RETRIEVAL_URL = reverse('index', args=["table", ])
        ORDER_RETRIEVAL_URL = reverse('index', args=["order", ])

        response = self.client.get(DISH_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(TABLE_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(ORDER_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 200)

    def text_index_non_existing_model(self):
        """
        Test the dynamic retrieval of a model that does not exist.
        """
        FALSE_RETRIEVAL_URL = reverse('index', args="ingredients",)
        response = self.client.get(FALSE_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 404)

    def test_detail_dynamic_instance_retrieval(self):
        """
        Test the dynamic retrieval of a single instance of a model.
        """
        DISH_RETRIEVAL_URL = reverse('detail', args=["dish", 1])
        TABLE_RETRIEVAL_URL = reverse('detail', args=["table", 2])
        ORDER_RETRIEVAL_URL = reverse('detail', args=["order", 3])

        response = self.client.get(DISH_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(TABLE_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(ORDER_RETRIEVAL_URL)
        self.assertEqual(response.status_code, 200)

    def test_missing_instance(self):
        """
        Test that the the returning response for a non existing instance is
        correct.
        """
        DISH_RETRIEVAL_URL = reverse('detail', args=["dish", 1000])
        response = self.client.get(DISH_RETRIEVAL_URL)
        self.assertEqual(json.loads(response.content.decode())['item'], [])

    def test_filtering_endpoint(self):
        """
        Test that the filter is applied correctly to the retrieval of model
        instances.
        """
        DISH_FILTERD_URL = reverse(
            'filtered', kwargs={'model_name': 'dish'}
        )

        filters = {
            'id': 1,
            'name': 'Chicken soup',
        }

        response = self.client.get(DISH_FILTERD_URL, data=filters)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode())
                         ['items'][0]['name'], 'Chicken soup')

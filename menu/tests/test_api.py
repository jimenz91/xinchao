from menu.models import Order, Table
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

ORDER_LIST_URL = reverse('order-list')
ORDER_DETAIL_URL = reverse('order-detail', args=[1, ])

TABLE_LIST_URL = reverse('table-list')
TABLE_DETAIL_URL = reverse('table-detail', args=[2, ])

DISH_LIST_URL = reverse('dish-list')
DISH_DETAIL_URL = reverse('dish-detail', args=[1, ])


class TestOrdersAPI(TestCase):
    """
    Test the Orders API.
    """
    fixtures = ['fixtures.json', ]

    def setUp(self):
        self.client = APIClient()

    def test_create_order_successful(self):
        """
        Tests the creation of an order.
        """
        payload = {
            'diners': 2,
            'table_id': 1
        }
        response = self.client.post(ORDER_LIST_URL, payload, format='json')

        exists = Order.objects.filter(
            id=response.data['id']
        ).exists()
        self.assertTrue(exists)
        self.assertEqual(response.status_code, 201)

    def test_orders_retrieval(self):
        response = self.client.get(ORDER_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_single_order_retrieval(self):
        response = self.client.get(ORDER_DETAIL_URL)
        self.assertEqual(response.status_code, 200)

    def test_single_order_retrival_missing_item(self):
        MISSING_ORDER_DETAIL_URL = reverse('order-detail', args=[30, ])
        response = self.client.get(MISSING_ORDER_DETAIL_URL)
        self.assertEqual(response.status_code, 404)

    def test_delete_order(self):
        response = self.client.delete(ORDER_DETAIL_URL)
        self.assertEqual(response.status_code, 204)


class TestTablesAPI(TestCase):
    """
    Test the Tables API.
    """
    fixtures = ['fixtures.json', ]

    def setUp(self):
        self.client = APIClient()
        Table.objects.create()

    def test_tables_retrieval(self):
        response = self.client.get(TABLE_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_table_creation(self):
        response = self.client.post(TABLE_LIST_URL, data={})
        self.assertEqual(response.status_code, 201)

    def test_single_table_retrieval(self):
        response = self.client.get(TABLE_DETAIL_URL)
        self.assertEqual(response.status_code, 200)

    def test_single_table_retrival_missing_item(self):
        MISSING_TABLE_DETAIL_URL = reverse('table-detail', args=[15, ])
        response = self.client.get(MISSING_TABLE_DETAIL_URL)
        self.assertEqual(response.status_code, 404)

    def test_delete_table(self):
        response = self.client.delete(TABLE_DETAIL_URL)
        self.assertEqual(response.status_code, 204)


class TestDishesAPI(TestCase):
    """
    Test the Dishes API.
    """
    fixtures = ['fixtures.json', ]

    def setUp(self):
        self.client = APIClient()

    def test_dishes_retrieval(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_dish_creation(self):
        payload = {
            "name": "Shrimp",
            "price": 10000.0,
            "rations_available": 3,
            "descripcion": "Great shrimp.",
            "weight": 200.0
        }
        response = self.client.post(DISH_LIST_URL, payload)
        self.assertEqual(response.status_code, 201)

    def test_single_dish_retrieval(self):
        response = self.client.get(DISH_DETAIL_URL)
        self.assertEqual(response.status_code, 200)

    def test_single_dish_retrival_missing_item(self):
        MISSING_DISH_DETAIL_URL = reverse('dish-detail', args=[10, ])
        response = self.client.get(MISSING_DISH_DETAIL_URL)
        self.assertEqual(response.status_code, 404)

    def test_delete_dish(self):
        response = self.client.delete(DISH_DETAIL_URL)
        self.assertEqual(response.status_code, 204)

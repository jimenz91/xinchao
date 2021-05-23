from django.test import TestCase
from menu.dish_distribution import DishDistribution
from django.test.client import RequestFactory
from rest_framework.test import APIClient
from menu.models import Dish


class TestDishDistrution(TestCase):
    """
    Test the dish distribution logic.
    """
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()

    def test_knapsack_algorithm(self):
        """
        Test knapsack algorithm
        """
        table_weight = 200
        weights = [100, 180, 300]
        prices = [20000.0, 40000.0, 50000.0]
        n = len(prices)
        self.factory.data = {
            'diners': 2,
            'table': 1
        }
        distribution = DishDistribution(self.factory)
        result = distribution.knapSack(
            table_weight, weights, prices, n)
        self.assertEqual(result, 40000.0)

    def test_distribute(self):
        self.factory.data = {
            'diners': 2,
            'table': 1
        }
        cost, dish_ids = DishDistribution(self.factory).distribute()
        self.assertEqual(cost, 40000.0)
        self.assertEqual(dish_ids, [3])

    def test_get_cost_and_ids_function(self):
        table_weight = 200
        weights = [100, 180, 300]
        available_dishes = Dish.objects.filter(
            rations_available__gt=0, weight__lte=table_weight).values(
        ).order_by('price')
        prices = [20000.0, 40000.0, 50000.0]
        n = len(prices)
        self.factory.data = {
            'diners': 2,
            'table': 1
        }
        distribution = DishDistribution(self.factory)
        result = distribution.knapSack(
            table_weight, weights, prices, n
        )

        dish_ids = DishDistribution(self.factory).get_cost_and_ids(
            result, prices, available_dishes)
        self.assertEqual(dish_ids, [3])

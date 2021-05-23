from typing import Union
from rest_framework.request import Request
from .models import Dish


class DishDistribution:
    """
    Service to distribute the available dishes depending on the number of
    diners and the benefit it would bring to the restaurant.
    """

    def __init__(self, request: Request) -> None:
        self.request = request
        self.diners = self.request.data['diners']
        self.table_weight = int(self.diners*100)

    def distribute(self) -> Union[float, list]:
        """
        Function distribute the available dishes according to the number of
        diners.

        Returns:
            float: the cost of the some of dishes.
            list: the list of ids of the dishes selected.
        """

        available_dishes = Dish.objects.filter(
            rations_available__gt=0, weight__lte=self.table_weight).values(
        ).order_by('price')

        prices = [dish['price'] for dish in available_dishes]
        weights = [weight['weight'] for weight in available_dishes]
        n_dishes = available_dishes.count()

        cost = self.knapSack(self.table_weight, weights, prices, n_dishes)

        return cost, self.get_cost_and_ids(cost, prices, available_dishes)

    def knapSack(
        self,
        table_weight: int,
        weights: list,
        prices: list,
        n_dishes: int
    ) -> float:
        """
        Brute force approach to KnapSack algorithm

        Args:
            table_weight (int): sum of the diners permitted weights
            weights (list): list of weights of the available unique dishes.
            prices (list): list of prices of the available unique dishes for
            n_dishes (int): number of available dishes

        Returns:
            float: the cost of the order.
        """
        if n_dishes == 0 or table_weight == 0:
            return 0
        if (weights[n_dishes-1] > table_weight):
            return self.knapSack(table_weight, weights, prices, n_dishes-1)
        else:
            return max(prices[n_dishes-1] + self.knapSack(
                table_weight-weights[n_dishes-1], weights, prices, n_dishes-1),
                self.knapSack(table_weight, weights, prices, n_dishes-1))

    def get_cost_and_ids(self, cost, prices, available_dishes) -> list:
        """
        Function for obtaining the ids from the cost calculated by the 
        knapSack.

        Args:
            cost ([type]): cost calculated.
            prices ([type]): available prices.
            available_dishes ([type]): available dishes.

        Returns:
            list: A list with all the ids from the cost calculated.
        """

        dishes_ids = []

        if cost in prices:
            dishes_ids.append(available_dishes.filter(price=cost)[0]['id'])
        else:
            for i in range(len(prices)):
                for j in range(i+1, len(prices)):
                    if prices[i] + prices[j] == cost:
                        dishes_ids.append(available_dishes.filter(
                            price=prices[i])[0]['id']
                        )
                        dishes_ids.append(available_dishes.filter(
                            price=prices[j])[0]['id']
                        )
        return dishes_ids

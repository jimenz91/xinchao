
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from menu.models import Dish, Order, Table
from menu.api.serializers import (
    DishSerializer,
    OrderSerializer,
    TableSerializer
)

from menu.dish_distribution import DishDistribution


class DishListCreateAPIView(APIView):
    """
    Dish APIView showing every dish created and with the post method to
    create more
    """

    def get(self, request: Request) -> Response:
        """
        GET method for Dish model.

        Args:
            request (Request): retrieval HttpRequest.

        Returns:
            Response: Http response with every dish created.
        """

        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        POST method for the Dish model.

        Args:
            request (Request): HttpRequest with the information for the new
            instance to create.

        Returns:
            Response: HttpResponse with the instance created.
        """
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishDetailAPIView(APIView):
    """
    Dish APIView that shows one specific instance of a Dish model. It contains
    the GET, PUT and DELETE methods.
    """

    def get(self, request: Request, pk: int) -> Response:
        """
        GET method to retrieve one instance.

        Args:
            request (Request): HttpRequest with the instance to retrieve.
            pk (int): identifier of the instance to retrieve

        Returns:
            [Response]: Http response with the item requested.
        """
        dish = get_object_or_404(Dish, pk=pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """
        PUT method to update an instance of the model.

        Args:
            request (Request): HttpRequest with the data to update.
            pk (int): identifier of the instance to update.

        Returns:
            Response: Response with the instance updated.
        """
        dish = get_object_or_404(Dish, pk=pk)
        serializer = DishSerializer(dish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """
        DELETE method to remove an instance of the model.

        Args:
            request (Request): Http Request with the instance to remove.
            pk (int): id of the instance to remove.

        Returns:
            Response: Http Response confirming the removal of the object.
        """
        dish = get_object_or_404(Dish, pk=pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderListCreateAPIView(APIView):

    def get(self, request: Request) -> Response:
        """
        GET method for the Order model.

        Args:
            request (Request): retrieval HttpRequest.

        Returns:
            Response: Http response with every order created.
        """
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        """
        POST method for the Table model. The Dish distribution method is
        used to override the data in the request in order to add the selected
        dishes. When the order is confirmed, the number of available dishes is
        reduced by the amount used in the order.

        Args:
            request (Request): HttpRequest with the information for the new
            instance to create.

        Returns:
            Response: HttpResponse with the instance created.
        """
        cost, dishes_id = DishDistribution(request).distribute()
        request.data['dishes'] = dishes_id
        request.data['cost'] = cost
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for id in dishes_id:
                dish = Dish.objects.filter(id=id).first()
                current_rations = dish.rations_available - 1
                dish.rations_available = current_rations
                dish.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    """
    Order APIView that shows one specific instance of an Order model. It
    contains the GET, PUT and DELETE methods.
    """

    def get(self, request: Request, pk: int) -> Response:
        """
        GET method to retrieve one instance.

        Args:
            request (Request): HttpRequest with the instance to retrieve.
            pk (int): identifier of the instance to retrieve

        Returns:
            [Response]: Http response with the item requested.
        """
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """
        PUT method to update an instance of the model.

        Args:
            request (Request): HttpRequest with the data to update.
            pk (int): identifier of the instance to update.

        Returns:
            Response: Response with the instance updated.
        """
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """
        DELETE method to remove an instance of the model.

        Args:
            request (Request): Http Request with the instance to remove.
            pk (int): id of the instance to remove.

        Returns:
            Response: Http Response confirming the removal of the object.
        """
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TableListCreateAPIView(APIView):

    def get(self, request: Request) -> Response:
        """
        GET method for the Table model.

        Args:
            request (Request): retrieval HttpRequest.

        Returns:
            Response: Http response with every table created.
        """
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        POST method for the Table model.

        Args:
            request (Request): HttpRequest with the information for the new
            instance to create.

        Returns:
            Response: HttpResponse with the instance created.
        """
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableDetailAPIView(APIView):
    """
    Table APIView that shows one specific instance of a Table model. It
    contains the GET, PUT and DELETE methods.
    """

    def get(self, request: Request, pk: int) -> Response:
        """
        GET method to retrieve one instance.

        Args:
            request (Request): HttpRequest with the instance to retrieve.
            pk (int): identifier of the instance to retrieve

        Returns:
            [Response]: Http response with the item requested.
        """
        table = get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        """
        PUT method to update an instance of the model.

        Args:
            request (Request): HttpRequest with the data to update.
            pk (int): identifier of the instance to update.

        Returns:
            Response: Response with the instance updated.
        """
        table = get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """
        DELETE method to remove an instance of the model.

        Args:
            request (Request): Http Request with the instance to remove.
            pk (int): id of the instance to remove.

        Returns:
            Response: Http Response confirming the removal of the object.
        """
        table = get_object_or_404(Table, pk=pk)
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

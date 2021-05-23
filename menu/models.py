from django.db import models


class Dish(models.Model):
    """
    Dishes to be served in the restaurant.
    """
    name = models.CharField(max_length=50)
    price = models.FloatField()
    weight = models.FloatField()
    rations_available = models.IntegerField()
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dishes'


class Table(models.Model):
    """
    Tables in the restaurant.
    """
    availability = models.BooleanField(default=True)

    def __str__(self):
        return "Table {}".format(self.id)


class Order(models.Model):
    """
    Orders made by tables.
    """
    diners = models.IntegerField()
    dishes = models.ManyToManyField(Dish)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    cost = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "Order #{}".format(self.id)

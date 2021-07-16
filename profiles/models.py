from django.db import models
from django.contrib.auth.models import AbstractUser
from menu.models import Order


class Client(AbstractUser):
    """
    Extended user class for further customization.
    """
    orders_made = models.ManyToManyField(Order, blank=True)

    def __str__(self):
        return ("{}, {}".format(self.last_name, self.first_name))

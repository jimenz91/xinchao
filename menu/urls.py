from django.urls import path
from . import views

urlpatterns = [
    path('<str:model_name>', views.index, name='index'),
    path('<str:model_name>/<int:id>', views.item_detail, name='detail'),
    path('<str:model_name>/filtered/', views.filtered, name='filtered'),
]

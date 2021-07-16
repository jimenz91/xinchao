
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from profiles.api.views import ClientCreateAPIView, HelloView


urlpatterns = [
    path('', ClientCreateAPIView.as_view(),
         name='create-user'),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
]

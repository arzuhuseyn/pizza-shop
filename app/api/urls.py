from django.urls import path, include

from . import views


orders = [
    path("", views.OrderListAPIView.as_view(), name="orders"),
    path('create/', views.CreateOrderAPIView.as_view(), name="create-order"),
    path("profile/create/", views.OrderProfileCreateAPIView.as_view(), name="create-profile"),
    path("order_profile/<int:pk>/", views.OrderProfileAPIView.as_view(), name="order-profile-api"),
    path("<int:pk>/", views.OrderAPIView.as_view()),
    path("<int:pk>/status/", views.UpdateOrderStatusAPIView.as_view()),
]


catalog = [
    path("items/", views.PizzaListAPIView.as_view(), name="items"),
    path("ingredients/", views.IngredientListAPIView.as_view(), name="ingredients")
]


urlpatterns = [
    path('orders/', include(orders)),
    path('catalog/', include(catalog))
]
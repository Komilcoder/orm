from django.urls import path
from .import views
from profileapp.views import ClientOrderCalculation, ProductOrderCalculation


urlpatterns = [
    path('product/',views.ProductListView.as_view()),
    path('orderss/',views.OrderListView.as_view()),
    path('clients/orders/', ClientOrderCalculation.as_view()),
    path('product/subject/',ProductOrderCalculation.as_view()),

]
from django.urls import path
from .import views 
from orm.views import *


urlpatterns = [
    path('client/',views.ClientListView.as_view()),
    path('post/',views.PostListView.as_view()),
    path('post/<int:pk>/',PostDetailView.as_view()),
    path('person/',views.PersonView.as_view()),
    path('persons/',views.PersonSubView.as_view()),
    # path('person_list/',views.PersonListView.as_view()),
    path('personlist/',views.PersonListView.as_view()),
    path('personlist/<int:pk>/', PersonDetailAPView.as_view()),
    path('order/',OrderApiView.as_view()),
    path('order/<int:pk>/',OrderDetailView.as_view()),
]


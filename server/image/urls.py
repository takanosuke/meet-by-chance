from django.urls import path
# from .views import ImagesList
from . import views

urlpatterns = [
    # path('show/', ImagesList.as_view(), name='show'),
    path('create/', views.create, name='create'),
    path('changeframe/', views.changeframe, name='changeframe'),
    path('delete/<str:img_name>/', views.delete, name='delete'),
]

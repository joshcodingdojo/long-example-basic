from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('view-officials', views.view_officials),
    path('show-officials', views.show_officials),
    path('rate/<str:name>/<str:elected_office>', views.rate_official)
]

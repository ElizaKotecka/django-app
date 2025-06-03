from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    # path('<int:pk>', views.PostDetailView.as_view(), name='marketplace_show'),

]

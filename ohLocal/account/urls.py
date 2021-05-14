from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
	path('', views.registration_form, name="register"),
	path('register/', views.registration_form, name="register"),
	path('get_state_names/', views.get_state_names, name="get_state_names"),
	path('get_district_names/', views.get_district_names, name="get_district_names"),
	path('get_city_names/', views.get_city_names, name="get_city_names")
]
from django.shortcuts import render

from django.http import JsonResponse

from django.core import serializers

from .models import Country, State, District, City

# Create your views here.

def registration_form(request):
	countries = Country.objects.all()
	return render(request, "account/registration_form.html", { "countries": countries })

def get_state_names(request):
	country_name = request.GET.get("country_name")

	if country_name == None:
		state_names = serializers.serialize('json', State.objects.all())
	else:
		country = Country.objects.get(country_name__iexact=country_name)
		state_names = serializers.serialize('json', State.objects.filter(country=country))
	return JsonResponse(state_names, safe=False)

def get_district_names(request):
	state_name = request.GET.get("state_name")

	if state_name == None:
		district_names = serializers.serialize('json', District.objects.all())
	else:
		state = State.objects.get(state_name__iexact=state_name)
		district_names = serializers.serialize('json', District.objects.filter(state=state))
	return JsonResponse(district_names, safe=False)

def get_city_names(request):
	district_name = request.GET.get("district_name")

	if district_name == None:
		city_names = serializers.serialize('json', City.objects.all())
	else:
		district = District.objects.get(district_name__iexact=district_name)
		city_names = serializers.serialize('json', City.objects.filter(district=district))
	return JsonResponse(city_names, safe=False)
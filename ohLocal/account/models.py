from django.db import models

# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=20)

	def __str__(self):
		return self.country_name

class State(models.Model):
	state_name = models.CharField(max_length=20)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)

	def __str__(self):
		return self.state_name

class District(models.Model):
	district_name = models.CharField(max_length=20)
	state = models.ForeignKey(State, on_delete=models.CASCADE)

	def __str__(self):
		return self.district_name

class City(models.Model):
	city_name = models.CharField(max_length=20)
	district = models.ForeignKey(District, on_delete=models.CASCADE)

	def __str__(self):
		return self.city_name

class User(models.Model):
	name = models.CharField(max_length=20)
	birthdate = models.DateField()
	country = models.OneToOneField(Country, on_delete=models.DO_NOTHING)
	state = models.OneToOneField(State, on_delete=models.DO_NOTHING)
	district = models.OneToOneField(District, on_delete=models.DO_NOTHING)
	city = models.OneToOneField(City, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.name
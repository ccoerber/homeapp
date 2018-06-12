from django.http import HttpResponse
from .models import Location, Device
from django.shortcuts import render

def index(request):
	location_list = Location.objects.order_by('name_text')
	response = "<h2>All Locations</h2>"
	for loc in location_list:
		response = response + loc.name_text + "<br />"
		
	return HttpResponse(response)
	
def location(request, loc_id):
	loc_name = Location.objects.get(id=loc_id).name_text
	device_list = Device.objects.filter(location_fk=loc_id)
	context = {'device_list':device_list, 'loc_name':loc_name}
	return render(request, 'homeapp/location.html', context)
	
def sensor(request, sensor_id):
	response = "You're looking at sensor %s."
	return HttpResponse(response % sensor_id)

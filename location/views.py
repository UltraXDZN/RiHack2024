import json

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import City, SelectedLocation


# For GET requests
def get_locations(request):
    if request.method == 'GET':
        # Retrieve all cities from the database
        cities = City.objects.all()

        # Prepare data (no serialization)
        city_list = [f"{city.name}, {city.county.name}" for city in cities]

        # Return as a simple JSON response
        return JsonResponse({'locations': city_list})

    # If method is not GET, return 405 Method Not Allowed
    return HttpResponse(status=405)


@csrf_exempt
@login_required  # Ensure only logged-in users can select/deselect locations
def set_locations(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            selected_cities = data.get('selected_cities', [])
            user = request.user  # Get the logged-in user

            # If there are no selected cities, delete all previously selected locations for the user
            if not selected_cities:
                SelectedLocation.objects.filter(user=user).delete()
                return JsonResponse({'message': 'All selected locations deleted for user.'})

            # Otherwise, add the selected cities
            for city_name in selected_cities:
                try:
                    city = City.objects.get(name=city_name)
                    # Check if the city is already selected by the user
                    if not SelectedLocation.objects.filter(user=user, selected_city=city).exists():
                        SelectedLocation.objects.create(user=user, selected_city=city)
                except City.DoesNotExist:
                    return HttpResponseBadRequest(f"City '{city_name}' not found.")

            return JsonResponse({'message': 'Locations saved successfully!'})

        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")

    return HttpResponseBadRequest("Invalid request method")


@login_required  # Ensure the user is logged in
def get_selected_locations(request):
    user = request.user  # Get the logged-in user
    selected_locations = SelectedLocation.objects.filter(user=user)  # Fetch all selected locations for the user

    # Prepare a list of selected city names
    selected_cities = [location.selected_city.name for location in selected_locations]

    return JsonResponse({'selected_cities': selected_cities}, status=200)
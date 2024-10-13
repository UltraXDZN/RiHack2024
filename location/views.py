import json

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import City


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


# For POST requests
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import City, SelectedLocation


@csrf_exempt  # Skip CSRF for simplicity, adjust based on your needs
def set_locations(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            selected_cities = data.get('selected_cities', [])

            if not selected_cities:
                return HttpResponseBadRequest("No cities selected")

            # Process each city and save to SelectedLocation (or other logic as needed)
            for city_name in selected_cities:
                try:
                    city = City.objects.get(name=city_name)

                    # You can add logic to store the selected city for a user or log it
                    SelectedLocation.objects.create(selected_city=city, user=request.user)
                except City.DoesNotExist:
                    return HttpResponseBadRequest(f"City '{city_name}' not found.")

            return JsonResponse({'message': 'Locations saved successfully!'})

        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")

    return HttpResponseBadRequest("Invalid request method")

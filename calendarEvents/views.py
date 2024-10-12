from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.utils.dateparse import parse_datetime

import json
from .models import Event


# Get all events (GET)
@require_http_methods(['GET'])
def get_events(request):
    events = Event.objects.all().values()
    events_list = list(events)

    # Convert DateTimeFields to ISO format and add custom properties
    for event in events_list:
        if event['start_time']:
            event['start_time'] = event['start_time'].isoformat()
        if event['end_time']:
            event['end_time'] = event['end_time'].isoformat()
        # Create an Event instance to access properties
        event_instance = Event(**event)
        event['is_past'] = event_instance.is_past
        event['duration'] = event_instance.duration

    return JsonResponse({'events': events_list}, status=200)


# Get a single event (GET)
@require_http_methods(['GET'])
def get_event_detail(request, event_id):
    try:
        event = Event.objects.filter(id=event_id).values().first()
        if event is None:
            return JsonResponse({'error': 'Event not found'}, status=404)
        if event['start_time']:
            event['start_time'] = event['start_time'].isoformat()
        if event['end_time']:
            event['end_time'] = event['end_time'].isoformat()
        event_instance = Event(**event)
        event['is_past'] = event_instance.is_past
        event['duration'] = event_instance.duration
        return JsonResponse({'event': event}, status=200)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)


@csrf_exempt  # Only if you're not using CSRF tokens
@require_http_methods(['POST'])
def create_event(request):
    try:
        data = json.loads(request.body.decode('utf-8'))

        # Extract required and optional fields
        title = data['title']
        description = data.get('description', '')
        location = data.get('location', '')
        start_time_str = data['start_time']
        end_time_str = data.get('end_time', None)

        # Parse the datetime strings into datetime objects
        start_time = parse_datetime(start_time_str)
        if start_time is None:
            return JsonResponse({'error': 'Invalid start_time format'}, status=400)

        end_time = parse_datetime(end_time_str) if end_time_str else None
        if end_time_str and end_time is None:
            return JsonResponse({'error': 'Invalid end_time format'}, status=400)

        # Create a new Event object
        event = Event.objects.create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            location=location,
        )

        # Prepare response data
        event_data = {
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'start_time': event.start_time.isoformat(),
            'end_time': event.end_time.isoformat() if event.end_time else None,
            'location': event.location,
            'is_past': event.is_past,
            'duration': event.duration,
        }

        return JsonResponse({'success': 'Event created successfully', 'event': event_data}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# Delete an event (DELETE)
@csrf_exempt  # Only if you're not using CSRF tokens
@require_http_methods(['DELETE'])
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        return JsonResponse({'success': 'Event deleted successfully'}, status=200)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from django.http import HttpResponse, JsonResponse
import json

# Create your views here.


def index(request):
    return HttpResponse("This is the wellness index page")


def show(request, datatype, item_id):
    supported_types = ["cardio", "lifts", "workouts"]
    if datatype in supported_types:
        response_data = {'info': datatype, 'id': item_id, 'details': {'reps': 'NaN', 'weight': 'NaN2'}}
        response_json = json.dumps(response_data)
        return JsonResponse(json.loads(response_json))
    else:
        return HttpResponse(f'No data was found matching id #{item_id} from the {datatype} dataset')
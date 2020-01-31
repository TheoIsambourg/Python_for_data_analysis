from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from prediction.models import Activity
from prediction.serializers import ActivitySerializer

def predict_activity(data):
    from sklearn.externals.joblib import load
    model = load('./estimator.joblib')
    return model.predict([data['ACC_X']])[0]

@csrf_exempt
def activity_list(request):
    if request.method== 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method== 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            data['ACTIVITY_ID'] = predict_activity(data)
            serializer = ActivitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.problems.problems import Problems


@csrf_exempt
def problem1(request):
    output = ""
    if request.method == "POST":
        body = json.loads(request.body)
        problem = Problems(body["input-1"], "problem1")
        output = problem.solve()
    return JsonResponse({"output": output}, safe=False)


@csrf_exempt
def problem2(request):
    output = ""
    if request.method == "POST":
        body = json.loads(request.body)
        problem = Problems(body["input-2"], "problem2")
        output = problem.solve()
    return JsonResponse({"output": output}, safe=False)


@csrf_exempt
def problem3(request):
    output = ["respuesta 3", ]
    if request.method == "POST":
        body = json.loads(request.body)
        problem = Problems(body["input-3"], "problem3")
        output = problem.solve()
    return JsonResponse({"output": output}, safe=False)

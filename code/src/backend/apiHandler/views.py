from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Disable CSRF for simplicity, not recommended for production
def text_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            type = data.get("type", "")
            text = data.get("text", "")
            

            
            response_data = {"Text": text, "Type": type}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
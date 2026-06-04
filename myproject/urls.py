from django.contrib import admin
from django.urls import path
from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return JsonResponse({'status': 'success', 'message': 'Login successful', 'username': user.username})
        return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logout successful'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', login_view),
    path('api/logout/', logout_view),
]
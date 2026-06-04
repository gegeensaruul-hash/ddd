from django.contrib import admin
from django.urls import path
from django.contrib.auth import authenticate, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    dealers = [
        {'id': 1, 'name': 'Best Cars Dealership', 'city': 'New York', 'state': 'NY', 'rating': 4.5},
        {'id': 2, 'name': 'Premium Auto Sales', 'city': 'Los Angeles', 'state': 'CA', 'rating': 4.2},
        {'id': 3, 'name': 'City Motors', 'city': 'Chicago', 'state': 'IL', 'rating': 4.8},
        {'id': 4, 'name': 'Kansas Auto Center', 'city': 'Wichita', 'state': 'KS', 'rating': 4.3},
        {'id': 5, 'name': 'Sunflower Motors', 'city': 'Topeka', 'state': 'KS', 'rating': 4.6},
    ]
    user = request.user
    if user.is_authenticated:
        nav = '<p>Welcome, <b>' + user.username + '</b> | <a href="/admin/logout/">Logout</a></p>'
    else:
        nav = '<p><a href="/admin/">Login</a></p>'
    html = '<h1>Car Dealerships</h1>' + nav + '<table border="1"><tr><th>ID</th><th>Name</th><th>City</th><th>State</th><th>Rating</th><th>Action</th></tr>'
    for d in dealers:
        if user.is_authenticated:
            btn = '<a href="/api/reviews/' + str(d['id']) + '/">Review Dealer</a>'
        else:
            btn = ''
        html += '<tr><td>' + str(d['id']) + '</td><td>' + d['name'] + '</td><td>' + d['city'] + '</td><td>' + d['state'] + '</td><td>' + str(d['rating']) + '</td><td>' + btn + '</td></tr>'
    html += '</table>'
    return HttpResponse(html)

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

def get_dealer_reviews(request, dealer_id):
    reviews = [
        {'id': 1, 'dealer_id': dealer_id, 'reviewer': 'John Doe', 'rating': 5, 'comment': 'Excellent service!'},
        {'id': 2, 'dealer_id': dealer_id, 'reviewer': 'Jane Smith', 'rating': 4, 'comment': 'Very good experience.'},
    ]
    return JsonResponse({'dealer_id': dealer_id, 'reviews': reviews})

def get_all_dealers(request):
    dealers = [
        {'id': 1, 'name': 'Best Cars Dealership', 'city': 'New York', 'state': 'NY', 'rating': 4.5},
        {'id': 2, 'name': 'Premium Auto Sales', 'city': 'Los Angeles', 'state': 'CA', 'rating': 4.2},
        {'id': 3, 'name': 'City Motors', 'city': 'Chicago', 'state': 'IL', 'rating': 4.8},
        {'id': 4, 'name': 'Kansas Auto Center', 'city': 'Wichita', 'state': 'KS', 'rating': 4.3},
        {'id': 5, 'name': 'Sunflower Motors', 'city': 'Topeka', 'state': 'KS', 'rating': 4.6},
    ]
    return JsonResponse({'dealers': dealers})

def get_dealer_by_id(request, dealer_id):
    dealers = {
        1: {'id': 1, 'name': 'Best Cars Dealership', 'city': 'New York', 'state': 'NY', 'rating': 4.5, 'address': '123 Main St'},
        2: {'id': 2, 'name': 'Premium Auto Sales', 'city': 'Los Angeles', 'state': 'CA', 'rating': 4.2, 'address': '456 Sunset Blvd'},
        3: {'id': 3, 'name': 'City Motors', 'city': 'Chicago', 'state': 'IL', 'rating': 4.8, 'address': '789 Lake Shore Dr'},
    }
    dealer = dealers.get(dealer_id)
    if dealer:
        return JsonResponse({'dealer': dealer})
    return JsonResponse({'error': 'Dealer not found'}, status=404)

def get_dealers_by_state(request, state):
    all_dealers = [
        {'id': 1, 'name': 'Best Cars Dealership', 'city': 'New York', 'state': 'NY', 'rating': 4.5},
        {'id': 2, 'name': 'Premium Auto Sales', 'city': 'Los Angeles', 'state': 'CA', 'rating': 4.2},
        {'id': 3, 'name': 'City Motors', 'city': 'Chicago', 'state': 'IL', 'rating': 4.8},
        {'id': 4, 'name': 'Kansas Auto Center', 'city': 'Wichita', 'state': 'KS', 'rating': 4.3},
        {'id': 5, 'name': 'Sunflower Motors', 'city': 'Topeka', 'state': 'KS', 'rating': 4.6},
    ]
    filtered = [d for d in all_dealers if d['state'].lower() == state.lower()]
    return JsonResponse({'state': state, 'dealers': filtered})

def get_all_car_makes(request):
    car_makes = [
        {'id': 1, 'make': 'Toyota', 'models': ['Camry', 'Corolla', 'RAV4', 'Highlander']},
        {'id': 2, 'make': 'Honda', 'models': ['Civic', 'Accord', 'CR-V', 'Pilot']},
        {'id': 3, 'make': 'Ford', 'models': ['F-150', 'Mustang', 'Explorer', 'Escape']},
        {'id': 4, 'make': 'Chevrolet', 'models': ['Silverado', 'Equinox', 'Malibu', 'Tahoe']},
        {'id': 5, 'make': 'BMW', 'models': ['3 Series', '5 Series', 'X3', 'X5']},
    ]
    return JsonResponse({'car_makes': car_makes})

def analyze_review(request):
    text = request.GET.get('text', '')
    positive_words = ['fantastic', 'excellent', 'great', 'good', 'amazing', 'wonderful', 'best', 'love', 'perfect']
    negative_words = ['bad', 'terrible', 'awful', 'poor', 'worst', 'hate', 'horrible', 'disappointing']
    text_lower = text.lower()
    if any(word in text_lower for word in positive_words):
        sentiment = 'positive'
    elif any(word in text_lower for word in negative_words):
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return JsonResponse({'text': text, 'sentiment': sentiment})

def post_review(request, dealer_id):
    names = {1: 'Best Cars Dealership', 2: 'Premium Auto Sales', 3: 'City Motors', 4: 'Kansas Auto Center', 5: 'Sunflower Motors'}
    name = names.get(dealer_id, 'Unknown Dealer')
    if request.method == 'POST':
        reviewer = request.POST.get('reviewer', '')
        rating = request.POST.get('rating', '')
        comment = request.POST.get('comment', '')
        date = request.POST.get('date', '')
        html = '<h1>Review Added Successfully!</h1>'
        html += '<p><b>Dealer:</b> ' + name + '</p>'
        html += '<p><b>Reviewer:</b> ' + reviewer + '</p>'
        html += '<p><b>Rating:</b> ' + rating + '</p>'
        html += '<p><b>Review:</b> ' + comment + '</p>'
        html += '<p><b>Purchase Date:</b> ' + date + '</p>'
        html += '<p><a href="/">Back to Home</a></p>'
        return HttpResponse(html)
    html = '<h1>Post a Review for ' + name + '</h1>'
    html += '<form method="post">'
    html += '<p><label>Your Name:</label><br><input type="text" name="reviewer" value="John Doe" style="width:300px;padding:5px"></p>'
    html += '<p><label>Rating:</label><br><select name="rating" style="width:300px;padding:5px"><option value="5">5 - Excellent</option><option value="4">4 - Good</option><option value="3">3 - Average</option></select></p>'
    html += '<p><label>Review:</label><br><textarea name="comment" rows="4" style="width:300px;padding:5px">Fantastic services and great experience!</textarea></p>'
    html += '<p><label>Purchase Date:</label><br><input type="date" name="date" value="2026-06-04" style="width:300px;padding:5px"></p>'
    html += '<p><input type="submit" value="Submit Review" style="padding:10px 20px;background:#6c63ff;color:white;border:none;cursor:pointer"></p>'
    html += '</form>'
    return HttpResponse(html)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/login/', login_view),
    path('api/logout/', logout_view),
    path('api/reviews/<int:dealer_id>/', get_dealer_reviews),
    path('api/dealers/', get_all_dealers),
    path('api/dealers/<int:dealer_id>/', get_dealer_by_id),
    path('api/dealers/state/<str:state>/', get_dealers_by_state),
    path('api/carmakes/', get_all_car_makes),
    path('api/analyze/', analyze_review),
    path('api/postreview/<int:dealer_id>/', post_review),
]
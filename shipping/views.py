from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Shipping

# Create your views here.

@login_required
def shipping(request):
    user = request.user
    my_shippings = Shipping.objects.filter(user=user)
    return render(request, 'shipping/tracking.html', {'my_shippings': my_shippings})
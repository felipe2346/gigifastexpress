from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.models import Shipment, LiveUpdate
# from . import emailsend

def home(request):
    return render(request, 'frontend/index.html')


def contact_view(request):
    return render(request, 'frontend/contact.html')


def track_shipment(request):
    if request.method == 'POST':

        tracking_code = request.POST.get('tracking_code')
        shipments = Shipment.objects.filter(tracking_number=tracking_code)

        if shipments.exists():

            shipment_single = shipments.first()
            live_update = LiveUpdate.objects.filter(shipment=shipment_single)
            live_update_count = live_update.count()
            latest_update = live_update.last()

            return render(request, 'frontend/track_shipment.html', {'shipments':shipments, 'shipment_single':shipment_single,
            'update_count':live_update_count, 'latest_update':latest_update,
            'live_update':live_update}) 
        else:
            messages.error(request, "Invalid tracking code.  Please check the code and try again.")
            return redirect('frontend:track_shipment')
    return render(request, 'frontend/track_shipment.html')


def about(request):
    return render(request, 'frontend/about.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account:dashboard')    
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'frontend/login.html')


@login_required()
def logoutUser(request):
	logout(request)
	return redirect('frontend:login')

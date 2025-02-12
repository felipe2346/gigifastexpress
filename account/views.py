from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Shipment, LiveUpdate
from .forms import ShipmentCreateForm, LiveUpdateCreateForm

class DashboardView(LoginRequiredMixin, ListView):
    model = Shipment
    template_name = 'account/dashboard.html'
    context_object_name = 'shipments'
    paginate_by = 15

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_staff:
    #         return HttpResponseRedirect(reverse_lazy('shipment:n_dashboard'))        
    #     return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super(DashboardView, self).get_queryset(*args, **kwargs)
    #     qs = qs.order_by("-created")
    #     return qs


@login_required
def create_new_shipment(request):
    form = ShipmentCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'A new shippment was created successfully')
        return redirect('account:dashboard')

    context = {'form':form}
    return render(request, 'account/create_shipment.html', context)


@login_required
def edit_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    form = ShipmentCreateForm(request.POST or None, instance=shipment)

    if form.is_valid():
        form.save()
        messages.success(request, 'Shippment was Updated successfully')
        return redirect('account:dashboard')
    
    context = {'form':form}
    return render(request, 'account/edit_shipment.html', context)


@login_required
def delete_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    shipment.delete()
    messages.success(request, 'Shipment was deleted successfully')
    return redirect('account:dashboard')


@login_required
def shipment_detail(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    live_update = LiveUpdate.objects.filter(shipment=shipment)
    live_update_count = live_update.count()
    latest_update = live_update.last()

    form = LiveUpdateCreateForm(request.POST or None)
    
    if form.is_valid():
        update_live_object = form.save(commit=False)
        update_live_object.shipment = shipment
        update_live_object.save()
        
        # Set a session variable to indicate that the form was submitted
        request.session['form_submitted'] = True

        # Display a success message
        messages.success(request, 'Live Update is saved successfully')
        
        # Redirect to the same shipment detail page
        return redirect('account:shipment_detail', pk=pk)
    
    # Check if the session variable exists
    form_submitted = request.session.pop('form_submitted', False)

    # Render the page with the context data
    context = {
        'shipment': shipment,
        'live_update': live_update,
        'update_count': live_update_count,
        'latest_update': latest_update,
        'form': form,
        'form_submitted': form_submitted
    }

    return render(request, 'account/shipment_detail.html', context)


@login_required
def update_live_update(request, pk):
    live_update = LiveUpdate.objects.get(pk=pk)

    form = LiveUpdateCreateForm(request.POST or None, instance=live_update)

    if form.is_valid():
        form.save()

        request.session['form_submitted'] = True

        # Display a success message
        messages.success(request, 'Live Update is saved successfully')
        
        # Redirect to the same shipment detail page
        return redirect('account:shipment_detail', pk=live_update.shipment.pk)
    
    form_submitted = request.session.pop('form_submitted', False)

    context = {'form':form, 'form_submitted': form_submitted}
    return render(request, 'account/update_live_update.html', context)


@login_required
def delete_live_update(request, pk):
    live_update = LiveUpdate.objects.get(pk=pk)
    live_update.delete()
    messages.success(request, 'Live Update is deleted successfully')
    return redirect('account:shipment_detail', pk=live_update.shipment.pk)


def view_receipt(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    live_update = LiveUpdate.objects.filter(shipment=shipment).first()

    context = {'shipment':shipment, 'live_update':live_update}
    return render(request, 'account/receipt.html', context)


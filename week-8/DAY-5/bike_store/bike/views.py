from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CustomerForm


# Create your views here.
def customers(request):
    customers_list = Customer.objects.all().order_by('first_name', 'last_name')
    context = {'customers': customers_list}
    return render(request, 'customers.html', context)


def customer(request, id:int):
    customer_obj = Customer.objects.get(id=id)
    context = {'customer': customer_obj}
    return render(request, 'customer.html', context)

def add_customer(request):
    if request.method == 'POST':
        form_filled = CustomerForm(request.POST)
        form_filled.save()

    form = CustomerForm()
    context = {'form': form}
    return render(request, 'add_customer.html', context)

def Rental_list(request):
    Rent_list = Rental.objects.filter(return_date__isnull=True).order_by("rental_date")
    context = {'Rental': Rent_list}
    return render(request, 'rental_list.html', context)

def rent_detail(request, pk):
    rental_detail = get_object_or_404(Rental, pk=pk)
    # get_object_or_404 ca verifie sil l'objet existe sinon ca tecris erreur 
    context = {'rent': rental_detail}
    return render(request, 'rental_detail.html', context)

def vehicle_list(request):
    vehicle_list = Vehicle.objects.all()
    context = {'rental_vehicle': vehicle_list}
    return render(request, 'vehicle_list.html', context)
    

def vehicle_detail(request, pk):
    vehicle_detail = get_object_or_404(Vehicle, pk=pk)
    context = {'vehicle': vehicle_detail, 'is_rental': is_rental}
    is_rental = Rental.objects.filter(return__date__isnull=True).exists()
    return render(request, 'vehicle_detail.html', context)


def add_vehicle(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_type')
        cost = request.POST.get()

    context = {'vehicle_id': vehicle_id, 'cost': cost}
    return render(request, 'add_vehicle.html', context )

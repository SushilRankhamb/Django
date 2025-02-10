from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Car
from .forms import ProductForm

# Home page view to display all cars and handle adding new cars
def home(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    cars = Car.objects.all()  # Fetch all cars from the database
    return render(request, 'electronics/home.html', {'data1': cars, 'form': form})

# Update Car view
def update_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)  # Fetch car by its ID
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()  # Save the updated car data
            return HttpResponseRedirect("/")  # Redirect to the home page
    else:
        form = ProductForm(instance=car)  # Pre-fill the form with existing car data

    return render(request, 'update_car.html', {'form': form})

# Delete Car view
def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)  # Fetch the car by its ID
    if request.method == "POST":
        car.delete()  # Delete the car
        return HttpResponseRedirect("/")  # Redirect to the home page after deletion

    return render(request, 'confirm_delete_car.html', {'car': car})

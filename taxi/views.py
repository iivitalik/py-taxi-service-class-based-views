from django.shortcuts import render
from django.views import View

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(View):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(View):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(View):
    model = Car


class DriverListView(View):
    model = Driver
    paginate_by = 5


class DriverDetailView(View):
    model = Driver
    queryset = Driver.objects.select_related("manufacturer")

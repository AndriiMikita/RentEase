from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

class Apartment_view(View):
    template_name = 'apartments/apartment.html'

    def get(self, request, object_id):
        apartment = get_object_or_404(Apartment, pk=object_id)
        
        context = {'apartment': apartment,
                   'apartment_type': apartment.type_set.first(),}
        return render(request, self.template_name, context)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import SMS

class SMSListView(ListView):
    model = SMS
    template_name = 'testapp/sms_list.html'
    success_url = reverse_lazy('testapp:sms_list')

from django.shortcuts import render
from .forms import AddressForm

def address_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = AddressForm()
    return render(request, 'address.html', {'form': form})

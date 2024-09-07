from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

from bboard.forms import BbForm
from bboard.models import Bb, Rubric
from testapp.views import SMSListView
from bboard.forms import MyForm

def my_controller(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Form submitted successfully!')
            return redirect('bboard:index')
        else:
            messages.error(request, 'Form is invalid. Please try again.')
    else:
        form = MyForm()

    return render(request, 'bboard/da.html', {'form': form})


def add_and_save(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('bboard:by_rubric',
                                                kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)
    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return HttpResponse(render_to_string('bboard/index.html',
                                         context, request))








def by_rubric(request, rubric_id):
    # bbs = Bb.objects.filter(rubric=rubric_id)
    # rubrics = Rubric.objects.all()
    rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
    current_rubric = Rubric.objects.get(pk=rubric_id)

    # bbs = current_rubric.entries.all()
    bbs = current_rubric.bb_set.all()

    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}

    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['rubrics'] = Rubric.objects.all()
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
        return context


def fromtestapp(request):
    return SMSListView(request)



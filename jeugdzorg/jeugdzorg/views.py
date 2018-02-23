from django.views.generic import TemplateView
from django.views.generic import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django import forms
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.management import call_command
import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import select_template
from django.core.exceptions import ObjectDoesNotExist
from .mail import send_simple_message
from .auth import auth_test
from django.contrib import messages


class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'snippets/config.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        error_log = "/var/log/nginx/error.log"
        access_log = "/var/log/nginx/access.log"

        error_log_f = open(error_log, 'r')
        access_log_f = open(access_log, 'r')
        data['error'] = [line.rstrip('\n') for line in open(error_log, 'r')]
        # data['error'] = error_log_f.read()
        # data['access'] = access_log_f.read()
        data['access'] = [line.rstrip('\n') for line in open(access_log, 'r')]

        return data


class RegelingList(ListView):
    model = Regeling

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        template = select_template([
            'snippets/regeling_list_%s.html' % self.request.GET.get('beeld', 'alfabet'),
            'snippets/regeling_list_alfabet.html'
        ])
        data['doelen'] = Doel.objects.all()
        data['list_template'] = template
        return data


class RegelingDetail(DetailView):
    model = Regeling


class RegelingDelete(UserPassesTestMixin, DeleteView):
    model = Regeling
    success_url = reverse_lazy('regelingen')

    def test_func(self):
        return auth_test(self.request.user, 'editor')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        return data

    def delete(self, request, *args, **kwargs):

        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        messages.add_message(self.request, messages.INFO, "De regeling '%s' is verwijderd." % self.object.titel)
        self.object.delete()
        return HttpResponseRedirect(success_url)


class RegelingCreate(UserPassesTestMixin, CreateView):
    model = Regeling
    fields = ['titel', 'samenvatting', 'bron', 'aanvraag_url', 'bron_url', 'startdatum', 'einddatum']
    success_url = reverse_lazy('regelingen')

    def test_func(self):
        return auth_test(self.request.user, 'editor')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        post = self.request.POST
        if post:
            data['voorwaarde'] = VoorwaardeFormSet(self.request.POST, self.request.FILES)
            data['dfs'] = DoelFormSet(self.request.POST, self.request.FILES)
            data['crfs'] = ContactNaarRegelingFormSet(self.request.POST, self.request.FILES)

        else:
            data['voorwaarde'] = VoorwaardeFormSet()
            data['dfs'] = DoelFormSet()
            data['crfs'] = ContactNaarRegelingFormSet()
        return data

    def get_success_url(self):
        if self.request.POST.get('submit'):
            return self.request.POST.get('submit')
        return reverse_lazy('update_regeling', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        context = self.get_context_data()
        voorwaarde = context['voorwaarde']
        crfs = context['crfs']
        dfs = context['dfs']
        with transaction.atomic():
            self.object = form.save()
            if voorwaarde.is_valid():
                voorwaarde.instance = self.object
                voorwaarde.save()
            if crfs.is_valid():
                crfs.instance = self.object
                crfs.save()
            if dfs.is_valid():
                dfs.instance = self.object
                dfs.save()
        messages.add_message(self.request, messages.INFO, "De regeling '%s' is aangemaakt." % self.object.titel)
        return super(RegelingCreate, self).form_valid(form)


class RegelingUpdate(UserPassesTestMixin, UpdateView):
    model = Regeling
    fields = ['titel', 'samenvatting', 'bron', 'aanvraag_url', 'bron_url', 'startdatum', 'einddatum']
    success_url = reverse_lazy('regelingen')

    def test_func(self):
        return auth_test(self.request.user, 'editor')

    def get_success_url(self):
        if self.request.POST.get('submit'):
            return self.request.POST.get('submit')
        return reverse_lazy('update_regeling', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        post = self.request.POST
        if post:
            data['voorwaarde'] = VoorwaardeFormSet(self.request.POST, self.request.FILES, instance=self.object)
            data['dfs'] = DoelFormSet(self.request.POST, self.request.FILES, instance=self.object)
            data['crfs'] = ContactNaarRegelingFormSet(self.request.POST, self.request.FILES, instance=self.object)

        else:
            data['voorwaarde'] = VoorwaardeFormSet(instance=self.object)
            data['dfs'] = DoelFormSet(instance=self.object)
            data['crfs'] = ContactNaarRegelingFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        voorwaarde = context['voorwaarde']
        crfs = context['crfs']
        dfs = context['dfs']
        with transaction.atomic():
            self.object = form.save()
            if voorwaarde.is_valid():
                voorwaarde.instance = self.object
                voorwaarde.save()
            if crfs.is_valid():
                crfs.instance = self.object
                crfs.save()
            if dfs.is_valid():
                dfs.instance = self.object
                dfs.save()

        messages.add_message(self.request, messages.INFO, "De regeling '%s' is aangepast." % self.object.titel)
        return super(RegelingUpdate, self).form_valid(form)


@staff_member_required
def dump_jeugdzorg(request):
    sysout = sys.stdout
    fname = "%s.json" % ('jeugdzorg')
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=%s' % fname

    sys.stdout = response
    call_command('dumpdata', 'jeugdzorg', '--indent=4')
    sys.stdout = sysout

    # send_simple_message()

    return response


@staff_member_required
def load_jeugdzorg(request):
    if request.method == 'POST':
        form = UploadJeugdzorgFixtureFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('%s?success=1' % reverse('loadjeugdzorg'))
    else:
        form = UploadJeugdzorgFixtureFileForm()
    return render(request, 'snippets/upload_fixture.html', {'form': form})




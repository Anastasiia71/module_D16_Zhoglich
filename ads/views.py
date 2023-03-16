from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad, Response
from .filters import ResponseFilter
from .forms import AdForm, ResponseForm


class AdList(ListView):
    model = Ad
    ordering = 'title'
    template_name = 'ads.html'
    context_object_name = 'ads'


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'


class AdCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('ads.add_ad')
    form_class = AdForm
    model = Ad
    template_name = 'ad_create.html'


class AdUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('ads.change_ad')
    form_class = AdForm
    model = Ad
    template_name = 'ad_create.html'


class AdDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad_list')


class ResponseList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Response
    ordering = 'author'
    template_name = 'responses.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ResponseDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'


class ResponseCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('ads.response_create')
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'


class ResponseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('ads.response_delete')
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('ad_list')

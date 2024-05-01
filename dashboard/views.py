from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView

@method_decorator(login_required, name='dispatch')
class SeeInfoView(TemplateView):
    template_name = 'dashboard/see_info/see-info.html'
@method_decorator(login_required, name='dispatch')
class HideInfoView(TemplateView):
    template_name = 'dashboard/hide_info/hide-info.html'


from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'dashboard/see_info/see-info.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard:see_info:see_info')
        else:
            return redirect('users:login')
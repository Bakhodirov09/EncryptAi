from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, View
import random
from conf import settings
from users.form import RegisterForm, UsersModel, LoginForm
from users.models import ConfirmationCodesModel

class RegisterView(View):
    def get(self, request):
        return render(request, 'users_html_files/register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if request.POST['check'] == True:
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('dashboard:see_info:see_info')
            else:
                context = {
                    'message': form.errors
                }
                return render(request, 'users_html_files/login.html', context=context)
        else:
            context = {
                'message': 'Iltimos EncryptAi shartlariga rozilik bildiring.!!'
            }
            return render(request, 'users_html_files/login.html', context=context)
@method_decorator(login_required, name='dispatch')
class AccountView(ListView):
    template_name = 'users_html_files/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['account'] = UsersModel.objects.get(username=self.request.user.username)


class LoginView(View):
    def get(self, request):
        return render(request, 'users_html_files/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('dashboard:see_info:see_info')
            else:
                context = {
                    'message': 'Username yoki parol xato !'
                }
                return render(request, 'users_html_files/login.html', context)
        else:
            return HttpResponse(form.errors, status=440)

# class GetUserEncryptedInfosView(ListView):
#     template_name = 'users_html_files/my_encrypted_infos.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['hidden_infos'] = HiddenInfoModel.objects.filter(user=self.request.user)
#         context['saw_infos'] = SawInfoModel.objects.filter(user=self.request.user)
#         return context

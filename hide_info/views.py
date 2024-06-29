import ast
import random
import string
from io import BytesIO
from PIL import Image
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from stegano.lsb import lsb
from hide_info.models import *
from django.http import HttpResponseBadRequest, HttpResponse
from environs import Env

env = Env()
env.read_env()

ENCRYPTION_KEYS = env.str('ENCRYPTION_KEYS')
ENCRYPTION_SECRETS_str = env.str('ENCRYPTION_SECRETS')

ENCRYPTION_SECRETS = ast.literal_eval(ENCRYPTION_SECRETS_str)

@method_decorator(login_required, name='dispatch')
class HideInfoWithTextView(View):
    def get(self, request):
        return render(request, 'dashboard/hide_info/hide-info-with-text.html')

    def post(self, request):
        msg = request.POST['message'].split(' ')
        status = False
        for message in msg:
            if message.isalpha():
                status = True
            else:
                status = False
        if status == True:
            message = list(request.POST['message'].lower())
            counter = 0
            encrypted_message = ""
            random_number = random.randint(0, len(request.POST['message']))
            sanoq = 0
            while message:
                encrypted_message += random.choice(ENCRYPTION_KEYS)
                if counter == random_number:
                    encrypted_message += f'({counter})'
                    count = 1
                    while count <= random_number:
                        encrypted_message += random.choice(ENCRYPTION_KEYS)
                        count += 1
                    try:
                        encrypted_message += ENCRYPTION_SECRETS[message[0]]
                        message.remove(message[0])
                        random_number = random.randint(0, len(request.POST['message']))
                        counter = 0
                        sanoq = 0
                        counter += 1
                    except IndexError:
                        pass
                else:
                    if sanoq == 5:
                        counter = random_number
                        random_number = random_number
                        sanoq = 0
                    else:
                        counter += 1
                        random_number = random.randint(0, len(request.POST['message']))
                        sanoq += 1
            context = {
                'encrypted_text': encrypted_message
            }
            HiddenTextsModel.objects.create(
                user=request.user,
                username=request.user.username,
                encrypted_text=encrypted_message,
                decrypted_text=request.POST['message']
            )
            return render(request, 'dashboard/hide_info/hide-info-with-text.html', context)
        else:
            return render(request, 'dashboard/hide_info/hide-info-with-text.html', {'message': "Iltimos ma'lumotlarni tekshirib qayta kiriting!"})


@method_decorator(login_required, name='dispatch')
class HideInfoWithPhotoView(View):

    def get(self, request):
        return render(request, 'dashboard/hide_info/hide-info-with-photo.html')

    def post(self, request):
        uploaded_image = request.FILES.get('image')
        if not uploaded_image:
            return HttpResponseBadRequest("Rasm fayli topilmadi.")
        message = request.POST.get('message')
        img = Image.open(uploaded_image)
        encoded_image = lsb.hide(image=img, message=message)
        with BytesIO() as output:
            encoded_image.save(output, format='PNG')
            encoded_image_bytes = output.getvalue()
        file_dir = os.path.join(settings.MEDIA_ROOT, 'hidden_images')
        os.makedirs(file_dir, exist_ok=True)
        new_image = HiddenImagesModel.objects.create(
            title=message,
            user=request.user,
            username=request.user.username
        )
        file_path = os.path.join(file_dir, f"{request.user}'s_{new_image.id}_hidden_image.png")
        with open(file_path, 'wb') as f:
            f.write(encoded_image_bytes)
        new_image.image = file_path
        new_image.save()
        context = {
            'image': new_image.image
        }
        return render(request, 'dashboard/hide_info/hide-info-with-photo.html', context)


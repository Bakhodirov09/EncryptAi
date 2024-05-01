import ast
import os.path
import random
from environs import Env
from conf import settings as keys
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from stegano.lsb import lsb
from conf import settings
from hide_info.models import HiddenInfoModel
from see_info.models import SawInfoModel

env = Env()
env.read_env()

ENCRYPTION_SECRETS_str = env.str('ENCRYPTION_SECRETS')

ENCRYPTION_SECRETS = ast.literal_eval(ENCRYPTION_SECRETS_str)

@method_decorator(login_required, name='dispatch')
class SeeInfoWithTextView(View):
    def get(self, request):
        return render(request, 'dashboard/see_info/see-info-with-text.html')

    def post(self, request):
        decrypted_message_keys = ""
        decrypted_message = ""
        xabar = request.POST['message']
        while "(" in xabar:
            index_open = xabar.index("(")
            index_close = xabar.index(")")
            number = int(xabar[index_open + 1:index_close])
            char_index = index_close + 1 + number
            decrypted_message_keys += xabar[char_index]
            xabar = xabar[char_index + 1:]

        reversed_dict = {value: key for key, value in ENCRYPTION_SECRETS.items()}
        for char in decrypted_message_keys:
            decrypted_message += reversed_dict[char]
        return render(request, 'dashboard/see_info/see-info-with-text.html', context={'decrypted_message': decrypted_message})

@method_decorator(login_required, name='dispatch')
class SeeInfoWithImageView(View):
    def get(self, request):
        return render(request, 'dashboard/see_info/see-info-with-image.html')

    def post(self, request):
        image = request.FILES['image']
        img_read = image.read()
        img = Image.open(image)
        try:
            hidden_info = lsb.reveal(img)
            file_dir = os.path.join(settings.MEDIA_ROOT, 'saw_info_images')
            os.makedirs(file_dir, exist_ok=True)
            new_image = SawInfoModel.objects.create(
                title=hidden_info,
                user=request.user
            )

            file_path = os.path.join(file_dir, f"{request.user}'s_{new_image.id}_saw_image.png")

            with open(file_path, 'wb') as f:
                f.write(img_read)

            new_image.image = file_path
            new_image_id = new_image.id
            new_image.save()

            context = {
                'hidden_info': hidden_info,
                'image': SawInfoModel.objects.get(user=request.user, id=new_image_id).image
            }
        except IndexError:
            context = {
                'hidden_info': "Ushbu suratda hech qanday ma'lumot shifrlanmagan! :("
            }
        return render(request, 'dashboard/see_info/see-info-with-image.html', context)

# Generated by Django 5.0.4 on 2024-04-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('see_info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sawinfomodel',
            old_name='info',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='sawinfomodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='saw_images/'),
        ),
    ]

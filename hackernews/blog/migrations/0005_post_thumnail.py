# Generated by Django 4.1 on 2022-08-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumnail',
            field=models.ImageField(blank=True, default='thumnail.jpg', null=True, upload_to=''),
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
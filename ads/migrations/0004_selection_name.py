# Generated by Django 4.1 on 2022-09-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1 on 2022-08-31 03:20

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_cidade_equipamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='ip',
            field=models.GenericIPAddressField(validators=[polls.models.valid_ip]),
        ),
    ]

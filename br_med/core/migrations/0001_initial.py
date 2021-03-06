# Generated by Django 4.0.5 on 2022-07-01 05:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('date', models.DateField(verbose_name='data de referência')),
                ('currency', models.CharField(choices=[('USD', 'Usd'), ('BRL', 'Brl'), ('EUR', 'Eur'), ('JPY', 'Jpy')], max_length=3, verbose_name='moeda')),
                ('value', models.DecimalField(decimal_places=20, max_digits=100, verbose_name='valor da cotação')),
            ],
            options={
                'verbose_name': 'cotação',
                'verbose_name_plural': 'cotações',
            },
        ),
    ]

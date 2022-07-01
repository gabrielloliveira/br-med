# Generated by Django 4.0.5 on 2022-07-01 03:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('name', models.CharField(max_length=25, verbose_name='moeda')),
                ('symbol', models.CharField(max_length=25, verbose_name='símbolo')),
                ('acronym', models.CharField(max_length=3, verbose_name='acrônimo')),
            ],
            options={
                'verbose_name': 'moeda',
                'verbose_name_plural': 'moedas',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('date', models.DateField(verbose_name='data de referência')),
                ('value', models.DecimalField(decimal_places=20, max_digits=100, verbose_name='valor da cotação')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.currency')),
            ],
            options={
                'verbose_name': 'cotação',
                'verbose_name_plural': 'cotações',
            },
        ),
    ]
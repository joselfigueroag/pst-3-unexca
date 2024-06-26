# Generated by Django 4.2.3 on 2024-04-21 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50, verbose_name='accion')),
                ('model', models.CharField(max_length=50, verbose_name='modelo afectado')),
                ('action_time', models.DateTimeField(auto_now_add=True, verbose_name='fecha de accion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audits', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
        ),
    ]

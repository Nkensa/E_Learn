# Generated by Django 5.0.4 on 2024-05-21 16:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('E_LearnApp_Admin', '0002_classroom'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('adventure_id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_LearnApp_Admin.classroom')),
                ('subjects', models.ManyToManyField(to='E_LearnApp_Admin.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
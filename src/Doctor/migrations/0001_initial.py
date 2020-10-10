# Generated by Django 2.2.4 on 2019-08-09 17:11

import User.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('degree', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('User.user', models.Model),
            managers=[
                ('objects', User.models.UserManager()),
            ],
        ),
    ]
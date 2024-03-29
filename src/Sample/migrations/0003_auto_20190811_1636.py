# Generated by Django 2.2.4 on 2019-08-11 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sample', '0002_auto_20190809_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='batch_id',
            new_name='batch',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Address.Address'),
        ),
        migrations.CreateModel(
            name='SampleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(null=True)),
                ('comment_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sample.Sample')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

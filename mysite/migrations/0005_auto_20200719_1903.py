# Generated by Django 3.0.4 on 2020-07-19 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0004_auto_20200718_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pin',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='DistributionCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('pin', models.CharField(max_length=6, null=True)),
                ('phone', models.CharField(max_length=300, null=True)),
                ('administrator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

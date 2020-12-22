# Generated by Django 2.2.4 on 2019-09-16 10:18

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
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_category', models.CharField(default='', max_length=20)),
                ('p_subcategory', models.CharField(default='', max_length=20)),
                ('p_name', models.CharField(default='', max_length=50)),
                ('p_image', models.ImageField(default='', upload_to='images')),
                ('p_desc', models.CharField(default='', max_length=300)),
                ('p_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('person', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

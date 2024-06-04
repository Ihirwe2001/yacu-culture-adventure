# Generated by Django 5.0.1 on 2024-06-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination1', models.CharField(choices=[('Kigali city', 'Kigali city'), ('Northern Province', 'Northern Province'), ('Southern Province', 'Southern Province'), ('Eastern Province', 'Eastern Province'), ('Western Province', 'Western Province')], max_length=50)),
                ('destination2', models.CharField(choices=[('Kigali city', 'Kigali city'), ('Northern Province', 'Northern Province'), ('Southern Province', 'Southern Province'), ('Eastern Province', 'Eastern Province'), ('Western Province', 'Western Province')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('names', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('depart_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('duration', models.CharField(choices=[('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months')], max_length=10)),
            ],
        ),
    ]

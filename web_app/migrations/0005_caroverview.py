# Generated by Django 3.2.22 on 2023-11-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_carmodels_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarOverview',
            fields=[
                ('carmodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web_app.carmodels')),
                ('varients', models.CharField(max_length=1000)),
                ('ex_showroom_price', models.FloatField()),
                ('milage', models.CharField(max_length=1000)),
                ('engine', models.CharField(max_length=1000)),
                ('transmission', models.CharField(max_length=1000)),
                ('seating_capacity', models.IntegerField()),
                ('colors', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('white', 'White')], max_length=20)),
                ('user_review', models.FloatField()),
                ('description', models.TextField()),
            ],
            bases=('web_app.carmodels',),
        ),
    ]
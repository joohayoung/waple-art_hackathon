# Generated by Django 3.1.3 on 2020-11-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areainfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaid', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('genres', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-05 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.IntegerField()),
                ('female', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender_title', to='subapp.artinfodb')),
            ],
        ),
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teens', models.IntegerField()),
                ('Twenties', models.IntegerField()),
                ('Thirties', models.IntegerField()),
                ('Forty', models.IntegerField()),
                ('Fifties', models.IntegerField()),
                ('Sixteen', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='age_title', to='subapp.artinfodb')),
            ],
        ),
    ]
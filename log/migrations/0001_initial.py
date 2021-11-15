# Generated by Django 3.1.13 on 2021-11-10 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Easy-paced run, Strength training,...', max_length=50, unique=True, verbose_name='Name of the workout type')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('time', models.TimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('feeling', models.CharField(blank=True, choices=[('GREAT', 'Great'), ('GOOD', 'Good'), ('NORMAL', 'Normal'), ('POOR', 'Poor'), ('TERRIBLE', 'Terrible')], max_length=20)),
                ('effort', models.CharField(blank=True, choices=[('1', 'Very light'), ('2', 'Light'), ('3', 'Light'), ('4', 'Moderate'), ('5', 'Moderate'), ('6', 'Moderate'), ('7', 'Hard'), ('8', 'Hard'), ('9', 'Very hard'), ('10', 'Max effort')], max_length=20)),
                ('notes', models.CharField(blank=True, max_length=1000, verbose_name='post workout notes')),
                ('workouttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.workouttype')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
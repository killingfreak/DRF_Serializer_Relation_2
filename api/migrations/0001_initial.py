# Generated by Django 3.2 on 2022-10-20 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=30)),
                ('class_head', models.IntegerField()),
                ('school_name', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, related_name='school_name', to='api.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=30)),
                ('standard', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='api.teacher')),
                ('school', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='api.school')),
            ],
            options={
                'ordering': ['roll'],
            },
        ),
    ]

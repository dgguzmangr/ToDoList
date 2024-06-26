# Generated by Django 4.1.13 on 2024-04-10 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Title')),
                ('description', models.CharField(max_length=400, verbose_name='Description')),
                ('creation_date', models.DateField(null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='SubTasks',
            fields=[
                ('sub_task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Title')),
                ('description', models.CharField(max_length=400, verbose_name='Description')),
                ('creation_date', models.DateField(null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Title')),
                ('description', models.CharField(max_length=400, verbose_name='Description')),
                ('creation_date', models.DateField(null=True, verbose_name='Date')),
            ],
        ),
    ]

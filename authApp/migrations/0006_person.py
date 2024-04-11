# Generated by Django 4.1.13 on 2024-04-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_projects_status_subtasks_status_tasks_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='LastName')),
            ],
        ),
    ]
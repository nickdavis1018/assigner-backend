# Generated by Django 4.0.1 on 2022-01-28 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('assignee', models.CharField(max_length=50)),
                ('assigner', models.CharField(default='system', max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
                ('overdue', models.BooleanField(default=False)),
                ('flagged', models.BooleanField(default=False)),
                ('urgency', models.BooleanField(default=False)),
            ],
        ),
    ]
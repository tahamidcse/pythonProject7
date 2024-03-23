# Generated by Django 3.2.11 on 2024-03-23 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2000)),
                ('language', models.CharField(max_length=100)),
                ('submission_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('S', 'Success'), ('E', 'Error'), ('P', 'Pending')], max_length=1)),
                ('user_input', models.CharField(blank=True, max_length=200, null=True)),
                ('output', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineide.user')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('notes', models.TextField(null=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('yet_to_start', 'Yet to Start')], max_length=20)),
                ('time', models.IntegerField(null=True)),
            ],
        ),
    ]
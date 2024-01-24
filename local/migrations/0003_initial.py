# Generated by Django 4.1.3 on 2022-12-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('local', '0002_delete_test_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=50, null=True)),
                ('mail', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('number', models.CharField(max_length=50, null=True)),
                ('latest', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]

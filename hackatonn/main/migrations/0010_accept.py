# Generated by Django 4.2.dev20220912110250 on 2022-09-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_mash_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_train', models.BooleanField()),
            ],
        ),
    ]

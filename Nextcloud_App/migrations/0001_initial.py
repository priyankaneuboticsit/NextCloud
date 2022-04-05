# Generated by Django 4.0.3 on 2022-04-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contname', models.CharField(max_length=100)),
                ('contemail', models.EmailField(max_length=100)),
                ('contmessage', models.TextField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

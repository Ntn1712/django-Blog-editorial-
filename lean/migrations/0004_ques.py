# Generated by Django 2.1.1 on 2019-02-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0003_bangalore_chennai_delhi_mumbai'),
    ]

    operations = [
        migrations.CreateModel(
            name='ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques', models.CharField(max_length=2000)),
            ],
        ),
    ]

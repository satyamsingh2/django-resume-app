# Generated by Django 3.1.6 on 2021-02-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=30)),
                ('your_email', models.EmailField(max_length=254)),
                ('your_subject', models.CharField(max_length=30)),
                ('your_message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

# Generated by Django 2.1.5 on 2019-04-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pictures/')),
                ('email', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('class1', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]

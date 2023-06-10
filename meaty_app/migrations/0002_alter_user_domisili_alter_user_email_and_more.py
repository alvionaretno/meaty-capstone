# Generated by Django 4.2.2 on 2023-06-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('meaty_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='domisili',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='meat_users', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pekerjaan',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='meat_users', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usia',
            field=models.IntegerField(),
        ),
    ]

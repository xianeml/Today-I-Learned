# Generated by Django 3.1.1 on 2020-09-27 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(max_length=45)),
                ('category_code', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('category_desc', models.CharField(max_length=100)),
                ('list_count', models.IntegerField(blank=True, null=True)),
                ('authority', models.IntegerField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'board_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoardLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'board_likes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoardReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField()),
                ('registered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reference_reply_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'board_replies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('registered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('view_count', models.IntegerField(blank=True, default=0)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d')),
            ],
            options={
                'db_table': 'boards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_superuser', models.IntegerField()),
                ('last_name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=254)),
                ('date_of_birth', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_staff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
    ]

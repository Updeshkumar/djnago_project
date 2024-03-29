# Generated by Django 3.2.19 on 2023-05-22 14:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('country_code', models.IntegerField(default=91)),
                ('mobile_number', models.CharField(max_length=20, unique=True)),
                ('otp', models.CharField(blank=True, max_length=4, null=True)),
                ('updated_by', models.IntegerField(default=False, null=True)),
                ('email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_type', models.CharField(default='USER', max_length=20)),
                ('profile_pic', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=1)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=0)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Account_Pending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('otp', models.PositiveIntegerField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=20, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_registered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Districts',
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'States',
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='tahseel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahseel_name', models.CharField(max_length=100)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_city', to='account.district')),
            ],
            options={
                'verbose_name_plural': 'Tahseel',
                'db_table': 'tahseel',
            },
        ),
        migrations.CreateModel(
            name='profileofall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('heavy_vehicle', 'heavy_vehicle'), ('driver', 'driver'), ('subcotructor', 'subcotructor'), ('labour', 'labour'), ('user', 'user')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_district', to='account.state'),
        ),
    ]

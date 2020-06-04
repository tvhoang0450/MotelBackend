# Generated by Django 3.0.4 on 2020-06-01 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('local', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='baseInforMotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=20)),
                ('DienTich', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateField(default=django.utils.timezone.now)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='local.District')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('washing_machine', models.BooleanField(default=False)),
                ('air_condition', models.BooleanField(default=False)),
                ('yard', models.BooleanField(default=False)),
                ('PCCC', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('board', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motel.baseInforMotel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageMotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='motel/')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motel.baseInforMotel')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoiDung', models.TextField(max_length=1000)),
                ('address', models.CharField(max_length=500)),
                ('motel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motel.baseInforMotel')),
            ],
        ),
        migrations.AddField(
            model_name='baseinformotel',
            name='typeMotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motel.TypeMotel'),
        ),
        migrations.AddField(
            model_name='baseinformotel',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='local.Ward'),
        ),
    ]

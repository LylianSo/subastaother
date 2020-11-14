# Generated by Django 3.1.3 on 2020-11-14 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subastaApp', '0002_clientes_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subastaApp.vehiculo')),
            ],
        ),
    ]

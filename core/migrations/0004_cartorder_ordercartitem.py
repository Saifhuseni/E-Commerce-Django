# Generated by Django 4.2.10 on 2024-04-01 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9999999)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.BooleanField(default=False)),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9999999)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cartorder')),
            ],
        ),
    ]

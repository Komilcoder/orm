# Generated by Django 3.1.7 on 2021-03-07 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0008_auto_20210303_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('create_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete')], max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.persons')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.product')),
            ],
        ),
    ]

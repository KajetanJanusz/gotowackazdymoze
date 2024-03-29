# Generated by Django 4.2.6 on 2023-10-31 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_converter_spoons_alter_converter_factor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='converter',
            name='factor',
            field=models.IntegerField(verbose_name='Przelicznik'),
        ),
        migrations.AlterField(
            model_name='converter',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Produkt'),
        ),
    ]

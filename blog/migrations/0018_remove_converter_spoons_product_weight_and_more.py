# Generated by Django 4.2.6 on 2023-11-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='converter',
            name='spoons',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=1, verbose_name='Waga łyżki'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('mililitr', 'ml'), ('gram', 'gr'), ('sztuki', 'szt')], default=1, max_length=20, verbose_name='Jednostka'),
            preserve_default=False,
        ),
    ]

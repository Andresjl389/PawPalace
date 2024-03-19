from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='descripcion',
            field=models.IntegerField(null=True, verbose_name='Cantidad'),
        ),
    ]

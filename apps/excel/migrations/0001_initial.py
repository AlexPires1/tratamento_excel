# Generated by Django 4.1.3 on 2022-11-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id_excel', models.AutoField(primary_key=True, serialize=False)),
                ('excel', models.FileField(upload_to='excel_arquivos/')),
                ('excel_tratado', models.FileField(upload_to='excel_arquivos/')),
            ],
        ),
    ]

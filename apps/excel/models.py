from django.db import models


class Excel(models.Model):
    id_excel = models.AutoField(primary_key=True)
    excel = models.FileField(upload_to='excel_arquivos/')
    excel_tratado = models.FileField(upload_to='excel_arquivos/')

from django.shortcuts import render
from . form import ExcelForm
from . models import Excel
import os
from django.http import HttpResponseRedirect, HttpResponse
import pandas as pd
import xlwt
from django.contrib import messages

myfile = "documents/excel_arquivos/Excel.xlsx"


def uploadExcel(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if os.path.isfile(myfile):
            os.remove(myfile)
        if form.is_valid():
            arquivo_excel = os.listdir("documents/excel_arquivos/")
            excel = form.save()

            if arquivo_excel[0] != "Excel.xlsx":
                os.rename("documents/excel_arquivos/" + arquivo_excel[0], "documents/excel_arquivos/Excel.xlsx")

            planilha = pd.read_excel("documents/excel_arquivos/Excel.xlsx", engine='openpyxl')
            try:
                novo_df = planilha.groupby(['CC', 'Fornecedor', 'Número', 'Dt Venc Rep.'])['Total'].sum().reset_index()
            except:
                try:
                    novo_df = planilha.groupby(['Coletor de Custo', 'Fornecedor', 'Número', 'Dt Venc Rep.'])['Total'].sum().reset_index()
                except:
                    messages.info(request, 'Alguma coluna não está com o nome correto!')

                    return render(request, 'excel/uploadExcel.html', {'form': form})

            novo_df.to_excel("documents/excel_arquivos/excel_tratado.xlsx", sheet_name="Tratados", index=False)

            with open('documents/excel_arquivos/excel_tratado.xlsx', 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename('documents/excel_arquivos/excel_tratado.xlsx')
                return response

    else:
        form = ExcelForm()
        return render(request, 'excel/uploadExcel.html', {'form': form})


# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.template import loader

from IACode.sniffer import Sniffer
from home.forms import HomeForm
from .models import CodeSnippet, Scores
import pandas as pd
from chartkick.django import BarChart, PieChart

from django.shortcuts import render

@csrf_exempt
def code(request):
    
    
    unit_chart = "No codes to check. Send the code in the text box."
    if 'code' in locals():
        print(f"code: {code}")
    else:
        print("create code")
        code = None

    template = loader.get_template("home/code.html")

    if request.POST:
        code = request.POST.get('code')

        session_key = request.session.session_key
        if session_key is None:
            # Se a session_key não existir, você pode forçar a criação de uma nova sessão
            request.session.create()
            session_key = request.session.session_key


        cs = CodeSnippet()
        cs.code = code
        cs.source = "web"
        cs.session_key = session_key
        cs.save()

        try:
            code_analysis_result = Sniffer.CodeAnalysis(code)
            for d in code_analysis_result:
                print(d)
                scores = Scores()
                scores.name = d
                scores.code = cs
                scores.value = code_analysis_result[d]
                scores.save()

            result = Sniffer.CodeAnalysis(code)
            result_gtz = {key: result[key] for key in result if result[key] > 0}
            unit_chart = PieChart(result_gtz, donut=True, percent=True)

            labels = []
            data = []

            for d in code_analysis_result:
                if d in ["Model Class", "Data Class", "Schizofrenic Class", "Futile Abstract Pipeline"]:
                    labels.append(d)
                    data.append(code_analysis_result[d])

            print(labels)

            return render(request, 'home/code.html', {
                'labels': labels,
                'data': data,
            })
        except Exception as error:
            unit_chart = error

    scores = Scores.objects.values('name').order_by('name').annotate(value=Avg('value')*100)
    cumulative_dic = {}
    for object in scores:
        cumulative_dic[object["name"]] = object["value"]
    # df = pd.DataFrame(scores)
    cumulative_chart = BarChart(cumulative_dic, colors= [["#DFFF00", "#FFBF00", "#FF7F50", "#DE3163", "#9FE2BF", "#40E0D0", "#6495ED", "#CCCCFF"]])
    context = {
        "cumulative_chart": cumulative_chart,
        "unit_chart": unit_chart,
        "form": HomeForm(),
        "code": code,
    }

    



    return HttpResponse(template.render(context, request))
def index(request):

    scores = Scores.objects.values('name').order_by('name').annotate(value=Count('value')*Avg('value'))
    df = pd.DataFrame(scores)
    df_labels = []
    if not df.empty:
        df_labels = df.name.tolist()
        df = df['value'].tolist()

    template = loader.get_template("home/index.html")
    context = {
        'df': df,
        'df_labels': df_labels
    }
    return HttpResponse(template.render(context, request))

def custom_404(request, exception):
    template = loader.get_template("home/page_not_found.html")
    context = {
    }

    return HttpResponse(template.render(context, request))
    # return HttpResponseNotFound('<h1>Página não encontrada</h1>')
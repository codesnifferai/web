# -*- coding: utf-8 -*-

from django.db.models import Avg, Count
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from django.template.defaultfilters import floatformat

from IACode.sniffer import Sniffer
from home.forms import HomeForm
from .models import CodeSnippet, Scores
import pandas as pd

def code(request):
    model = CodeSnippet
    form_class = HomeForm
    template_name = 'home/index.html'

    code_analysis_result = None
    code = None
    template = loader.get_template("home/code.html")

    if request.POST:
        code = request.POST.get('code')

        cs = CodeSnippet()
        cs.code = code
        cs.source = "web"
        cs.save()

        code_analysis_result = Sniffer.CodeAnalysis(code)
        for d in code_analysis_result:
            scores = Scores()
            scores.name = d
            scores.code = cs
            scores.value = code_analysis_result[d]
            scores.save()

        code_analysis_result = Sniffer.CodeAnalysis(code)

    context = {
        "code_analysis_result": code_analysis_result,
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

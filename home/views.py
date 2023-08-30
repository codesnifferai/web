# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from IACode.sniffer import Sniffer
from home.forms import HomeForm
from .models import CodeSnippet

def code(request):
    model = CodeSnippet
    form_class = HomeForm
    template_name = 'home/index.html'

    code_analysis_result = None
    code = None
    template = loader.get_template("home/code.html")

    if request.POST:
        code = request.POST.get('code')
        code_analysis_result = Sniffer.CodeAnalysis()

    context = {
        "code_analysis_result": code_analysis_result,
        "form": HomeForm(),
        "code": code,
    }

    return HttpResponse(template.render(context, request))
def index(request):
    template = loader.get_template("home/index.html")
    context = { }
    return HttpResponse(template.render(context, request))

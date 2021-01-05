from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Survey, Question, Response

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SurveySerializer, QuestionSerializer, ResponseSerializer

import json

def index_redirect(request):
    return HttpResponseRedirect("/survey/")

def index(request):
    return render(request, "survey/index.html", locals())

def reply(request, token):
    survey = get_object_or_404(Survey, token=token)    
    if request.method == "POST":
        print(request.POST)
        ans = {}
        for qnum in request.POST:
            if qnum == "csrfmiddlewaretoken":
                continue
            ans[qnum] = request.POST[qnum] #[0]
        Response.objects.create(survey=survey, content=json.dumps(ans) )
        return render(request, "survey/reply_success.html", locals())
    elif request.method == "GET":
        questions = Question.objects.filter(survey=survey)
        return render(request, "survey/reply.html", locals())

@login_required
def survey_edit(request, token):
    survey = get_object_or_404(Survey, token=token)
    questions = Question.objects.filter(survey=survey)
    return render(request, "survey/survey_edit.html", locals())

@login_required
def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, "survey/survey_list.html", locals())

@login_required
def reply_summary(request, token):
    survey = get_object_or_404(Survey, token=token)
    questions = Question.objects.filter(survey=survey)
    questions_order = list(questions.values_list("pk", flat=True))
    print(questions_order)
    responses = Response.objects.filter(survey=survey)
    return render(request, "survey/reply_summary.html", locals())


class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survey.objects.all() #.order_by('-date_joined')
    serializer_class = SurveySerializer
    lookup_field = 'token'
    permission_classes = []

    # lookup_value_regex = "[^/]+" 

@receiver(post_save, sender=Survey)
def create_token_handler(sender, instance, created, **kwargs):
    if created:
        new_token = get_random_string(length=5)
        while Survey.objects.filter(token=new_token).exists():
            new_token = get_random_string(length=5)
        instance.token = new_token
        instance.save()

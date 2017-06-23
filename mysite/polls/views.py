# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Question, Choice

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    part1 = "<p>Hello. Your question id is %s" % question_id
    part2 = "<p>Your question is:asdf %s" % Question.objects.get(id=question_id)
    return HttpResponse(part1 + part2)

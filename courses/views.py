from django.http import HttpResponse
from django.shortcuts import render

from . models import Course

def course_list(request):
    courses = Course.objects.all()
    output = ', '.join([str(xourse) for course in courses])
    return HttpResponse(output)



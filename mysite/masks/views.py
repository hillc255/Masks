from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    latest_title_list = Mask.objects.order_by('-pub_date')[:5]
    template = loader.get_template('masks/index.html')
    context = {'latest_mask_list': latest_mask_list,}
    return HttpResponse(template.render(context, request))

def detail(request, title_id):
    return HttpResponse("You're looking at mask title %s." % title_id)

def results(request, title_id):
    response = "You're looking at the results of mask title %s."
    return HttpResponse(response % title_id)

def vote(request, title_id):
    return HttpRespose("You're voting on mask title %s." % title_id)

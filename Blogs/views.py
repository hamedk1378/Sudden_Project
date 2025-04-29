from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models as b_models

def blogs_home_view(request):
    return HttpResponse("Sudden Project`s Blogs Home")



def ideas_index_view(request):
    idea_q = b_models.Idea.objects.order_by("-pub_date")[:3]
    context = {"idea_list" : idea_q}
    return render(request, "Blogs/idea_index.html", context)


def idea_detail_view(request, idea_id):
    idea_ob = get_object_or_404(b_models.Idea, pk = idea_id)
    return render(request, "Blogs/idea_detail.html", {"idea_ob" : idea_ob})

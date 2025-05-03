from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from . import models as b_models


class IdeasIndexView(generic.ListView):
    template_name = "Blogs/idea_index.html"
    context_object_name = "idea_list"

    def get_queryset(self):
        return b_models.Idea.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:3]


class IdeaDetailView(generic.DetailView):
    template_name = "Blogs/idea_detail.html"
    model = b_models.Idea


def like_idea_view(request, idea_id):
    idea_ob = get_object_or_404(b_models.Idea, pk = idea_id)
    idea_ob.likes = F("likes") + 1
    idea_ob.save()
    return HttpResponseRedirect(reverse("blogs:idea_detail", kwargs = {"pk" : idea_id}))


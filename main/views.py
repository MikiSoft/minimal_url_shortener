from django.core.validators import URLValidator
from django.http import response
from django.urls import reverse
import json
from .models import URL


val = URLValidator(schemes=['http', 'https'])


def shorten(request):
    try:
        url = json.loads(str(request.body, encoding='utf-8'))['url']
        val(url)
        obj = URL.objects.get_or_create(original_link=url)
    except:
         return response.HttpResponseBadRequest()
    return response.JsonResponse({
        "short_link": request.build_absolute_uri(reverse("open", args=(obj[0].slug,))),
        "original_link": obj[0].original_link
    }) #status=201 if obj[1] else 200


def open(request, slug):
    try:
        obj = URL.objects.get(slug=slug)
    except:
        return response.HttpResponseNotFound()
    return response.HttpResponseRedirect(obj.original_link, status=301)
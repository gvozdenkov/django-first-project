from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse


monthly_challenges = {
    "january": "this is jan",
    "february": "this is feb",
    "march": "this is march"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid namber :(")

    redirect_month = months[month-1]
    redirect_path = reverse("month_challenge", args=[redirect_month])  # /challenge/1
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        response_data = f"<h1>{challenges_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("no page :(")
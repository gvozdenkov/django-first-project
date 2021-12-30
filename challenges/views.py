from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse


monthly_challenges = {
    "january": "this is jan",
    "february": "this is feb",
    "march": "this is march",
    "april": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenges_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("no page :(")
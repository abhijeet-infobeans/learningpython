from django.shortcuts import render
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


dict_monthly_challenges = {
    "january": "Eat healthy food every day!",
    "february": "Walk 20 minutes on each day for entire month!",
    "march": "Play Bedminton every day!",
    "april": "Go for a swiming class!",
    "may": "Spend 30 min on Yoga classes!",
    "june": "No eating after 8",
    "july": "Do core muscle exercise",
    "august": "read at least 5 pages of a book each day",
    "september": "Challenge enough water drinking!",
    "october": "Clean up your desk before work",
    "november": "Fruits will give us the needed natural vitamins",
    "decemeber": None,
}

# Create your views here.

def index(request):
    months = list(dict_monthly_challenges.keys())
    return render(request, 'challenges/index.html',{
        'months':months
    })
    """
    for month in months:
        capitalize_month = month.capitalize()
        redirect_url = reverse('month-challenge', args=[month])
        str_challenge_list += f'<li><a href="{redirect_url}">{capitalize_month}</a></li>'
    reponse_html = f'<ul>{str_challenge_list}</ul>'
    return HttpResponse(reponse_html)
    """


def monthly_challenge_by_number(request, month):
    try:
        months = list(dict_monthly_challenges.keys())
        'redirect_month = months[month-1]'
        'return HttpResponse(dict_monthly_challenges[redirect_month])'
        redirect_month = months[month-1]
        redirect_url = reverse('month-challenge', args=[redirect_month])
        'return HttpResponseRedirect("/challenges/" + redirect_month)'
        return HttpResponseRedirect(redirect_url)
    except:
        raise Http404()


def monthly_challenge(request, month):
    try:
        challenge_text = dict_monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            'text':challenge_text,
            'month_name': month
            })
    except:
        raise Http404()

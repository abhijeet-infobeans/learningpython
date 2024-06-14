from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import ReviewForm
from . models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView




class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/index.html'
    success_url = '/thank-you'


""" class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/index.html'
    success_url = '/thank-you'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form) """
    

""" class ReviewView(View):
    def get(self, request, *args, **kwargs):
        formReview = ReviewForm()
        return render(request, 'reviews/index.html', {
            'formReview': formReview
        })

    def post(self, request, *args, **kwargs):
        formReview = ReviewForm(request.POST)
        if formReview.is_valid():
            formReview.save()
            return HttpResponseRedirect('/thank-you')

        return render(request, 'reviews/index.html', {
            'formReview': formReview
        }) """


# Create your views here.
""" def index(request):
    if request.method == 'POST':
        formReview = ReviewForm(request.POST)
        if formReview.is_valid():
            # review = Review()
            # review.user_name = formReview.cleaned_data['user_name']
            # review.review_text = formReview.cleaned_data['review_text']
            # review.rating = formReview.cleaned_data['rating']
            formReview.save()
            return HttpResponseRedirect('/thank-you')
    else:
        formReview = ReviewForm()

    return render(request, 'reviews/index.html', {
        'formReview': formReview
    }) """

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'list_review'
    
    """ def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(rating__gt = 3)
        return queryset """


""" class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    
    def get_context_data(self, **kwargs):
        list_review = Review.objects.all()
        context = super().get_context_data(**kwargs)
        context["list_review"] = list_review
        return context """


class SingleReviewView(DetailView):
    model = Review
    template_name = 'reviews/single_review.html'

    
""" class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'
    def get_context_data(self, **kwargs):
        review_id = kwargs['id']
        review = Review.objects.get(pk=review_id)
        context = super().get_context_data(**kwargs)
        context["review"] = review 
        return context """
    
    
# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')
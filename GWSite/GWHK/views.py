from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import jobOpenings, pressRelease, companyNews

# Create your views here.
def home(request):
	comNews = companyNews.objects.order_by('-published_date')[:4]
	context = {'comNews': comNews}
	return render(request, 'GWHK/home.html', context)

def companyInfo(request):
	return render(request, 'GWHK/company_info.html')

def visionValues(request):
	return render(request, 'GWHK/vision_values.html')

def companyCulture(request):
	return render(request, 'GWHK/company_culture.html')

def stockInvest(request):
	return render(request, 'GWHK/stockinvest.html')

class companyNewsDetail(DetailView):
	context_object_name = 'companynews_details'
	model = companyNews

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# context['prev_news'] = self.object.get_previous_by_published_date()
		# context['next_news'] = self.object.get_next_by_published_date()
		return context

class companyNewsList(ListView):
	model = companyNews
	paginate_by = 10

class pressReleaseList(ListView):
	model = pressRelease
	paginate_by = 10

class pressReleaseDetail(DetailView):
	context_object_name = 'pressrelease_details'
	model = pressRelease

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class jobOpeningsList(ListView):
	model = jobOpenings

def contactUs(request):
	return render(request, 'GWHK/contactus.html')
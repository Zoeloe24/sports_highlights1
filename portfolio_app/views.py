from django.shortcuts import render
from .models import Videos, About, Articles

# Create your views here.
def home(request):
    status = 'F'
    featured_videos = Videos.objects.filter(status=status)[:8]
    popular_videos1 = Videos.objects.filter(status='P')[:1]
    popular_videos2 = Videos.objects.filter(status='P')[1:2]
    popular_videos3 = Videos.objects.filter(status='P')[2:3]
    popular_videos4 = Videos.objects.filter(status='P')[3:4]
    popular_videos5 = Videos.objects.filter(status='P')[4:5]

    about_details = About.objects.get()

    latest_articles = Articles.objects.filter(is_published=True).order_by('-posted_on')[:3]

    context = {
        'featured_videos': featured_videos,

        'popular_videos1': popular_videos1,
        'popular_videos2': popular_videos2,
        'popular_videos3': popular_videos3,
        'popular_videos4': popular_videos4,
        'popular_videos5': popular_videos5,

        'about': about_details,

        'latest_articles': latest_articles,
    }
    return render(request, 'index.html', context)

def allFeaturedVideos(request):
    status = 'F'
    all_videos = Videos.objects.filter(status=status)
    about_details = About.objects.get()
    context = {
        'all_videos': all_videos,
        'about': about_details,
    }
    return render(request, 'all_featured_videos.html', context)


def allPopularVideos(request):
    status = 'P'
    all_videos = Videos.objects.filter(status=status)
    about_details = About.objects.get()
    context = {
        'all_videos': all_videos,
        'about': about_details,
    }
    return render(request, 'all_popular_videos.html', context)


def articleDetails(request, pk):
    article_details = Articles.objects.get(id=pk)
    about_details = About.objects.get()
    context = {
        'article_details': article_details,
        'about': about_details,
    }
    return render(request, 'article_details.html', context)

def allArticles(request):
    all_articles = Articles.objects.filter(is_published=True)
    about_details = About.objects.get()
    context = {
        'all_articles': all_articles,
        'about': about_details,
    }
    return render(request, 'all-articles.html', context)


def successPage(request):
    about_details = About.objects.get()
    context = {
        'about': about_details,
    }
    return render(request, 'success_page.html', context)


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import News
from .models import Game
from .models import Member
from .models import Photo
from django.contrib.auth.decorators import login_required
from .forms import MemberForm

def index(request):
    if str(request.user) != "AnonymousUser":
        if Member.objects.all().filter(user=request.user).count() != 1:
            print('creating blog')
            member = Member(user=request.user)
            member.save()
    news_list = News.objects.order_by('-created').all()[:3]
    template = loader.get_template("index.html")
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context,request))

def warmachine_players(request):
    news_list = News.objects.order_by('-created').all()[:3]
    member_list = Member.objects.all()
    template = loader.get_template("warmachine_players.html")
    context = {
        'news_list': news_list,
        'member_list': member_list,
    }
    return HttpResponse(template.render(context,request))

def available_games(request):
    news_list = News.objects.order_by('-created').all()[:3]
    game_list = Game.objects.order_by('title').all()
    template = loader.get_template("available_games.html")
    context = {
        'news_list': news_list,
        'game_list': game_list,
    }
    return HttpResponse(template.render(context,request))

def news(request):
    news_list = News.objects.order_by('-created').all()
    template = loader.get_template("news.html")
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context,request))

def members(request):
    news_list = News.objects.order_by('-created').all()[:3]
    member_list = Member.objects.order_by('-rank').all()
    template = loader.get_template("members.html")
    context = {
        'news_list': news_list,
        'member_list': member_list,
    }
    return HttpResponse(template.render(context,request))

@login_required
def account(request):
    if request.method == 'POST':
        nick = request.POST.get('username')
        faction = request.POST.get('faction')
        member = Member.objects.get(user=request.user.id)

        member.user.username = nick
        member.whFaction = faction
        member.save()

    news_list = News.objects.order_by('-created').all()[:3]
    template = loader.get_template("account.html")
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context,request))


@login_required
def add_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        players = request.POST.get('players')
        game = Game.objects.create(title=title,numberOfPlayers=players,owner=request.user)

        game.save()

    news_list = News.objects.order_by('-created').all()[:3]
    template = loader.get_template("add_game.html")
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context,request))

@login_required
def add_photo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if len(request.FILES) != 0:
            img = request.FILES['img']
            photo = Photo.objects.create(title=title,image=img,author=request.user)

            photo.save()

    news_list = News.objects.order_by('-created').all()[:3]
    template = loader.get_template("add_photo.html")
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context,request))

def photos(request):
    news_list = News.objects.order_by('-created').all()[:3]
    photo_list = Photo.objects.order_by('-created').all()
    template = loader.get_template("photos.html")
    context = {
        'news_list': news_list,
        'photo_list': photo_list,
    }
    return HttpResponse(template.render(context,request))
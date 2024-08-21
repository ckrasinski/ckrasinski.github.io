from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Region, User, Message
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse


# Create your views here.
def index(request):
    regions = Region.objects.all()
    region_object = Region.objects.get(name="pomorskie")
    people = User.objects.filter(region=region_object)
    return render(request, "friender/index.html", {
        "regions": regions,
        "region": region_object,
        "people": people
    })


def show_people(request):
    if request.method == "POST":
        regions = Region.objects.all()
        region = request.POST["region"]
        region_object = Region.objects.get(name=region)
        people = User.objects.filter(region=region_object)
        return render(request, "friender/index.html", {
            "regions": regions,
            "region": region_object,
            "people": people
    })
    else:
        return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "friender/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "friender/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    regions = Region.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["name"]
        picture = request.POST["picture"]
        region_name = request.POST["region"]
        region = Region.objects.get(name=region_name)

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "friender/register.html", {
                "message": "Passwords must match.",
                "regions": regions
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, name=name, region=region,
                                     image=picture)
        except IntegrityError:
            return render(request, "friender/register.html", {
                "message": "Username already taken.",
                "regions": regions
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "friender/register.html", {
            "regions": regions
        })


def show_message(request, id):
    user = User.objects.get(pk=request.user.id)
    friend = User.objects.get(pk=id)
    messages_from = Message.objects.filter(from_who=user, to_who=friend)
    messages_to = Message.objects.filter(from_who=friend, to_who=user)
    all_messages = (messages_from).union(messages_to).order_by("timestamp")
    paginator = Paginator(all_messages, 20)
    page_num = request.GET.get("page")
    messages_of_the_page = paginator.get_page(page_num)
    return render(request, "friender/message.html", {
        "messages": messages_of_the_page,
        "friend": friend,
        "me": user
    })


def send_message(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        friend = User.objects.get(pk=id)
        text = request.POST["content"]
        message = Message(from_who=user, to_who=friend, content=text)
        message.save()
    return HttpResponseRedirect(reverse("message", args=(id,)))


def show_messages(request):
    friends = []
    messages_from = Message.objects.filter(from_who=request.user)
    messages_to = Message.objects.filter(to_who=request.user)
    all_messages = (messages_from).union(messages_to)
    for message in all_messages:
        if message.from_who not in friends:
            friends.append(message.from_who)
        elif message.to_who not in friends:
            friends.append(message.to_who)
    paginator = Paginator(friends, 22)
    page_num = request.GET.get("page")
    friends_of_the_page = paginator.get_page(page_num)
    return render(request, "friender/messages.html", {
        "friends": friends_of_the_page
    })

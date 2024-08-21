from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("show", views.show_people, name="show_people"),
    path("message/<int:id>", views.show_message, name="message"),
    path("sendMessage/<int:id>", views.send_message, name="send_message"),
    path("messages", views.show_messages, name="messages")
]

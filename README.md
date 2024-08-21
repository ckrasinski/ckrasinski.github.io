Project name: Friender
Author: Cezary Krasiński

Description:
------------------------------------------------------

1 Distinctiveness and Complexity:
----------------------------------------
My project is complete new web app to make friends online and eventually meet them in real life.
It's not social network, because it's not like twitter, where you create posts and follow users.
It's web application where you can send messages to people you found online.
My application is more complex than all of projects in this course, because it uses a lot of styles, models,
mechanisms you couldn't find in projects before.

2 Each file:
------------------------------------------

2.1 models.py
--------------
I've created three models: User, Region and Message. User represents every user who created account in my web
application. Region represents region where user lives. Message represents message which user sent to another user.

2.2 views.py
---------------
I've created eight functions: index, show_people, login_view, logout_view, register, show_message, send_message, show_messages. Index renders default application page. Show_people filters users by selected by current user region and shows them. Login_view allows user to log in. Logout_view allow user to log out. Register allows user to register on this web application. Show_message shows messages sent from user to another user and messages from another user to user. Send_message saves sent message to database and renders messages with another user. Show_messages allows user to see all his friends and by clicking on them will be redirected to messages with that user.

2.3 urls.py
---------------
I've created eight paths: "", login, logout, register, show, message/<int:id>, sendMessage/<int:id>, messages. Each of them
renders appropiate function from views.py.

2.4 layout.html
---------------
In this file I've created default layout for the web page and each of templates will inherit from it.

2.5 index.html
---------------
In this file I've created layout for home page. It consists of form where we can choose region and list of people in choosed
region displayed in grid. By default region "pomorskie" is chosen.

2.6 login.html
---------------
In this file I've created form with two inputs: username and password. It also consists of submit button.

2.7 register.html
---------------
In this file I've created form with seven inputs: username, email, password, confirmation, name, picture and region to choose
from list. Name corresponds to name of the user which will be displayed to other users. Picture requires link to image which will be displayed to other users. And this form also have the submit button.

2.8 message.html
---------------
In this file I've created using Django templates list of messages which user sent to one of his friends and messages from friend to user sorted in chronological order. Messages from friend are displayed in green background. Each message have also image of user who sent it on the left. The file also have a form to sent new message of friend. This template uses pagination.

2.9 messages.html
---------------
This file displays list of current user's friends with image and name showed in grid. This template uses pagination.

2.10 styles.css
---------------
In this file I've created styles for entire application.

3 How to run:
------------------------------------------
To run this application you go to the project main directory and run command python manage.py runserver.

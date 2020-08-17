# Discord-Polling-Bot

This is a discord polling bot where multiple users can create mass polls at once.
This bot has one extra feature that is to create a mass poll which means to creat a poll of lots of questions at once.

What is the use?
Well, To be very honest, I created this bot to cheat in online tests :) lol, by converting all the questions from the test form to a discord poll bot where me and friends can vote answers. 
We didn't use voice chat because lots of people speak at once and no one can understand anything.

How to use it?
First of all you have to change the token in pbot.py with your token
Then make pbot.py alive by going to discord developers site (you can google how to do that)
now add the bot to your server

To create the poll, you have to send a command message:
?poll;Enter your Question here; Enter option 1; Enter option 2;

Simple right :)

But in order to make mass poll you will need something that is quicker for a test
So I created a poller.py file which can take questions and options and output the commands to execute them on discord. Now you don't have to write the commands

But it was still slower to make many questions in a test
So i decided to give it a multi-user (6 users max) support so that work can be divided
Now Me and my friends can make parts of the test form so that one person doesn't have to do all the work of adding questions

for this i created boom.py and boom.exe which does the same thing. It takes different boom numbers through which they can create their own part of the form.
for example;
boom1 creates first 5 questions
boom2 creates next 5 and so on .. till boom 6

now on discord we can add any part of the form; like ?boom1 for first 5 questions.. and boom2 for next five questins
In this way we divide the work of coping pasting questions and no one wastes much of their time and everyone gets the benefit by voing the answers.

Please don't tell my TEACHER !! SHHHHH

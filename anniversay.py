import pyttsx3
engine = pyttsx3.init()
engine.say("WELCOME")
engine.runAndWait()
print("WELCOME")
print()
engine.setProperty('rate', 150)
#engine.setProperty('volume', 0.7)
engine.say("Hope you'll remember this day forever! Let's go on a quick ride.")
engine.say("Before that here's a heart for you two")
engine.runAndWait()

from turtle import *
color("red", "pink")
begin_fill()
left(50)
forward(100)
circle(40,180)
left(260)
circle(40,180)
forward(100)
end_fill()
done()

engine.setProperty('rate', 150)
engine.say("Hope you are happy and excited from here.")
engine.runAndWait()


#------Quiz game-------

import random
print()
Papa = input("What is Male Partner's name? ")
Mummy = input("What is Female Partner's name? ")

engine.say("Good Luck " + str(Papa) + " " + str(Mummy) + ". Let's see who wins!")
print("Good Luck " + str(Papa) + " " + str(Mummy) + ". Let's see who wins!")
engine.runAndWait()


di = {1: "Favourite Show",
      2: "Favourite Color",
      3: "Money or Fame?",
      4: "what were you doing at my age?",
      5: "After getting married ever wished 'single hi rehte yaar' "}

possible_ans = {"Favourite Show" : ["tmkuc", "did"],
                "Favourite Color" : ["white", "green"],
                "Money or Fame?" : ["money", "fame"],
                "what were you doing at my age?" : ["study", "cook"],
                "After getting married ever wished 'single hi rehte yaar' ": ["yes", "yes"]}


round = 3
cnt1 = 0
cnt2 = 0
i=0
p=1
j=0
while p>0:
  engine.say("Starting with " + str(Mummy) + " to answer " + str(Papa) + "'s Questions")
  engine.runAndWait()
  print("Starting with " + str(Mummy) + " to answer " + str(Papa) + "'s Questions")
  while i<round:
      print(di)
      engine.say(str(Papa) + " choose a number from given dictionary")
      engine.runAndWait()
      person1_choice = int(input(str(Papa) + " choose a number(1,2,3,4,5): "))
      if person1_choice in di.keys():
            print(di[person1_choice] + " of " + str(Papa))
            engine.say(str(Mummy) + " enter your answer: ")
            engine.runAndWait()
            person2_choice = input(str(Mummy) + " enter your answer: ")
            if person2_choice.lower() == possible_ans[di[person1_choice]][0]:
                  print("yes you are correct!")
                  engine.say("yes you are correct!")
                  engine.runAndWait()
                  cnt2 = cnt2 + 1
            else:
                  print("uh oh! Incorrect")
                  engine.say("uh oh! Incorrect")
                  engine.runAndWait()
      i += 1

  print()
  engine.say("Aha, now it's " + str(Papa) +  "'s turn to answer " + str(Mummy) + "'s Questions")
  engine.runAndWait()
  print("Aha, now it's " + str(Papa) +  "'s turn to answer " + str(Mummy) + "'s Questions")

  while j<round:
       print(di)
       engine.say(str(Mummy) + " choose a number from given dictionary")
       engine.runAndWait()
       person2_choice = int(input(str(Mummy) + " choose a number(1,2,3,4,5): "))
       if person2_choice in di.keys():
             print(di[person2_choice] + " of " + str(Mummy))
             engine.say(str(Papa) + " enter your answer: ")
             engine.runAndWait()
             person1_choice = input(str(Papa) + " enter your answer: ")
             if person1_choice.lower() == possible_ans[di[person2_choice]][1]:
                   print("yes you are correct!")
                   engine.say("yes you are correct!")
                   engine.runAndWait()
                   cnt1 = cnt1 + 1
             else:
                   print("uh oh! Incorrect")
                   engine.say("uh oh! Incorrect")
                   engine.runAndWait()
       j +=1

  n = input("Enter any number to abort the game: ")
  if n.isdigit():
      break

print()
engine.say("Score Time!!!")
engine.runAndWait()
print("Score Time!!!")

print("Score of " +str(Papa)+ " is " +str(cnt1))
engine.say("Score of " +str(Papa)+ " is " +str(cnt1))
engine.runAndWait()
print("Score of " +str(Mummy)+ " is " +str(cnt2))
engine.say("Score of " +str(Mummy)+ " is " +str(cnt2))
engine.runAndWait()

print()
if cnt1 > cnt2:
    print("Hurray! {} is the man of the match".format(Papa))
    engine.say("Hurray! {} is the man of the match".format(Papa))
    engine.runAndWait()
elif cnt1 == cnt2:
    print("Love Birds! Winner Winner chicken dinner")
    engine.say("Love Birds! Winner Winner chicken dinner")
    engine.runAndWait()
else:
    print("Noice! {} is the Superwomen yayyyy".format(Mummy))
    engine.say("Noice! {} is the Superwomen yayyyy".format(Mummy))
    engine.runAndWait()

#----frame showing happy annv.-----

print("HAPPY MARRIAGE ANNIVERSARY MUMMY PAPA")
from tkinter import *
import tkinter.font as tkfont
from PIL import  ImageTk, Image
t= Tk()
t.geometry("600x600")
t.resizable(0,0)
#global variable
fontStyle = tkfont.Font(family="Impact", size=15)

# def speak(text):
#     engine.setProperty("rate", 150)
#     engine.say(text)
#     engine.runAndWait()



def home():
    f0 = Frame(bg="sky blue")
    f0.place(x=0, y=0, width=600, height=600)
#local variable
    engine.say("Welcome again my lovebirds")
    engine.runAndWait()
    u0 = Label(f0, text="WELCOME MY LOVEBIRDS", fg="white", bg="pink", font=fontStyle)
    u0.place(x=100, y=70)
    engine.say("HAPPY MARRIAGE ANNIVERSARY MUMMY PAPA")
    engine.runAndWait()
    u1 = Label(f0, text="HAPPY MARRIAGE ANNIVERSARY MUMMY PAPA", fg="white", bg="pink", font=fontStyle)
    u1.place(x=70, y=150)

    b0 = Button(f0, text="Mummy",command=mummy)
    b0.place(x=80, y=300, width=120, height="40")

    b1 = Button(f0, text="Papa", command=papa)
    b1.place(x=300, y=300, width=120, height="40")

def mummy():
    f1 = Frame(bg="sky blue")
    f1.place(x=0, y=0, width=600, height=600)

    u2 = Label(f1, text="Thank you for being an amazing mother! Love Love", fg="white", bg="pink", font=fontStyle)
    u2.place(x=100, y=80)
    engine.say("Thank you for being an amazing mother! Love Love")
    engine.runAndWait()

    b2 = Button(f1, text="HOME", command=home)
    b2.place(x=0, y=0, width=120, height="40")

def papa():
    f2 = Frame(bg="sky blue")
    f2.place(x=0, y=0, width=600, height=600)

    u3 = Label(f2, text="Thank you for being an amazing Father! Love Love", fg="white", bg="pink", font=fontStyle)
    u3.place(x=100, y=80)
    engine.say("Thank you for being an amazing Father! Love Love")
    engine.runAndWait()

    b3 = Button(f2, text="HOME", command=home)
    b3.place(x=0, y=0, width=120, height="40")

home()
t.mainloop()

from tkinter import *
import random
from tkinter import messagebox
from functools import partial
import string

root = Tk()
root.geometry("800x500")
root.resizable(height=False,width=False)
root.title("Hangman")
root.configure(background="white")

frame1=Frame(root,background="white")
frame2=Frame(root,background="white")

frame1.pack(side="top")
frame2.pack(side="bottom")

words=["PEOPLE","JUNCTION","LOCATION","APPLE","BANANA","SECTION","FUNCTION","CLASS","MEASURE","IDENTITY"]
buttons=[]
blanks=[]
photos=[]
get_guessed_letters=[]
save_correct_guesses=[]

chances=0
check=0

guess_letter=""
show_word=""
word_outline=""
comments=""

show_word_variable=StringVar()
show_comments=StringVar()

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


photo0=PhotoImage(file='0.png')
photo1=PhotoImage(file='1.png')
photo2=PhotoImage(file='2.png')
photo3=PhotoImage(file='3.png')
photo4=PhotoImage(file='4.png')
photo5=PhotoImage(file='5.png')
photo6=PhotoImage(file='6.png')
photo7=PhotoImage(file='7.png')
photo8=PhotoImage(file='8.png')
photo9=PhotoImage(file='9.png')
photo10=PhotoImage(file='10.png')


word=random.choice(words)
blanks.extend(word)

for i in range(len(blanks)):
		blanks[i]="_"

show_word_variable.set(blanks)


def get_guess(character,index_num):
	global guess_letter,get_guessed_letters
	buttons[index_num].configure(state=DISABLED)
	get_guessed_letters.append(character)
	guess_letter=character
	print_guessed_letter()
	comment_function(guess_letter)
	reveal_letters(guess_letter)


def comment_function(character):
	show_comments.set("Enter Your Guess")
	for i in range(len(word)):
		if(character==word[i]):
			show_comments.set("Your guess is Correct!")
			break
		else:
			show_comments.set("OOPS! Try another one")


def reveal_letters(character):
	global show_word_variable,blanks,chances,get_guessed_letters,save_correct_guesses
	check=0
	if character in word:
		for i in range(len(word)):
			if word[i]==character:
				blanks[i]=character
				save_correct_guesses.append(character)
		x=' '.join(blanks)
		show_word_variable.set(x)
		if(len(blanks)==len(save_correct_guesses)):
			messagebox.showinfo("Congrats","Y O U  W O N")
			
				
	else:
		chances=chances+1
		change_image(chances)
		show_word_variable.set(blanks)
		if(chances==10):
			messagebox.showwarning("HANGED!!!!","G A M E O V E R")
			show_word_variable.set(word)

def change_image(chance):
	if(chances==1):
		image_label.configure(image=photo1)
	if(chances==2):
		image_label.configure(image=photo2)
	if(chances==3):
		image_label.configure(image=photo3)
	if(chances==4):
		image_label.configure(image=photo4)
	if(chances==5):
		image_label.configure(image=photo5)
	if(chances==6):
		image_label.configure(image=photo6)
	if(chances==7):
		image_label.configure(image=photo7)
	if(chances==8):
		image_label.configure(image=photo8)
	if(chances==9):
		image_label.configure(image=photo9)
	if(chances==10):
		image_label.configure(image=photo10)

def print_guessed_letter():
		global word_outline,show_word,guess_letter,comments
		show_word=word_outline
		show_word_variable.set(show_word)


alphbet_count=0

for i in range(2):
	for j in range(13):
		letter=alphabet[alphbet_count]
		buttons.append(Button(frame2,text=letter,relief="flat",width=6,height=2,bg="white",fg="red",command=partial(get_guess,letter,alphbet_count)))
		buttons[alphbet_count].grid(row=i,column=j)
		alphbet_count+=1


print_label=Label(frame1,textvariable=show_word_variable,bg="white",font=(None,25))
print_label.grid(row=0,column=2)
print_label2=Label(frame1,textvariable=show_comments,font=(None,12),bg="white")
print_label2.grid(row=1,columnspan=2)
image_label=Label(frame1,image=photo0,justify="left")
image_label.grid(row=0,column=0)
root.mainloop()
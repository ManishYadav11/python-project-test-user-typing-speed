from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random
root= Tk()
root.geometry("700x500")    #Window Size
root.configure(bg="Black")
root.title(' Typing Speed Test')

window = Tk()
window.title(' Typing Speed Test  ')
window.geometry("1400x700")
window.withdraw()


hs_file = open('highscore.txt', 'r+')
x=0


def game():
 
    global x
    if x == 0:

        root.withdraw()
        x= x+1
    window.deiconify()

    def check_result():

        j=error=0
        answer=entry.get("1.0","end-1c")
        end = timer()
        time_taken=end-start
        #len diff
        if len(words[word])>=len(answer):

            error=len(words[word])-len(answer)
            for i in answer: #take shorter sentence

                if i == words[word][j]:
                    pass
                else:
                    error+=1
                j+=1
        elif len(words[word])<=len(answer):
            error=len(answer)-len(words[word])
            for i in words[word]:
                if i==answer[j]:
                    pass
                else:
                    error+=1
                j+=1
        wpm = len(answer)/5
        wpm = wpm-error
        wpm=int(wpm/(time_taken/60))
        hs_file.seek(0)
        line = int(hs_file.readline())
        if wpm>line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result="Amazing! Your new highscore is: "+str(wpm)+" WPM"
            messagebox.showinfo("Score", result)
        else:
            result="Your score is: "+str(wpm)+" WPM\nBetter luck next time!"
            messagebox.showinfo("Score", result)
    def finish():
        hs_file.close() 
        window.destroy()
        root.destroy()
    
    words = ["Python is a interpreting programming language" ,"welcome to python"]
    word = random.randint(0, (len(words)-1))

    x2 = Label(window, text=words[word], bg="black", fg="white", height=8, width=100, font="times 20"  )
    x2.place(x=15, y=10)

    x3 = Button(window, text="Submit", font="times 20", bg="#fc2828", command=check_result)
    x3.place(x=650, y=520)

    entry= Text(window)
    entry.place(x=100, y=300, height=200, width=1200)

    b2 = Button(window, text="Done", font="times 13", bg='#ffc003', width=12, command=finish)
    b2.place(x=300, y=550)
    
    b3 =Button(window, text="Try Again", font="times 13", bg='#ffc003', width=12, command=game)
    b3.place(x=1000, y=550)

    start= timer()
    window.mainloop()


x1 = Label(root, text="Let's test your typing speed!", bg="black", fg="white", font="times 35")
x1.place(x=100, y=50)

b1 = Button(root, text="Go!", width=25, bg="red", font="times 20", command=game)
b1.place(x=150, y=120)

hs_text = Label(root, text="Highscore", width=20, bg='#03fcf8', font="times 35")
hs_text.place(x=90, y=240)

hs = int(hs_file.readline()) 
hs_val = Label(root, text=str(hs)+" WPM", width=20, fg="yellow", bg='black', font="times 35")
hs_val.place(x=110, y=320)
root.mainloop()
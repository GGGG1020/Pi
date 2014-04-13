import tkinter
import tkinter.ttk
import pickle
import math
import itertools
import fractions
import platform
currentSYS=platform.platform()
print(currentSYS)
cache=dict()  
def calculate_pi(nth,out,error,win,cache):
    stats=tkinter.ttk.Label(Fram, text="Working.....", font=("Comic Sans MS", 13,"normal"),background="green")
    stats.place(x=150,y=600)
    try:
        nth=int(nth)
        error1=False
    except ValueError as err:
          errwin=tkinter.Tk()
          b=tkinter.ttk.Style(errwin)
          b.configure('Err.TButton', background="green", font=("Comic Sans MS", 13, "normal"))
          errwin.geometry("300x100")
          errwin.title('Error')
          errwin.resizable(False, False)
          errwin.configure(background="green")
          errtext=tkinter.ttk.Label(errwin, text="   Please enter a nonzero integer", font=("Comic Sans MS", 13,"bold"), background='green', foreground='red')
          errtext.pack()
          errbutton=tkinter.ttk.Button(errwin, text="Okay", style="Err.TButton", command=lambda:errwin.destroy())
          errbutton.pack()
          nth=1
          error1=True
    if not nth in cache and not error1:
        current_sum=float(4/1)
        current_val=int()
        curren_pack=int()
        current_sign=str("-")
        curr_str="4/1"
        num,den=curr_str.split("/")
        Newden=str(int(den)+2)
        limit=int(den)
        current_val_str="4/"+str(Newden)
        print(current_val_str)
        current_val=float(4/int(Newden))
        current_str=str(current_val)
        for i in range(nth):        
            if current_sign==str("+"):
                current_sum=current_sum+current_val
                current_sign="-"
                num,den=current_val_str.split("/")
                Newden=str(int(den)+2)
                limit=int(den)
                current_val_str="4/"+str(Newden)
                print(current_val_str)
                current_val=float(4/int(Newden))
                current_str=str(current_val)
            else:
                current_sum=current_sum-current_val
                current_sign=str("+")
                num,den=current_val_str.split("/")
                Newden=str(int(den)+2)
                limit=int(den)
                current_val_str="4/"+str(Newden)
                print(current_val_str)
                current_val=float(4/int(Newden))
                current_str=str(current_val)
        cache[nth]=current_sum
    elif nth in cache:
        current_sum=cache[nth]
    elif error1:
        pass
    if not error1:
        out.configure(text=current_sum)
        out.pack()
        error.config(text=(abs(math.pi-current_sum)))
        error.pack()
win=tkinter.Tk()
s=tkinter.ttk.Style(win)
s.configure('Pi.TButton', background="green",font=("Comic Sans MS", 11, "normal"))
a=tkinter.ttk.Style(win)
a.configure("Frame.TFrame", background='green', foreground='green')
win.title("Pi")
win.configure(background="green")
win.geometry("400x500")
text1_str=str("Sum")
text1_str
Fram=tkinter.ttk.Frame(win,style='Frame.TFrame')
text1=tkinter.ttk.Label(Fram, text=text1_str, font=("Comic Sans MS", 13,"normal"),background="green")
text1.pack()
nth=tkinter.ttk.Entry(Fram,width=4)
nth.pack()
text2=tkinter.ttk.Label(Fram,text="terms to get pi",  font=("Comic Sans MS", 13,"normal"),background="green")
text2.pack()
Out=tkinter.ttk.Label(win,font=("Comic Sans MS", 16, "normal"),background='green')
Error=tkinter.ttk.Label(win, font=("Comic Sans MS", 13, "bold"), background="green", foreground="red")
goButton=tkinter.ttk.Button(Fram,text="Go!",style='Pi.TButton',command=lambda:calculate_pi(nth.get(),Out,Error,win,cache))
goButton.pack()
Fram.pack()
result_fram=tkinter.ttk.Frame(win)
result_fram.pack()
Quit=tkinter.ttk.Button(win, text="Quit", style='Pi.TButton', command=lambda:win.destroy())
Quit.pack()
win.mainloop()

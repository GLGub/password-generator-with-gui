import secrets
import string
import random
import tkinter as tk

def pw_get(x):
    pword = "".join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range((x))))
    randpword=list(pword)
    random.shuffle(randpword)
    textbox_update((''.join(randpword)))
    
def tocopy():
    window.clipboard_clear()
    window.clipboard_append(pw_box.get('1.0', tk.END))

def textbox_update(pw):
    pw_box.config(state="normal")
    pw_box.delete("0.0", "end")
    pw_box.insert('end',pw)
    pw_box.config(state="disabled")

#TKinter window below
window=tk.Tk()
window.title("The Password Generator")
window.geometry('500x120')
window.resizable(False,False)
window.configure(bg='#30becf')

plabel=tk.Label(window,text="Password Length",height=1,bg='#30becf').grid(row=0,column=0,padx=20)
#Slider
slideval=tk.IntVar()
slider = tk.Scale(window,from_=4,to=32,orient='horizontal',variable=slideval,length=200,bg='#30becf')
slider.grid(row=0,column=1)

button_generate=tk.Button(window,text="Generate A Password",
                          command=lambda : pw_get(slideval.get()),height=2,bg='#30becf').grid(row=0,column=2,padx=10,pady=10)

#textbox part
pw_box=tk.Text(window,height=1,width=10)
pw_box.grid(row=2,column=1,sticky='we',columnspan=2,padx=10,pady=10)
pw_box.config(state="disabled")

button_copy=tk.Button(window,text="Copy",command=tocopy).grid(row=2,column=0)


window.mainloop()
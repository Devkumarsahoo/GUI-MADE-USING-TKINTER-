from tkinter import*

window=Tk()

##def greet():
##    hello="hello " +str(inp_1.get())
##    label_2=Label(window,text=hello)
##    label_2.pack()
##
##inp_1=Entry()
##inp_1.pack()
##inp_1.insert(0,"enter ur name")
##
##button_1=Button(window,text="Enter the name",command=greet)
##button_1.pack()
entry_1=Entry(window)
entry_1.grid(row=0,column=0,padx=30,pady=33)

def on_clear():
    
    entry_1.delete(0,END)
    
def on_add():
    first_number=entry_1.get()
    global fnum
    global flag
    flag="addition"
    fnum=int(first_number)
    entry_1.delete(0,END)


def on_sub():
    first_number=entry_1.get()
    global fnum
    global flag
    flag="substraction"
    fnum=int(first_number)
    entry_1.delete(0,END)

def on_mul():
    first_number=entry_1.get()
    global fnum
    global flag
    flag="multiplication"
    fnum=int(first_number)
    entry_1.delete(0,END)

def on_div():
    first_number=entry_1.get()
    global fnum
    global flag
    flag="division"
    fnum=int(first_number)
    entry_1.delete(0,END)



def on_equal():
    if flag=="addition":
        second_number=entry_1.get()
        entry_1.delete(0,END)
        entry_1.insert(0,int(second_number)+int(fnum))
    if flag=="substraction":
        second_number=entry_1.get()
        entry_1.delete(0,END)
        entry_1.insert(0,int(second_number)-int(fnum))
    if flag=="multiplication":
        second_number=entry_1.get()
        entry_1.delete(0,END)
        entry_1.insert(0,int(second_number)*int(fnum))
    if flag=="division":
        second_number=entry_1.get()
        entry_1.delete(0,END)
        entry_1.insert(0,int(second_number)/int(fnum))

    
def on_click(number):
    current=entry_1.get()
    entry_1.delete(0,END)
    entry_1.insert(0,str(current)+str(number))



window.title("DEV CALCULATOR")


button_1=Button(window,text="1",padx=33,pady=33,command=lambda:on_click(1))
button_2=Button(window,text="2",padx=33,pady=33,command=lambda:on_click(2))
button_3=Button(window,text="3",padx=33,pady=33,command=lambda:on_click(3))
button_4=Button(window,text="4",padx=33,pady=33,command=lambda:on_click(4))
button_5=Button(window,text="5",padx=33,pady=33,command=lambda:on_click(5))
button_6=Button(window,text="6",padx=33,pady=33,command=lambda:on_click(6))
button_7=Button(window,text="7",padx=33,pady=33,command=lambda:on_click(7))
button_8=Button(window,text="8",padx=33,pady=33,command=lambda:on_click(8))
button_9=Button(window,text="9",padx=33,pady=33,command=lambda:on_click(9))
button_0=Button(window,text="0",padx=33,pady=33,command=lambda:on_click(0))

button_add=Button(window,text="+",padx=33,pady=33,command=on_add)
button_equal=Button(window,text="=",padx=33,pady=33,command=on_equal)
button_clear=Button(window,text="AC",padx=33,pady=33,command=on_clear)
button_sub=Button(window,text="-",padx=33,pady=33,command=on_sub)
button_mul=Button(window,text="*",padx=33,pady=33,command=on_mul)
button_div=Button(window,text="/",padx=33,pady=33,command=on_div)                  

button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=3)

button_4.grid(row=2,column=1)
button_5.grid(row=2,column=2)
button_6.grid(row=2,column=3)


button_7.grid(row=1,column=1)
button_8.grid(row=1,column=2)
button_9.grid(row=1,column=3)

button_0.grid(row=4,column=1)
button_add.grid(row=4,column=2)
button_equal.grid(row=4,column=3)
button_clear.grid(row=5,column=1)
button_sub.grid(row=5,column=2)
button_mul.grid(row=5,column=3)
button_div.grid(row=6,column=1)

window.mainloop()

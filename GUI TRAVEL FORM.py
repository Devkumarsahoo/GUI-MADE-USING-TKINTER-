from tkinter import *
import sqlite3

window=Tk()



window.geometry("400x400")

details=Label(window,text="Welcome to DEV TRAVELS")
details.grid(row=0,column=0)



name=Label(window,text="NAME")
name.grid(row=1,column=0)


name=Label(window,text="PHONE")
name.grid(row=2,column=0)


name=Label(window,text="GENDER")
name.grid(row=3,column=0)

name=Label(window,text="PAYMENT")
name.grid(row=4,column=0)

##

name_entry=Entry(window)
name_entry.grid(row=1,column=1)


phone_entry=Entry(window)
phone_entry.grid(row=2,column=1)

gender_entry=Entry(window)
gender_entry.grid(row=3,column=1)

payment_entry=Entry(window)
payment_entry.grid(row=4,column=1)

def getdata():
    conn=sqlite3.connect('travel_book.db')
    c=conn.cursor()
    
    c.execute(""" CREATE TABLE data(
                name text,
                phone integer,
                gender text,
                payment text
              )""")

    conn.commit()
    conn.close()




   

## BUTTON

submit=Button(window,text="SUBMIT",command=getdata)
submit.grid(row=5,column=1)

window.mainloop()


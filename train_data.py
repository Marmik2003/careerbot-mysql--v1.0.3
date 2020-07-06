from tkinter import *
from tkinter import messagebox
import mysql.connector as mscon
from functools import partial

cbdb = mscon.connect(host="localhost", user="careerbot", passwd="1234", database="careerbot_response")
cbcur = cbdb.cursor()


def insertdata(inpt, otpt):

    inputdata = "\""+inpt.get()+"\""
    outputdata = '"'+otpt.get()+'"'
    try:
        sql = "INSERT INTO res_table (input,output) VALUES (%s, %s)" %(inputdata, outputdata)
        cbcur.execute(sql)
        cbdb.commit()
        messagebox.showinfo(title="Success", message="Data Inserted Successfully")
    except:
        messagebox.showerror(title="ERROR",message="SOMETHING WENT WRONG")


tkWindow = Tk()
tkWindow.geometry('400x100')
tkWindow.title('Train Response Data')


inptLabel = Label(tkWindow, text="Input").grid(row=0, column=0)
inpt = StringVar()
inptEntry = Entry(tkWindow, textvariable=inpt).grid(row=0, column=1)


otptLabel = Label(tkWindow, text="Output").grid(row=1, column=0)
otpt = StringVar()
otptEntry = Entry(tkWindow, textvariable=otpt).grid(row=1, column=1)

insertdata = partial(insertdata, inpt, otpt)


loginButton = Button(tkWindow, text="Save", command=insertdata).grid(row=2, column=0)

tkWindow.mainloop()

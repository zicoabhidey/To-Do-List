#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:29:53 2021

@author: zico
"""
from tkinter import *
from tkinter import messagebox as mb

"""
functions:
    Append a new task
    Delete a specific task
    Delete all task
"""
tasks = []
def addNewTask():
    #input from tkinter Entry
    newTask = entryBox.get()
    if newTask != "":
        tasks.append(newTask)
        listBox.insert(END, newTask)
        entryBox.delete(0, "end")
    else:
        #tkinter messagebox
        mb.showwarning("warning", "Please enter some task.")
     
def deleteSpecificTask():
    #tkinter messagebox
    messageBox = mb.askyesno('Delete All','Are you sure?')
    if messageBox==True:
        listBox.delete(ANCHOR)
          
def deleteAllTask():
    #tkinter messagebox
    messageBox = mb.askyesno('Delete All','Are you sure?')
    if messageBox==True:
        while(len(tasks)!=0):
            tasks.pop()
            listBox.delete(0,'end')
"""
GUI:
    Need a Listbox to show tasks
    Create a Scrollbar to scroll the tasks
    Create a Entry to fetch new task
    Create 3 buttons Add new task, Delete Specific tasks and delete all tasks
"""
window = Tk()
window.geometry('750x500')
window.title('TO DO LIST')
window.config(bg='#999966')
window.resizable(width=False, height=False)
#Adding message to window
var = StringVar()
label = Label(window, textvariable=var, relief=RAISED )
var.set("Task will show up in the below window")
label.pack()

#Create a frame
frame = Frame(window)
frame.pack(pady=10)

#Create Listbox in frame
listBox = Listbox(frame, 
                  width=30, 
                  height=10, 
                  font=('Helvetica', 12), 
                  bd=0, 
                  fg='#464646',
                  highlightthickness=0,
                  selectbackground='#3399ff',
                  activestyle="none",
)

listBox.pack(side=LEFT, fill=BOTH)
#Add tasks to Listbox
for task in tasks:
    listBox.insert(END, item)
    
#Add scrollbar in frame  
scrollBar = Scrollbar(frame)
scrollBar.pack(side=LEFT, fill=BOTH)
#Adding scrollbar to listBox
listBox.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)

#Adding message to window
var = StringVar()
label = Label(window, textvariable=var, relief=RAISED )
var.set("Enter your task in the textfield")
label.pack()

#Create an entry
entryBox = Entry(
    window,
    font=('Helvetica', 24)
    )
entryBox.pack(pady=10)

#Create frame for buttons within window
buttonFrame = Frame(window)
buttonFrame.pack(pady=20)

#Create a button for adding new task         
addTaskButton = Button(
    buttonFrame,
    text='Add Task',
    font=('Courier 14'),
    bg='#66ff33',
    padx=0,
    pady=0,
    command=addNewTask
)

addTaskButton.pack(fill=BOTH, expand=False, side=TOP)
#Create a button for delete specific task
deleteTaskButton = Button(
    buttonFrame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff3300',
    padx=0,
    pady=0,
    command=deleteSpecificTask
)

deleteTaskButton.pack(fill=BOTH, expand=True, side=TOP)
#Create a button for deleting all task
deleteAllTaskButton = Button(
    buttonFrame,
    text='Delete All Task',
    font=('times 14'),
    bg='#ff3300',
    padx=0,
    pady=0,
    command=deleteAllTask
)

deleteAllTaskButton.pack(fill=BOTH, expand=True, side=TOP)

#hold the screen
window.mainloop()
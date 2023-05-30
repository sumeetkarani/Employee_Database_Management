from tkinter import *
import backend
import re

def viewcommand():
    """
    It deletes all the items in the listbox, then inserts the rows returned by the view() function in
    the backend.py file.
    """
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def searchcommand():
    """
    It deletes all the items in the listbox, then inserts the results of the search function into the
    listbox.
    """
    list1.delete(0,END)
    for row in backend.search(name_text.get(),department_text.get(),identity_text.get(),Salary_text.get()):
        list1.insert(END,row)

def add_command():
    """
    It takes the data from the entry boxes and passes it to the backend.insert function
    """
    if Name.get()=="" or Department.get()=="" or Identity.get()=="" or Salary.get()=="":
        errormessage("(All fields are required)")
    elif len(re.findall("^\d{6}$",identity_text.get()))==0:
        errormessage("Employee ID")
    elif len(re.findall("\d+", Salary_text.get()))==0:
        errormessage("Price")
    elif len(re.findall("^[a-zA-Z0-9 ]*$", department_text.get()))==0:
        errormessage("Department")
    elif len(re.findall("^[a-zA-Z0-9 ]*$", name_text.get()))==0:
        errormessage("Name")
    
    
    else:
        backend.insert(name_text.get(),department_text.get(),identity_text.get(),Salary_text.get())
        list1.delete(0,END)
        list1.insert(END,"Press View all to see the new entry")
        viewcommand()

def get_selected_row(event):
    """
    It gets the selected row from the listbox and inserts the values into the entry boxes
    """
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        
        Name.delete(0,END)
        Name.insert(END,selected_tuple[1])

        Department.delete(0,END)
        Department.insert(END,selected_tuple[2])

        Identity.delete(0,END)
        Identity.insert(END,selected_tuple[3])

        Salary.delete(0,END)
        Salary.insert(END,selected_tuple[4])
    except IndexError:
        pass
    

def delete_command():
    """
    It deletes the selected tuple from the database
    """
    try:
        backend.delete(selected_tuple[0])
        Name.delete(0,END)
        Department.delete(0,END)
        Identity.delete(0,END)
        Salary.delete(0,END)
        viewcommand()
    except NameError:
        errormessage("(No field selected)")

def update_command():
    # Updating the selected tuple in the database and then calling the viewcommand() function to
    # update the listbox.
    try:
        if len(re.findall("^\d{6}$",identity_text.get()))==0:
            errormessage("Employee ID")
        elif len(re.findall("\d+", Salary_text.get()))==0:
            errormessage("Salary")
        elif len(re.findall("^[a-zA-Z0-9 ]+$", department_text.get()))==0:
            errormessage("Department")
        elif len(re.findall("^[a-zA-Z0-9 ]+$", name_text.get()))==0:
            errormessage("Name")
        else:
            backend.update(selected_tuple[0],name_text.get(),department_text.get(),identity_text.get(),Salary_text.get())
            viewcommand()
    except NameError:
        errormessage("(No field selected)")
    
def errormessage(error_field):
    '''Error fo'''
    error=Tk()
    error.wm_title("Error")
    error_lable = Label(error,text=f"Invalid {error_field}")
    error_lable.grid(row=1,column=0)
    error.mainloop()

window=Tk()
window.configure(bg='#7393b3')

window.wm_title("Company Database")

Name_Label=Label(window,text="Name",bg="#c0e8eb")
Name_Label.grid(row=0,column=0)

Department_Label=Label(window,text="Department",bg="#c0e8eb")
Department_Label.grid(row=0,column=2)

Identity_Label=Label(window,text="Employee ID",bg="#c0e8eb")
Identity_Label.grid(row=1,column=0)

Salary_Label=Label(window,text="Salary",bg="#c0e8eb")
Salary_Label.grid(row=1,column=2)


name_text=StringVar()
Name=Entry(window,textvariable=name_text)
Name.grid(row=0,column=1)


department_text=StringVar()
Department=Entry(window,textvariable=department_text)
Department.grid(row=0,column=3)


identity_text=StringVar()
Identity=Entry(window,textvariable=identity_text)
Identity.grid(row=1,column=1)


Salary_text=StringVar()
Salary=Entry(window,textvariable=Salary_text)
Salary.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=1,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6,)

# Binding the scrollbar to the listbox.
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

view_button=Button(window,text="View all",width=12,command=viewcommand,bg="#c0e8eb")
view_button.grid(row=2,column=0)


search_button=Button(window,text="Search Entry",width=12,command=searchcommand,bg="#c0e8eb")
search_button.grid(row=3,column=0)


add_button=Button(window,text="Add Entry",width=12,command=add_command,bg="#c0e8eb")
add_button.grid(row=4,column=0)


update_button=Button(window,text="Update",width=12,command=update_command,bg="#c0e8eb")
update_button.grid(row=5,column=0)


delete_button=Button(window,text="Delete",width=12,command=delete_command,bg="#c0e8eb")
delete_button.grid(row=6,column=0)


exit_button=Button(window,text="Close",width=12,command=window.destroy,bg="#c0e8eb")
exit_button.grid(row=7,column=0)
window.mainloop()
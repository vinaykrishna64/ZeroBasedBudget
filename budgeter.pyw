import os
import sys
import datetime
import Bugdet_functions as B0
from tkinter import *
from tkinter.ttk import Notebook, Entry
from tkinter import ttk
## get this year and month

current_time = datetime.datetime.now()  
time = str(current_time)
global year, month
year = time[0:4]
month = time[5:7]
B0.make_folder('DATA')
#check for current months folder and create if it doesn't exist
B0.current_month_folders(year,month)

CATEGORIES = ['Food', 'Utilities', 'Travel' ,'Entertainment', 'Subscriptions', 'Clothing', 'Miscellaneous']


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# GUI

window = Tk()
window.title("My Zero Based Budget")
window.geometry("900x900")



def update_app(flag = 0):

    if flag == 0:
        global label, frame1, frame2, frame21, frame3,label2 ,label3, frame4
        frame1=Frame(window)
        frame1.pack(fill = "both")
        
        label = Label(frame1, text=  B0.month_numtoname(month) + '    ' + year, bg="RoyalBlue1", fg="sienna2", padx=3, pady=3)
        label.pack(fill = 'both', side ='top')
        label.config(font=('Arial', 20))
        label2 = Label(frame1, text= "Savings", bg="ivory2", fg="OrangeRed2", padx=3, pady=3)
        label2.pack(fill = 'both')
        label2.config(font=('Arial', 20))
        frame2=Frame(window)
        frame2.pack(fill = "both")
        dateval = StringVar()
        depval = StringVar()
        withdrawval = StringVar()
        def add_savings_button():
            date = dateval.get()
            deposit = depval.get()
            withdrawal = withdrawval.get()
            if date != '':
                date = date + '-' + B0.month_numtoname(month) + '-'  + year
                if deposit == '':
                    deposit = '0'
                if withdrawal == '':
                    withdrawal = '0'  
                B0.write_savings(date,deposit,withdrawal)
                update_app(1)
        
        def remove_savings_button():
            B0.savings_remove_lastentry()
            update_app(1)
        Savings_headers = ['DATE (day in number)',' DEPOSIT',' WITHDRAWAL',' BALANCE','ACTION']
        savings = B0.read_savings()
        savings = savings[::-1]
        for row in range(3):  
            for column in range(5):
                if row==0:
                    if column < 5:
                        label = Label(frame2, text= Savings_headers[column], bg="deep sky blue", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1)
                elif row==1:
                    if column == 0 :
                        e1 = Entry(frame2, textvariable = dateval)
                        e1.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1)   
                    if column == 1:
                        e2  = Entry(frame2,textvariable = depval )
                        e2 .grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1) 
                    if column == 2 :
                        e3 = Entry(frame2, textvariable = withdrawval)
                        e3.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1)  
                    if column == 3 :
                        label = Label(frame2, text= '---', bg="grey70", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1)  
                
                    if column == 4:
                    
                        button=Button(frame2,text  = 'add savings',command = add_savings_button,bg="lavender",fg="blue",padx=3,pady=3)
                        button.grid(row=row,column=column,sticky="nsew",padx=1,pady=1 )
                        frame2.grid_columnconfigure(column,weight=3)
                    
                elif row == 2:
                    if column <4 and len(savings)>1:
                        label = Label(frame2, text= savings[0][column], bg="grey70", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1)
                    if column <4 and len(savings)<=1:
                        label = Label(frame2, text= 'no entries', bg="grey70", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame2.grid_columnconfigure(column, weight=1)
                    if column == 4:
                        button=Button(frame2,text="delete last entry",command=remove_savings_button,bg="lavender",fg="red",padx=3,pady=3)
                        button.grid(row=row,column=column,sticky="nsew",padx=1,pady=1,columnspan =2)
                        frame2.grid_columnconfigure(column,weight=1)
        frame21=Frame(window)
        frame21.pack(fill = "both")
        label3 = Label(frame21, text= "Expenses", bg="ivory2", fg="OrangeRed2", padx=3, pady=3)
        label3.pack(fill = 'both')
        label3.config(font=('Arial', 20))
        frame3=Frame(window)
        frame3.pack(fill = "both")
        dateval = StringVar()
        expenseval = StringVar()
        typeval = StringVar()
        amountval = StringVar()
        def add_EXPENSES_button(month=month, year=year):
            date = dateval.get()
            exp = expenseval.get()
            cat = typeval.get()
            amount = amountval.get()
            if date != '':
                date = date + '-' + B0.month_numtoname(month) + '-'  + year
                B0.write_expenses(date,exp,cat,amount,month,year)
                update_app(1)
        
        def remove_EXPENSES_button(month=month, year=year):
            B0.remove_lastentry_expenses(month,year)
            update_app(1)
        Savings_headers = ['DATE (day in number)',' EXPENSE',' CATEGORY',' AMOUNT','ACTION']
        expenses = B0.read_expenses(month,year)
        expenses = expenses[::-1]
        for row in range(3):  
            for column in range(5):
                if row==0:
                    if column < 5:
                        label = Label(frame3, text= Savings_headers[column], bg= "deep sky blue", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1)
                elif row==1:
                    if column == 0 :
                        e1 = Entry(frame3, textvariable = dateval)
                        e1.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1)   
                    if column == 1:
                        e2  = Entry(frame3,textvariable = expenseval )
                        e2 .grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1) 
                    if column == 2 :
                        e3 = OptionMenu(frame3,  typeval, *CATEGORIES)
                        e3.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1)  
                    if column == 3 :
                        e4 = Entry(frame3, textvariable= amountval)
                        e4.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1)  
                
                    if column == 4:
                    
                        button=Button(frame3,text  = 'add expense',command = add_EXPENSES_button,bg="lavender",fg="blue",padx=3,pady=3)
                        button.grid(row=row,column=column,sticky="nsew",padx=1,pady=1 )
                        frame3.grid_columnconfigure(column,weight=3)
                    
                elif row == 2:
                    if column <4 and len(expenses)>1:
                        label = Label(frame3, text= expenses[0][column], bg="grey70", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1)
                    if column <4 and len(expenses)<=1:
                        label = Label(frame3, text= 'no entries', bg="grey70", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        frame3.grid_columnconfigure(column, weight=1)
                    if column == 4:
                        button=Button(frame3,text="delete last entry",command=remove_EXPENSES_button,bg="lavender",fg="red",padx=3,pady=3)
                        button.grid(row=row,column=column,sticky="nsew",padx=1,pady=1,columnspan=2)
                        frame3.grid_columnconfigure(column,weight=1)   
        frame4=Frame(window)
        frame4.pack(fill = "both")
    else:
        label.destroy()
        label2.destroy()
        label3.destroy()
        frame1.destroy()
        frame2.destroy()
        frame21.destroy()
        frame3.destroy()
        frame4.destroy()
        update_app()
    
    

        
def next_month():
    global year, month
    if month == '12':
        month = '1'
        year = str(int(year)+1)
        B0.current_month_folders(year,month)
        update_app(1)
    else:
        month = str(int(month)+1) 
        B0.current_month_folders(year,month)
        update_app(1)
def previous_month():
    global year, month
    if month == '1':
        month ='12'
        year = str(int(year)-1)
        B0.current_month_folders(year,month)
        update_app(1)
    else:
        month = str(int(month)-1)
        B0.current_month_folders(year,month)
        update_app(1)

    
update_app()

def savings_window(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(window) 
    newWindow.title('Savings tracker')
    newWindow.geometry("900x900")
    # # tabs
    frame2=Frame(newWindow)
    frame2.pack(fill = "both")  
    tree_scroll = Scrollbar(frame2)
    tree_scroll.pack(side=RIGHT,fill=Y)
    # Add some style
    style = ttk.Style()
    #Pick a theme
    style.theme_use("default")
    # Configure our treeview colors
    
    style.configure("Treeview", 
    	background="#D3D3D3",
    	foreground="black",
    	rowheight=25,
    	fieldbackground="#D3D3D3"
    	)
    # Change selected color
    style.map('Treeview', background=[('selected', 'lightblue')])
     
    sav_tree = ttk.Treeview(frame2, yscrollcommand=tree_scroll.set, selectmode="extended")
    #define colums
    sav_tree["columns"] = ("DATE", "DEPOSIT", "WITHDRAWAL","BALANCE")
    sav_tree.column("#0", width= 50)
    sav_tree.column("DATE", anchor=W, minwidth =50)
    sav_tree.column("DEPOSIT", anchor=CENTER, minwidth =50)
    sav_tree.column("WITHDRAWAL", anchor=CENTER, minwidth =50)
    sav_tree.column("BALANCE", anchor=CENTER, minwidth =50)
        #make headings
    sav_tree.heading("#0", text="Label", anchor=CENTER)   
    sav_tree.heading("DATE", text="DATE", anchor=CENTER)
    sav_tree.heading("DEPOSIT", text="DEPOSIT", anchor=CENTER)
    sav_tree.heading("WITHDRAWAL", text="WITHDRAWAL", anchor=CENTER)
    sav_tree.heading("BALANCE", text="BALANCE", anchor=CENTER)
    # Add Data
    savings = B0.read_savings()
    savings = savings[::-1]
    for i in range(len(savings)-1):   
        if i % 2 == 0:
            sav_tree.insert(parent = '',index ='end', iid = i, text =str(i+1),values = (savings[i][0],savings[i][1],savings[i][2],savings[i][3]), tags=('evenrow',))
        else: 
            sav_tree.insert(parent = '',index ='end', iid = i, text =str(i+1),values = (savings[i][0],savings[i][1],savings[i][2],savings[i][3]), tags=('oddrow',))
      # Create striped row tags
    sav_tree.pack(expand=True, fill='y')
    tree_scroll.config(command=sav_tree.yview)
    sav_tree.tag_configure('oddrow', background="white")
    sav_tree.tag_configure('evenrow', background="deep sky blue")  

def expenses_window(): 
     
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(window) 
    newWindow.title('Expenses for the month of  ' +  B0.month_numtoname(month) + '    ' + year)
    newWindow.geometry("900x900")
    # # tabs
    frame2=Frame(newWindow)
    frame2.pack(fill = "both")  
    tree_scroll = Scrollbar(frame2)
    tree_scroll.pack(side=RIGHT,fill=Y)
    # Add some style
    style = ttk.Style()
    #Pick a theme
    style.theme_use("default")
    # Configure our treeview colors
    
    style.configure("Treeview", 
    	background="#D3D3D3",
    	foreground="black",
    	rowheight=25,
    	fieldbackground="#D3D3D3"
    	)
    # Change selected color
    style.map('Treeview', background=[('selected', 'lightblue')])

    sav_tree = ttk.Treeview(frame2, yscrollcommand=tree_scroll.set, selectmode="extended")
    #define colums
    sav_tree["columns"] = ("DATE", "BILL", "TYPE","AMOUNT")
    sav_tree.column("#0", width= 50)
    sav_tree.column("DATE", anchor=W, minwidth =50)
    sav_tree.column("BILL", anchor=CENTER, minwidth =50)
    sav_tree.column("TYPE", anchor=CENTER, minwidth =50)
    sav_tree.column("AMOUNT", anchor=CENTER, minwidth =50)
        #make headings
    sav_tree.heading("#0", text="Label", anchor=CENTER)   
    sav_tree.heading("DATE", text="DATE", anchor=CENTER)
    sav_tree.heading("BILL", text="BILL", anchor=CENTER)
    sav_tree.heading("TYPE", text="CATEGORY", anchor=CENTER)
    sav_tree.heading("AMOUNT", text="AMOUNT", anchor=CENTER)
    # Add Data
    expenses = B0.read_expenses(month,year)
    expenses = expenses[::-1]
    for i in range(len(expenses)-1):   
        if i % 2 == 0:
            sav_tree.insert(parent = '',index ='end', iid = i, text =str(i+1),values = (expenses[i][0],expenses[i][1],expenses[i][2],expenses[i][3]), tags=('evenrow',))
        else: 
            sav_tree.insert(parent = '',index ='end', iid = i, text =str(i+1),values = (expenses[i][0],expenses[i][1],expenses[i][2],expenses[i][3]), tags=('oddrow',))
    sav_tree.pack(expand=True, fill='y')
    tree_scroll.config(command=sav_tree.yview)  
    sav_tree.tag_configure('oddrow', background="white")
    sav_tree.tag_configure('evenrow', background="deep sky blue")  
    
    frame1=Frame(newWindow)
    frame1.pack(fill = "both", expand=True) 
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ['Food', 'Utilities', 'Travel' ,'Entertainment', 'Subscriptions', 'Clothing', 'Miscellaneous']
    sizes = B0.find_slices_pie(month,year,CATEGORIES)
    
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.2f%%', startangle=90,shadow=True, radius=5)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.legend(labels,  loc="best")
    plt.axis('equal')
    plt.tight_layout()
    #plt.show()
    canvas = FigureCanvasTkAgg(fig1, master=frame1)
    canvas.get_tk_widget().pack()
    canvas.draw()




menu = Menu(window)
window.config(menu=menu)
menu.add_command(label ='<<<month', command = previous_month)
menu.add_separator()
menu.add_command(label ='month>>>', command = next_month)
menu.add_separator()
menu.add_separator()
menu.add_command(label ='View savings', command = savings_window)
menu.add_separator()
menu.add_command(label ='View expenses', command = expenses_window)
menu.add_separator()
menu.add_command(label ='EXIT', command = window.destroy)

window.mainloop()



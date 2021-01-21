
import os
import sys
import datetime
import csv

CATEGORIES = ['Food', 'Utilities', 'Travel' ,'Entertainment', 'Subscriptions', 'Clothing', 'Miscellaneous']
def make_folder(folder_name,rm = 0): #floder name, remove flag
    #creates the requested folder locally
    path = os.path.abspath(os.getcwd()) # current path 
    if not os.path.exists(folder_name): #if the folder doesn't exist, create it 
        os.mkdir(folder_name)
    else:  
        if rm == 0: #remove flag =0                   
            #no need to create or remove
            pass
        else :
            
            #if the folder already exists, delete it and create it (to empty it) 
            shutil.rmtree(os.path.join(path,folder_name))
            os.mkdir(folder_name)
def month_numtoname(month):
    monthnames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return monthnames[int(month)-1]
def current_month_folders(year,month):
    #check for this years folder and if doesn't exist make it
    path1 = os.path.abspath(os.getcwd()) 
    os.chdir(os.path.join(path1,'DATA'))   
    make_folder(year)
    os.chdir(os.path.join(path1,'DATA',year))
    make_folder(month_numtoname(month))
    os.chdir(path1)
                        ############# Savings tracker functions ###############3 
def read_savings(): #reader for savings
    file = 'DATA/savings.csv'
    if os.path.isfile(file):
        with open(file, 'r') as savings_file:
            csv_reader = csv.reader(savings_file)
            data = [[]]
            for row in csv_reader: 
                if len(row) == 4:
                    data.append(row[0:4])
                  
                
        return data
    else :
        return [['0','0','0','0']]
    
def write_savings(date,deposit,withdrawal): #write new entry
    savings = read_savings()
    if savings == [[]]:
        balance = 0
    else:
        balance = savings[-1][3]
    file = 'DATA/savings.csv'
    add_row = [date,deposit,withdrawal, str(float(balance)+float(deposit)-float(withdrawal))]
    if os.path.isfile(file):
        with open(file,'a', newline='') as savings_file:
            csv_writer = csv.writer(savings_file)
            csv_writer.writerow(add_row)
    else :
        with open(file,'w', newline='') as savings_file:
            csv_writer = csv.writer(savings_file)
            csv_writer.writerow(add_row)
def savings_remove_lastentry(): #remove last entry
    file = 'DATA/savings.csv'
    f = open(file, "r+")
    lines = f.readlines()
    if len(lines) != 0:
        lines.pop()
        f = open(file, "w+")
        f.writelines(lines)

############# Expenses tracker functions ###############3 
def read_expenses(month,year): #reader for savings
    file = 'DATA/'+year+'/'+month_numtoname(month)+'/expenses.csv'
    if os.path.isfile(file):
        with open(file, 'r') as savings_file:
            csv_reader = csv.reader(savings_file)
            data = [[]]
            for row in csv_reader: 
                if len(row) == 4:
                    data.append(row[0:4])
                  
                
        return data
    else :
        return [['0','0','0','0']]
    
def write_expenses(date,exp,cat,amount,month,year): #write new entry
    file = 'DATA/'+year+'/'+month_numtoname(month)+'/expenses.csv'
    print(file)
    add_row = [date,exp,cat,amount]
    if os.path.isfile(file):
        with open(file,'a', newline='') as savings_file:
            csv_writer = csv.writer(savings_file)
            csv_writer.writerow(add_row)
    else :
        with open(file,'w', newline='') as savings_file:
            csv_writer = csv.writer(savings_file)
            csv_writer.writerow(add_row)
def remove_lastentry_expenses(month,year): #remove last entry
    file = 'DATA/'+year+'/'+month_numtoname(month)+'/expenses.csv'
    f = open(file, "r+")
    lines = f.readlines()
    if len(lines) != 0:
        lines.pop()
        f = open(file, "w+")
        f.writelines(lines)
def find_slices_pie(month,year,CATEGORIES):
    data1 = read_expenses(month,year)
    data = data1[1::]
    pies = []
    for j in range(len(CATEGORIES)):
        pies.append(0)

    for i in range(len(data)):
        for j in range(len(CATEGORIES)):
            if data[i][2] == CATEGORIES[j]:
                pies[j] = pies[j] + float(data[i][3])
    return pies
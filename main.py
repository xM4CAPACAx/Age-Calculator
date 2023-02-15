import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
window = tk.Tk()
window.title("Age Calculator")
window.geometry("475x300")
window.config(bg="#00FFFF")
window.resizable(width=False,height=False)

from datetime import date
today = date.today()

def exit():
  window.destroy()
def get_age():
    day = int(e1.get())
    month =month_chosen.current()
    year =int(e3.get())
  
    if month > 12:
      print("that month does not exist")
    elif month < 1:
      print("that month does not exist")

    def isValidDate(y, m, d):

      # If month is outside the bounds of 1 to 12, return False:
      if (1 < month > 12):
          return False
      # After this point, you can assume the month is valid:

      # Check for invalid dates in 31-day months:
      if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= m <= 31):
          return False
      # Check for invalid dates in 30-day months:
      elif month in (4, 6, 9, 11) and not (1 <= d <= 30):
          return False
      # Check for invalid dates in February:
      elif month == 2 and not (1 <= d <= 28):
          return False
      # Date passes all checks and is valid, so return True:
      return True
        
    age = today.year-year-((today.month, today.day)<(month,day))
  
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')


l1 = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#00FFFF")
l2 = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#00FFFF")

l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#00FFFF")
l_m=tk.Label(window,text = "Month : ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#00FFFF")
e1=tk.Entry(window,width=5)
e2=tk.Entry(window,width=5)

n = tk.StringVar()
month_chosen = ttk.Combobox(window, textvariable = n, width=12)

# Adding combobox drop down list
month_chosen['values'] = ('Select a date...', 
                          'January', 
                          'February',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September',
                          'October',
                          'November',
                          'December')








e3=tk.Entry(window,width=5)


b1=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=get_age)
 
l3 = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#00FFFF")
t1=tk.Text(window,width=5,height=0,state="disabled")
 
b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)

l1.place(x=70,y=5)
l2.place(x=10,y=40)
l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
l_y.place(x=100,y=120)
e1.place(x=180,y=70)
#e2.place(x=180,y=95)
month_chosen.place(x=180,y=95)
e3.place(x=180,y=120)
b1.place(x=100,y=150)
l3.place(x=50,y=200)
t1.place(x=300,y=203)
b2.place(x=100,y=230)


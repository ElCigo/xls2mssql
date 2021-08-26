from tkinter import *
import pandas as pd


def submit_fields():
    path = 'foo.xlsx'
    df1 = pd.read_excel(path)

    SeriesA = df1['Loan']
    SeriesB = df1['Customer_ID']

    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    df2 = pd.DataFrame({"Loan": SeriesA, "Customer_ID": SeriesB})
    df2.to_excel(path, index=FALSE)
    entry1.delete(0, END)
    entry2.delete(0, END)


master = Tk()

frame = Frame(master)

Label(master, text="Loan").grid(row=0)
Label(master, text="Customer_ID").grid(row=1)
# frame.pack()

entry1 = Entry(master)
entry2 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=3, column=1, pady=4)

master.mainloop()

master.quit()


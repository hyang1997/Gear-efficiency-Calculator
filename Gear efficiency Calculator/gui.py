from tkinter import*
from calculator import*

commonstats = "HP/Def/Eff/Eff-res/Atk"
crit_d = "Crit Damage"
crit_c = "Crit Chance"
spd = "Speed"

stat_list = [commonstats, crit_d,crit_c,spd]

class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='white',width=20)
        self['menu'].config(font=('calibri',(10)),bg='white')

def calculate_gear():
    modi1 = (statline1.var,int(myentry1.get()))
    modi2 = (statline2.var,int(myentry1.get()))
    modi3 = (statline3.var,int(myentry1.get()))
    modi4 = (statline4.var,int(myentry1.get()))
    modi_list = [modi1,modi2,modi3, modi4]
    print(gearScore(modi_list))

     
root = Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
reforgeCheck = IntVar()
reforgeButton = Checkbutton(root, text = "Reforged/88", variable = reforgeCheck)


statline1 = MyOptionMenu(root, 'Select status', commonstats, crit_d , crit_c , spd)
statline2 = MyOptionMenu(root, 'Select status', commonstats, crit_d , crit_c , spd)
statline3 = MyOptionMenu(root, 'Select status', commonstats, crit_d , crit_c , spd)
statline4 = MyOptionMenu(root, 'Select status', commonstats, crit_d , crit_c , spd)


myentry1 = Entry(root)
myentry2 = Entry(root)
myentry3 = Entry(root)
myentry4 = Entry(root)

calculator = Button(root, text = "Calulate", command = calculate_gear)

reforgeButton.grid(row = 0, column = 0)
statline1.grid(row=1, column=0, sticky='e')
statline2.grid(row=2, column=0, sticky='e')
statline3.grid(row=3, column=0, sticky='e')
statline4.grid(row=4, column=0, sticky='e')

myentry1.grid(row=1, column=1, sticky='w')
myentry2.grid(row=2, column=1, sticky='w')
myentry3.grid(row=3, column=1, sticky='w')
myentry4.grid(row=4, column=1, sticky='w')

calculator.grid(row=5, column = 1)


root.geometry("400x400")
root.mainloop()


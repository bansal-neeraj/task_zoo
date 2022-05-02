from tkinter import Tk,Button,Label
from zoo_animals import Zoo,Animal


app = Tk()
app.title('Zoo Simulation')

z1 = Zoo(app)

# create labels for List boxes for user interface

for index, animal_species in enumerate(Animal, start=1):
    animal_label = Label(app, text=animal_species.name, font=('bold', 14), pady=20)
    animal_label.grid(row=0, column=index)

# ------------------------------------Buttons ------------------------------------

hour_btn = Button(app,text='Feed',width=10,command=z1.feed)
hour_btn.grid(row=5,column=0)

hour_btn = Button(app,text='next hour',width=10,command=z1.hour_next)
hour_btn.grid(row=5,column=3)

# ------------------------------------Buttons ------------------------------------

app.geometry('700x350')
app.mainloop()
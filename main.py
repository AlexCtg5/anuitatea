from tkinter import *
import pandas as pd

#----------------------------FUNCTIONS-------------------------------

def calcul_anuitate():
    durata_creditului = int(durata_credituluie.get())
    rata_dobanda = float(rata_dobandae.get())/100
    val_credit = float(val_credite.get())

    partea_de_sus= (val_credit * rata_dobanda)/12
    partea_de_jos = 1-(1/((1+(rata_dobanda/12))**durata_creditului))

    anuitatea = partea_de_sus/partea_de_jos
    valoare_anuitate.config(text= f"{anuitatea}")

    suma = val_credit
    d =[]
    s =[]
    p =[]
    a = []
    for _ in range(durata_creditului):
        dobanda = suma * rata_dobanda / 12
        principal = anuitatea - dobanda
        a.append(round(anuitatea, 2))
        d.append(round(dobanda, 2))
        s.append(round(suma, 2))
        p.append(round(principal, 2))
        suma -= principal
    data = {"Suma": s, "anuitate": a, "dobanda": d, "principal": p}
    df = pd.DataFrame(data)
def calcul_valoare_credit():
    anuitatea = float(anuitate.get())
    durata_creditului = int(durata_credituluie.get())
    rata_dobanda = float(rata_dobandae.get())/100

    partea_de_jos = 1-(1/((1+(rata_dobanda/12))**durata_creditului))

    valoarea_creditului = (anuitatea * partea_de_jos)/(rata_dobanda/12)
    valoare_credit.config(text= f"{valoarea_creditului}")

    suma = valoarea_creditului
    d = []
    s = []
    p = []
    a = []
    for _ in range(durata_creditului):
        dobanda = suma * rata_dobanda / 12
        principal = anuitatea - dobanda
        a.append(round(anuitatea, 2))
        d.append(round(dobanda, 2))
        s.append(round(suma, 2))
        p.append(round(principal, 2))
        suma -= principal
    data = {"Suma": s, "anuitate": a, "dobanda": d, "principal": p}
    df = pd.DataFrame(data)
    print(df)

def clear_text(entry):
    entry.delete(0, "end")

def reseteaza():
    clear_text(val_credite)
    clear_text(anuitate)
    clear_text(rata_dobandae)
    clear_text(durata_credituluie)
    valoare_anuitate.config(text= "0")
    valoare_credit.config(text= "0")


#-------------------------------UI-SETUP-------------------------------

screen = Tk()
screen.config(padx=50, pady=50)
screen.title("Anuitate/ValCredit")

anuitate_text = Label(text="Anuitate:")
anuitate_text.grid(column=0, row=0)
anuitate = Entry()
anuitate.grid(column=1, row=0)

val_credit_text = Label(text="Valoarea creditului:")
val_credit_text.grid(column=0, row=1)
val_credite = Entry()
val_credite.grid(column=1, row=1)

rata_dobanda_text = Label(text="Rata dobanda:")
rata_dobanda_text.grid(column=0, row=2)
rata_dobandae = Entry()
rata_dobandae.grid(column=1, row=2)

durata_creditului_text = Label(text="Durata creditului:")
durata_creditului_text.grid(column=0, row=3)
durata_credituluie = Entry()
durata_credituluie.grid(column=1, row=3)

valoare_anuitate = Label(text="0")
valoare_anuitate.grid(column=1, row=4)
calculeaza_anuitatea = Button(text="Calculeaza Anuitatea", width= 17, command= calcul_anuitate)
calculeaza_anuitatea.grid(column=0, row=4)


valoare_credit = Label(text="0")
valoare_credit.grid(column=1, row=5)
calculeaza_val_credit = Button(text="Calculeaza Val. Creditului", width= 17, command= calcul_valoare_credit)
calculeaza_val_credit.grid(column=0, row=5)

reset_button = Button(text= "Reseteaza", width=17, command= reseteaza)
reset_button.grid(column=1, row=6)



screen.mainloop()

# test 2 
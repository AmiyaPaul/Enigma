from tkinter import *
from datetime import date

today = date.today()
td = f"{today}"



log = "f"

rotor = {1: "D", 2: "Z", 3: "V", 4: "U", 5: "G", 6: "A", 7: "H", 8: "W", 9: "B", 10: "L", 11: "S", 12: "K", 13: "E",
         14: "P", 15: "M", 16: "T", 17: "X", 18: "J", 19: "Q", 20: "F", 21: "N", 22: "I", 23: "R", 24: "Y", 25: "O",
         26: "C"}

rotA = {1: 3, 2: 17, 3: 1, 4: 12, 5: 7, 6: 5, 7: 20, 8: 23, 9: 11, 10: 14, 11: 19, 12: 24, 13: 16, 14: 10, 15: 18,
        16: 8, 17: 2, 18: 26, 19: 21, 20: 4, 21: 25, 22: 15, 23: 22, 24: 9, 25: 6, 26: 13}

rotB = {1: 15, 2: 4, 3: 3, 4: 13, 5: 25, 6: 17, 7: 1, 8: 18, 9: 22, 10: 14, 11: 11, 12: 2, 13: 26, 14: 8, 15: 7,
        16: 19, 17: 20, 18: 16, 19: 6, 20: 9, 21: 24, 22: 23, 23: 21, 24: 5, 25: 12, 26: 10}

rotC = {1: 24, 2: 23, 3: 7, 4: 6, 5: 17, 6: 4, 7: 21, 8: 22, 9: 19, 10: 11, 11: 10, 12: 14, 13: 18, 14: 20, 15: 3,
        16: 12, 17: 1, 18: 9, 19: 8, 20: 26, 21: 13, 22: 5, 23: 16, 24: 25, 25: 2, 26: 15}

reflac = {6: 5, 24: 14, 16: 17, 1: 23, 10: 18, 2: 21, 19: 8, 15: 26, 22: 7, 11: 3, 4: 9, 12: 13, 20: 25, 5: 6, 14: 24,
          17: 16, 23: 1, 18: 10, 21: 2, 8: 19, 26: 15, 7: 22, 3: 11, 9: 4, 13: 12, 25: 20}



def caps(event):
    inptxt.set(inptxt.get().upper())


def fnAp():
    if lbAvar.get() >= 26:
        lbAvar.set(1)
    else:
        x = lbAvar.get()
        x = x+1
        lbAvar.set(x)

def fnBp():
    if lbBvar.get() >= 26:
        lbBvar.set(1)
    else:
        x = lbBvar.get()
        x = x+1
        lbBvar.set(x)

def fnCp():
    if lbCvar.get() >= 26:
        lbCvar.set(1)
    else:
        x = lbCvar.get()
        x = x+1
        lbCvar.set(x)

def fnAm():
    if lbAvar.get() <= 1:
        lbAvar.set(26)
    else:
        x = lbAvar.get()
        x = x-1
        lbAvar.set(x)

def fnBm():
    if lbBvar.get() <= 1:
        lbBvar.set(26)
    else:
        x = lbBvar.get()
        x = x-1
        lbBvar.set(x)

def fnCm():
    if lbCvar.get() <= 1:
        lbCvar.set(26)
    else:
        x = lbCvar.get()
        x = x-1
        lbCvar.set(x)

def fnforbac():
    global log
    if log == "f":
        log = "b"
        forbac.configure(text="BACKWARD")
    else:
        log = "f"
        forbac.configure(text="FORWARD")

def fnclr():
    outvar.set("")
    inptxt.set("")
    lbAvar.set(1)
    lbBvar.set(1)
    lbCvar.set(1)


def fEnigma(kt):
    key = list(filter(lambda x: rotor[x] == kt, rotor))[0]
    key = key + lbAvar.get() - 1
    if key > 26:
        key = key - 26
    k1 = rotA[key]
    k1 = k1 + lbBvar.get() - 1
    if k1 > 26:
        k1 = k1 - 26
    k2 = rotB[k1]
    k2 = k2 + lbCvar.get() - 1
    if k2 > 26:
        k2 = k2 - 26
    k3 = rotC[k2]
    k3 = reflac[k3]
    k3 = k3 + lbCvar.get() - 1
    if k3 > 26:
        k3 = k3 - 26
    k2 = rotC[k3]
    k2 = k2 + lbBvar.get() - 1
    if k2 > 26:
        k2 = k2 - 26
    k1 = rotB[k2]
    k1 = k1 + lbAvar.get() - 1
    if k1 > 26:
        k1 = k1 - 26
    kf = rotA[k1]
    fin = rotor[kf]
    return fin

def bEnigma(kt):
    key = list(filter(lambda x: rotor[x] == kt, rotor))[0]
    k1 = list(filter(lambda x: rotA[x] == key, rotA))[0]
    k1 = k1 - lbAvar.get() + 1
    if k1 < 1:
        k1 = k1 + 26
    k2 = list(filter(lambda x: rotB[x] == k1, rotB))[0]
    k2 = k2 - lbBvar.get() + 1
    if k2 < 1:
        k2 = k2 + 26
    k3 = list(filter(lambda x: rotC[x] == k2, rotC))[0]
    k3 = k3 - lbCvar.get() + 1
    if k3 < 1:
        k3 = k3 + 26
    k3 = list(filter(lambda x: reflac[x] == k3, reflac))[0]
    k2 = list(filter(lambda x: rotC[x] == k3, rotC))[0]
    k2 = k2 - lbCvar.get() + 1
    if k2 < 1:
        k2 = k2 + 26
    k1 = list(filter(lambda x: rotB[x] == k2, rotB))[0]
    k1 = k1 - lbBvar.get() + 1
    if k1 < 1:
        k1 = k1 + 26
    kf = list(filter(lambda x: rotA[x] == k1, rotA))[0]
    kf = kf - lbAvar.get() + 1
    if kf < 1:
        kf = kf + 26
    fin = rotor[kf]
    return fin

def fnentr():
    keytxt = inptxt.get().upper()
    txt = ""
    for i in range(len(keytxt)):
        jio = keytxt[i]
        if jio.isspace() or jio == "." or jio == "," or jio == "?" or jio == "!":
            kk = jio
        else:
            if log == "f":
                kk = fEnigma(jio)
            else:
                kk = bEnigma(jio)
        txt = f"{txt}{kk}"

        lbAvar.set(lbAvar.get()+1)
        if lbAvar.get() >= 26:
            lbAvar.set(1)
        if (i+1) % 13 == 0:
            lbBvar.set(lbBvar.get()+1)
            if lbBvar.get() >= 26:
                lbBvar.set(1)
        if (i+1) % 26 == 0:
            lbCvar.set(lbCvar.get()+1)
            if lbCvar.get() >= 26:
                lbCvar.set(1)

    outvar.set(txt)


def fntday():
    tdlis = td.split("-")
    a = int(tdlis[2])
    if a > 26:
        xa = a // 26
        a = a - (xa * 26)
    b = int(tdlis[1])
    if b > 26:
        xb = b // 26
        b = b - (xb * 26)
    c = int(tdlis[0][-2:])
    if c > 26:
        xc = c // 26
        c = c - (xc * 26)

    lbAvar.set(a)
    lbBvar.set(b)
    lbCvar.set(c)





root = Tk()
root.geometry("650x345")
root.title("Enigma Machine")

f1 = Frame(root, bg="white")
f1.pack(side=TOP, anchor="nw", fill=X)

Label(f1, text="Welcome To Amiya's Enigma Machine", bg="white", fg="red", font="Arial 20 bold").pack(side=TOP)

disfra = Frame(f1, bg="#60FFFA")
disfra.pack(side=TOP, fill=X)

disleft = Frame(disfra, bg="#60FFFA")
disleft.pack(side=LEFT, padx=50, pady=20)

disright = Frame(disfra, bg="#60FFFA")
disright.pack(side=LEFT)

btnAp = Button(disleft, text="+", command=fnAp)
btnAp.grid(row=1, column=3, pady=5, padx=5, ipady=2, ipadx=5)
btnBp = Button(disleft, text="+", command=fnBp)
btnBp.grid(row=1, column=2, pady=5, padx=5, ipady=2, ipadx=5)
btnCp = Button(disleft, text="+", command=fnCp)
btnCp.grid(row=1, column=1, pady=5, padx=5, ipady=2, ipadx=5)
btnAm = Button(disleft, text="-", command=fnAm)
btnAm.grid(row=3, column=3, pady=5, padx=5, ipady=2, ipadx=7)
btnBm = Button(disleft, text="-", command=fnBm)
btnBm.grid(row=3, column=2, pady=5, padx=5, ipady=2, ipadx=7)
btnCm = Button(disleft, text="-", command=fnCm)
btnCm.grid(row=3, column=1, pady=5, padx=5, ipady=2, ipadx=7)

lbAvar = IntVar()
lbBvar = IntVar()
lbCvar = IntVar()


lbA = Entry(disleft, width=4, state="disabled", justify=CENTER, textvariable=lbAvar)
lbAvar.set(1)
lbA.grid(row=2, column=3, ipady=4)

lbB = Entry(disleft, width=4, state="disabled", justify=CENTER, textvariable=lbBvar)
lbBvar.set(1)
lbB.grid(row=2, column=2, ipady=4)

lbC = Entry(disleft, width=4, state="disabled", justify=CENTER, textvariable=lbCvar)
lbCvar.set(1)
lbC.grid(row=2, column=1, ipady=4)

forbac = Button(disright, text="FORWARD", height=2, width=10, command=fnforbac)
forbac.grid(row=1, column=1, padx=20)

entr = Button(disright, text="CONVERT", height=2, width=10, command=fnentr)
entr.grid(row=1, column=2, padx=20)

clr = Button(disright, text="CLEAR", height=2, width=10, command=fnclr)
clr.grid(row=1, column=3, padx=20)

tday = Button(disright, text="TODAY", height=2, width=10, command=fntday)
tday.grid(row=2, column=2, padx=20, pady=10)






keyfra = Frame(f1, bg="#FFDFB8")
keyfra.pack(side=TOP, fill=X)

Label(keyfra, text="Give the input text", font="Arial 10 bold", bg="#FFDFB8").pack(side=TOP, pady=10)

inptxt = StringVar()
inpEntry = Entry(keyfra, font="Arial 10 bold", width=70, justify=CENTER, textvariable=inptxt)
inpEntry.pack(side=TOP, ipady=4)
inpEntry.bind("<KeyRelease>", caps)

Label(keyfra, text="Converted text is", font="Arial 10 bold", bg="#FFDFB8").pack(side=TOP, pady=10)

outvar = StringVar()
outLbl = Entry(keyfra, bg="white", font="Arial 10 bold", width=70, justify=CENTER, textvariable=outvar)
outLbl.pack(side=TOP, ipady=4, pady=10)




root.mainloop()
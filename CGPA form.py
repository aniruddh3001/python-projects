import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

#--------------------------------pointer
def pointerz(z):
    if 0.55 <= z < 0.6:
        return 6
    z = z * 10

    if int(z) == 0 or int(z) == 1 or int(z) == 2 or int(z) == 3:
        return 0
    elif int(z) == 4:
        return 4
    elif int(z) == 5:
        return 5
    elif int(z) == 6:
        return 7
    elif int(z) == 7:
        return 8
    elif int(z) == 8:
        return 9
    elif int(z) == 9 or int(z) ==10:
        return 10
    
    return 0


#-------------------------------------submit button
def submit_form():
    intpce = int(intpce_entry.get())
    endpce = int(endpce_entry.get())
    b = endpce + intpce

    intmath = int(intmath_entry.get())
    endmath = int(endmath_entry.get())
    a = endmath + intmath

    
    intcp = int(intcp_entry.get())
    endcp = int(endcp_entry.get())
    g = endcp + intcp

    intphy = int(intphy_entry.get())
    endphy = int(endphy_entry.get())
    c = endphy + intphy
    
    intchem = int(intchem_entry.get())
    endchem = int(endchem_entry.get())
    d = endchem + intchem
    
    intmech = int(intmech_entry.get())
    endmech = int(endmech_entry.get())
    e = endmech + intmech

    intbeee = int(intbeee_entry.get())
    endbeee = int(endbeee_entry.get())
    f = endbeee + intbeee

    att = attendance_var.get()
    
    a = (a/125);
    a = pointerz(a);
    
    b = (b/75);
    b = pointerz(b);

    c = (c/75);
    c = pointerz(c);

    d = (d/75);
    d= pointerz(d);
    
    e = (e/100);
    e = pointerz(e);

    f = (f/100);
    f= pointerz(f);
    
    g = (g/50);
    g = pointerz(g);
    
    if(a*b*c*d*e*f*g==0):
        print("Your pointer was not generated")
        return 0

    if(att == -1):
        h = 1.0*(3*a + 2*b + 2*c+ 2*d+ 2*g+ 2*f + 3*e + 7*2 + 7*0.5 + 7*0.5 + 10*2 + 7*1 + 9*1)/23;
        print(f"Your pointer is {h}")
        messagebox.showinfo("Title",f"The GPA is {h}") 
        return h
    if(att == 0):
        h = 1.0*(3*a + 2*b + 2*c+ 2*d+ 2*g+ 2*f + 3*e + 9*2 + 8*0.5 + 8*0.5 + 10*2 + 8*1 + 9*1)/23;
        print(f"Your pointer is {h}")
        messagebox.showinfo("Title",f"The GPA is {h}") 
        return h
    if(att == 1):
        h = 1.0*(3*a + 2*b + 2*c+ 2*d+ 2*g+ 2*f + 3*e + 10*2 + 8*0.5 + 10*0.5 + 10*2 + 10*1 + 9*1)/23;
        print(f"Your pointer is {h}")
        messagebox.showinfo("Title",f"The GPA is {h}") 
        return h


#main tkinter window   ------------  
root = tk.Tk()

root.title("Sem 1 SGPA calculator")
root.geometry("280x440")
tk.Label(root, text="Internal").place(x=60, y=20)
tk.Label(root, text="Endsem").place(x=150, y=20)


# --- MATH ---
y_off = 60
tk.Label(root, text="Math").place(x=20, y=y_off)
intmath_entry = tk.Entry(root, width=5)
intmath_entry.place(x=60, y=y_off)
endmath_entry = tk.Entry(root, width=5)
endmath_entry.place(x=150, y=y_off)

# --- CP ---
y_off += 40
tk.Label(root, text="CP").place(x=20, y=y_off)
intcp_entry = tk.Entry(root, width=5)
intcp_entry.place(x=60, y=y_off)
endcp_entry = tk.Entry(root, width=5)
endcp_entry.place(x=150, y=y_off)

# --- BEEE ---
y_off += 40
tk.Label(root, text="BEEE").place(x=20, y=y_off)
intbeee_entry = tk.Entry(root, width=5)
intbeee_entry.place(x=60, y=y_off)
endbeee_entry = tk.Entry(root, width=5)
endbeee_entry.place(x=150, y=y_off)

# --- MECH ---
y_off += 40
tk.Label(root, text="Mech").place(x=20, y=y_off)
intmech_entry = tk.Entry(root, width=5)
intmech_entry.place(x=60, y=y_off)
endmech_entry = tk.Entry(root, width=5)
endmech_entry.place(x=150, y=y_off)

# --- PHYSICS ---
y_off += 40
tk.Label(root, text="Phy").place(x=20, y=y_off)
intphy_entry = tk.Entry(root, width=5)
intphy_entry.place(x=60, y=y_off)
endphy_entry = tk.Entry(root, width=5)
endphy_entry.place(x=150, y=y_off)

# --- CHEMISTRY ---
y_off += 40
tk.Label(root, text="Chem").place(x=20, y=y_off)
intchem_entry = tk.Entry(root, width=5)
intchem_entry.place(x=60, y=y_off)
endchem_entry = tk.Entry(root, width=5)
endchem_entry.place(x=150, y=y_off)

# --- PCE ---
y_off += 40
tk.Label(root, text="PCE").place(x=20, y=y_off)
intpce_entry = tk.Entry(root, width=5)
intpce_entry.place(x=60, y=y_off)
endpce_entry = tk.Entry(root, width=5)
endpce_entry.place(x=150, y=y_off)

#-----------------main window again
attendance_var = tk.IntVar(value = -2)
l = tk.Radiobutton(root, text="Low(<75%)", variable = attendance_var, value = -1)
m = tk.Radiobutton(root, text="Medium", variable = attendance_var, value = 0)
f = tk.Radiobutton(root, text="Full", variable = attendance_var, value = 1)

l.place(x=20, y =340)
m.place(x=120, y =340)
f.place(x=200, y =340)

submit_button = tk.Button(root, text="Calculate", command=submit_form)
submit_button.place(x=20, y=380)



root.mainloop()

import tkinter as mic

window mic.Tk() 
window.title("MICOH EBARLE") 
window.geometry("600x600") 
window.resizable (False, True) 
window.configure(bg="lightblue")

label1 = mic.Label(window, text="STUDENT PROFILE", PROFILE", font ("calibri",20,"bold"), fg-"black",bg-"lightblue") 
label2 = mic.Label(window, text="name: Mark christian B. Ebarle", font ("Arial",14),fg" 14), fg="black", bg-lightblue")
label3 = mic.Label(window, text="Age: 22 years old", font("Arial",14), fg="black", bg="lightblue") 
label4 = mic.Label(window, text="course: BSIT-1C", font ("Arial", 14), fg="black", bg="lightblue")
labels = mic.Label(window, text="Birthday: november 03 2003", font=("Arial",14), fg="black", bg="lightblue") 
labe16 - mic.Label(window, text="Motto: ", font=("Arial",14), fg="black", bg="lightblue") 
label7 = mic.Label(window, text="Maging positibo sa lahat wag lang sa drugs", font=("Arial",14), fg="black", bg="lightblue")

label1.pack(padx=(10,0), pady=(0,0)) 
label2.pack(padx=(0,340), pady-(10,0))
label3.pack(padx=(0,440), pady-(10,0)) 
labe14.pack(padx=(0,454), pady-(10,0))
labe15.pack(padx=(0,355), pady=(101e)) 
label6.pack(padx=(0,535), pady-(10,0))
label7.pack(padx=(0,200), pady-(10,0))

window.mainloop()

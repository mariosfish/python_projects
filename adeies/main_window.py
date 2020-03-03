from tkinter import *

root = Tk()
root.title('Άδεια Στρατιωτικού Προσωπικού')
root.iconbitmap('')
root.geometry('800x400')

# Labels
bathmos = Label(root, text="Βαθμός:")
onoma = Label(root, text="Όνομα:")
eponymo = Label(root, text="Επώνυμο:")
patronymo = Label(root, text="Πατρώνυμο:")
am = Label(root, text="ΑΜ/ΕΠΟ:")
kathikonta = Label(root, text="Καθήκοντα/Ειδικότητα:")
edra = Label(root, text="Έδρα:")
thema = Label(root, text="Θέμα:")
eidos_adeias = Label(root, text="Είδος άδειας:")

# Entries
bathmos_entry = Entry(root, width=20)
am_entry = Entry(root, width=10)
onoma_entry = Entry(root, width=20)
eponymo_entry = Entry(root, width=210)
patronymo_entry = Entry(root, width=20)
kathikonta_entry = Entry(root, width=20)
bathmos_entry = Entry(root, width=20)
edra_entry = Entry(root, width=10)
thema_entry = Entry(root, width=40)
eidos_entry = Entry(root, width=10)

# Buttons
create = Button(root, text='Δημιουργία άδειας')

# Positioning
bathmos.grid(row=0, column=0, pady=5, sticky=W, padx=10)
bathmos_entry.grid(row=0, column=1, pady=5)
am.grid(row=0, column=2, padx=10, pady=5)
am_entry.grid(row=0, column=3, pady=5)
onoma.grid(row=1, column=0, pady=5)
onoma_entry.grid(row=1, column=1, pady=5)
eponymo.grid(row=1, column=2, pady=5)
eponymo_entry.grid(row=1, column=3, pady=5)
patronymo.grid(row=2, column=0, pady=5)
patronymo_entry.grid(row=2, column=1, pady=5)
kathikonta.grid(row=2, column=2, pady=5)
kathikonta_entry.grid(row=2, column=3, pady=5)
thema.grid(row=3, column=0, pady=5)
thema_entry.grid(row=3, column=1, pady=5)
create.grid(row=6, column=0, padx=10, pady=5)  # Button

root.mainloop()

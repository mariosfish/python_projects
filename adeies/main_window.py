from tkinter import *

root = Tk()
root.title('Άδεια Στρατιωτικού Προσωπικού')
root.iconbitmap('')
root.geometry('400x400')

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
eponymo_entry = Entry(root, width=25)
patronymo_entry = Entry(root, width=20)
kathikonta_entry = Entry(root, width=20)
bathmos_entry = Entry(root, width=20)
edra_entry = Entry(root, width=10)
thema_entry = Entry(root, width=20)
eidos_entry = Entry(root, width=10)


# Positioning
bathmos.grid(row=0, column=0,pady=5)
bathmos_entry.grid(row=0, column=1,pady=5)
am.grid(row=0, column=2, padx=5, pady=5)
am_entry.grid(row=0, column=3, pady=5)
onoma.grid(row=1, column=0, pady=5)
onoma_entry.grid(row=1, column=0, pady=5)
bathmos_entry.grid(row=0, column=1, pady=5)
am.grid(row=0, column=2, padx=5, pady=5)
am_entry.grid(row=0, column=3, pady=5)


root.mainloop()

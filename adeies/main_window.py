import locale
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import *

from mailmerge import MailMerge

locale.setlocale(locale.LC_TIME, "el_GR.UTF-8")  # greek


def replace_values():
    # file to open
    template = "adeia-template.docx"
    document = MailMerge(template)
    # print(document.get_merge_fields())
    # replace values from entries to the new document
    document.merge(
        tilefono=tilefono_entry.get(),
        diefthinsi=diefthinsi_entry.get(),
        kathikonta=kathikonta_entry.get(),
        thema=thema_entry.get(),
        start_date=start_date_entry.get_date(),
        eponymo=eponymo_entry.get(),
        monada=monada_entry.get(),
        patronymo=patronymo_entry.get(),
        today='{:%d %b %y}'.format(date.today()),
        edra=edra_entry.get(),
        bathmos=bathmos_entry.get(),
        am=am_entry.get(),
        onoma=onoma_entry.get()
    )
    # save the new document
    document.write('test-output.docx')


root = Tk()
root.title('Άδεια Στρατιωτικού Προσωπικού')
root.iconbitmap('')
root.geometry('500x500')

# Labels
monada = Label(root, text="Μονάδα:", font=('Arial', 12))
bathmos = Label(root, text="Βαθμός:", font=('Arial', 12))
onoma = Label(root, text="Όνομα:", font=('Arial', 12))
eponymo = Label(root, text="Επώνυμο:", font=('Arial', 12))
patronymo = Label(root, text="Πατρώνυμο:", font=('Arial', 12))
am = Label(root, text="ΑΜ/ΕΠΟ:", font=('Arial', 12))
kathikonta = Label(root, text="Καθήκοντα/Ειδικότητα:", font=('Arial', 12))
edra = Label(root, text="Έδρα:", font=('Arial', 12))
thema = Label(root, text="Θέμα:", font=('Arial', 12))
eidos_adeias = Label(root, text="Είδος άδειας:", font=('Arial', 12))
diefthinsi = Label(root, text="Διεύθυνση:", font=('Arial', 12))
tilefono = Label(root, text="Τηλέφωνο:", font=('Arial', 12))
antikatastatis = Label(root, text="Αντικαταστάτης:", font=('Arial', 12))
start_date = Label(root, text="Έναρξη άδειας:", font=('Arial', 12))

# Entries
monada_entry = Entry(root, width=20)
bathmos_entry = Entry(root, width=20)
am_entry = Entry(root, width=20)
onoma_entry = Entry(root, width=20)
eponymo_entry = Entry(root, width=20)
patronymo_entry = Entry(root, width=20)
kathikonta_entry = Entry(root, width=20)
bathmos_entry = Entry(root, width=20)
edra_entry = Entry(root, width=20)
thema_entry = Entry(root, width=20)
eidos_entry = Entry(root, width=20)
diefthinsi_entry = Entry(root, width=20)
tilefono_entry = Entry(root, width=20)
antikatastatis_entry = Entry(root, width=20)
start_date_entry = DateEntry(root)

# Button
create = Button(root, text='Δημιουργία άδειας', command=replace_values)

# Positioning
am.grid(row=0, column=0, pady=5, sticky=W, padx=10)
am_entry.grid(row=0, column=1, pady=5, sticky=W, padx=10)
bathmos.grid(row=1, column=0, pady=5, sticky=W, padx=10)
bathmos_entry.grid(row=1, column=1, pady=5, sticky=W, padx=10)
onoma.grid(row=2, column=0, pady=5, sticky=W, padx=10)
onoma_entry.grid(row=2, column=1, pady=5, sticky=W, padx=10)
eponymo.grid(row=3, column=0, pady=5, sticky=W, padx=10)
eponymo_entry.grid(row=3, column=1, pady=5, sticky=W, padx=10)
patronymo.grid(row=4, column=0, pady=5, sticky=W, padx=10)
patronymo_entry.grid(row=4, column=1, pady=5, sticky=W, padx=10)
monada.grid(row=5, column=0, pady=5, sticky=W, padx=10)
monada_entry.grid(row=5, column=1, pady=5, sticky=W, padx=10)
kathikonta.grid(row=6, column=0, pady=5, sticky=W, padx=10)
kathikonta_entry.grid(row=6, column=1, padx=10, pady=5, sticky=W)
thema.grid(row=7, column=0, padx=10, pady=5, sticky=W)
thema_entry.grid(row=7, column=1, padx=10, pady=5, sticky=W)
eidos_adeias.grid(row=8, column=0, padx=10, pady=5, sticky=W)
eidos_entry.grid(row=8, column=1, padx=10, pady=5, sticky=W)
diefthinsi.grid(row=9, column=0, padx=10, pady=5, sticky=W)
diefthinsi_entry.grid(row=9, column=1, padx=10, pady=5, sticky=W)
tilefono.grid(row=10, column=0, padx=10, pady=5, sticky=W)
tilefono_entry.grid(row=10, column=1, padx=10, pady=5, sticky=W)
antikatastatis.grid(row=11, column=0, padx=10, pady=5, sticky=W)
antikatastatis_entry.grid(row=11, column=1, padx=10, pady=5, sticky=W)
start_date.grid(row=12, column=0, padx=10, pady=5, sticky=W)
start_date_entry.grid(row=12, column=1, padx=10, pady=5, sticky=W)
create.grid(row=100, columnspan=2, pady=20)  # button


root.mainloop()

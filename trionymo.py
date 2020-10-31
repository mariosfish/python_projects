from math import sqrt


def trionymo(a, b, c):
    D = float(b**2 - 4*a*c)

    if a == 0:
        print("Η εξίσωση που προσπαθείς να λύσεις δεν είναι 2ου βαθμού.")

    elif D < 0:
        x1 = complex(-b/(2*a), sqrt(abs(D))/(2*a))
        x2 = complex(-b/(2*a), -sqrt(abs(D))/(2*a))
        print("Το τρυώνυμο δεν έχει πραγματικές ρίζες αλλά μιγαδικές.")
        print(
            "Οι μιγαδικές ρίζες του τριωνύμου είναι οι x1= {0} και x2= {1}.".format(x1, x2))
        return x1, x2
    elif D == 0:
        x1 = -b/(2*a)
        print("Το τρυώνυμο έχει μία διπλή ρίζα την: {0}".format(x1))
        return x1
    else:
        x1 = -b + sqrt(D)/(2*a)
        x2 = -b - sqrt(D)/(2*a)
        print("Το τριώνυμο έχει 2 πραγματικές ρίζες, την x1= {0} και την x2= {1}.".format(
            x1, x2))
        return x1, x2

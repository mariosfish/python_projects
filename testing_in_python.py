import trionymo
# import system


print("Καλώς ήρθατε στον υπολογιστή ριζών τριωνύμου!\n")

a = float(input("Παρακαλώ εισάγετε τον συντελεστή α του τριωνύμου: "))
b = float(input("Παρακαλώ εισάγετε τον συντελεστή β του τριωνύμου: "))
c = float(input("Παρακαλώ εισάγετε τον συντελεστή γ του τριωνύμου: "))

rizes = trionymo.trionymo(a, b, c)

print(rizes)

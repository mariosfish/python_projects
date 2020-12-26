import pandas as pd

# load data
df = pd.read_excel('questions_full.xlsx')

# allagi tou index gia na tairiazei me to tErwthsh_id
df = df.set_index('tErwthsh_id')

# antikatastasi to aa me A, B, C, D
df['apanthsh_aa'] = df['apanthsh_aa'].replace(
    {1: "A. ", 2: "B. ", 3: "C. ", 4: "D. "})

# concat ta A B C D me to lektiko tis apantisis
df['mazi'] = df['apanthsh_aa']+df['apanthshlektiko']

# lexiko pou tha xreiastei gia tin ektyposi tis apantisis
mappings = {1: "A", 2: "B", 3: "C", 4: "D"}

# dimiourgia arxeiou txt
with open("test_full.txt", "w+", encoding="utf-8") as file:
    
    # gia kathe monadiko Erothsh_id
    for i in df.index.unique():

        # grafei tin erotisi sto arxeio
        file.write(str(df.loc[i]['Perigrafh'].unique()).strip("['']")+"\n")

        # gia kathe erotisi grafei sto arxeio tis pithanes apantiseis
        for val in df.loc[i]['mazi']:
            file.write(str(val).strip("['']")+"\n")

        # deixnei poia apo tis pithanes apantiseis einai i sosti (xekinaei apo to 1 oxi to 0)
        sosti_apantisi = list(df.loc[i]['posostobathmologias']).index(100)+1

        # grafei tin sosti apantisi sto arxeio
        file.write("ANSWER: " + mappings[sosti_apantisi]+"\n")

        # prosthetei mia keni grammi
        file.write("\n")

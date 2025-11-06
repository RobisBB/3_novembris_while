# Sasummē ievadītos skaitļus. 0 norāda, ka darbs jābeidz.
summa = 0 # inicialize summa mainigo
x = int(input("Ievadi skaitli (0 lai beigtu): ")) # inicialize x mainigo
while x != 0: # kamer x nav 0
    summa += x # pievieno x summai
    x = int(input("Ievadi skaitli (0 lai beigtu): ")) # ievadi jaunu x
print("Summa:", summa) # izvada summu
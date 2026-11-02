n1=float(input("donner la premier note:"))
n2=float(input("donner la dexieme note:"))
n3=float(input("donner la troisieme  note:"))
moy=(n1+n2+n3)/3
print("la moyenne est :",moy)
#########################
if moy<10:
    print("Mention: Insuffisant")
elif moy<12:
    print("Mention :Passable")
elif moy<14:
    print(" Mention:Assez bien ")
elif moy<16:
    print(" Mention: Bien ")
else:
    print("Mention: Tres bien ")
    
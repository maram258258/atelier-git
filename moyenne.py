n1=float(input("donner la premier note:"))
n2=float(input("donner la dexieme note:"))
n3=float(input("donner la troisieme:"))
code= input("donner le code:")
nom= input("donner le nom:")
prenom= input("donner le prenom:")
moy=(n1+n2+n3)/3
print("la moyenne est :",moy)
if moy<10:
    print("redouble")
    print("Mention: Insuffisant")
elif moy<12:
    print("Mention :Passable")
    print('admis')
elif moy<14:
    print(" Mention:Assez bien ")
    print('admis bien')
elif moy<16:
    print(" Mention: Bien ")
    print("admis tres bien")
else:
    print("Mention: Tres bien ")
    print("admis excellent")
print("code:",code)
print("nom:",nom)
print("prenom:",prenom)
 
def mediane(notes):
    tri=sorted(notes)
    n=len(tri)
    return tri [n//2]
print("mediane:",mediane(notes))
    
    
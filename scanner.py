
f=open("Hamlet.txt","r")

quantidade_caracteres=len(f.read())

f.close()
print(f"Quantidade de caracteres: {quantidade_caracteres}")

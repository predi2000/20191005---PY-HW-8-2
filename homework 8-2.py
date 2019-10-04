secret=3
secret1=14
secret2=27
secret3=44
secret4=68

guess=int(input("Raten Sie die Zahl (00-99): "))

if guess == secret:
    print("Perfekt, Gratulation!")
elif guess==secret1:
    print("Perfekt, Gratulation!")
elif guess==secret2:
    print("Perfekt, Gratulation!")
elif guess==secret3:
    print("Perfekt, Gratulation!")
elif guess==secret4:
    print("Perfekt, Gratulation!")
else:
    print("Schade. Neuen Versuch starten.")
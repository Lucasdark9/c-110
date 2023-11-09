import random
response = input ("deseja jogar um dado? Responda: y ou n")
while response == "y":
    no=random.randint(1,6)
    if no == 1:
        print(["   "])
        print([" * "])
        print(["   "])
    elif no == 2:
        print(["*   "])
        print(["    "])
        print(["   *"])
    elif no == 3:    
        print(["*   "])
        print(["  * "])
        print(["   *"])
    elif no == 4:    
        print(["*   *"])
        print(["     "])
        print(["*   *"])
    elif no == 5:    
        print(["*   *"])
        print(["  *  "])
        print(["*   *"])
    elif no == 6:    
        print(["*   *"])
        print(["*    *"])
        print(["*   *"])
    response=input("deseja rolar outro dado? y ou n")
print("até a proxima")
    
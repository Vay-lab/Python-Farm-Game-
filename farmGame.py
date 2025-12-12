
#Display Main Menu
class Base_class:
    day=1
    energy=10
    money=20
    LET=0
    POT=0
    Caul=0
    lTime = 2
    pTime = 3
    cTime = 5
    
class Main(Base_class):

    def Main_menu():
        return('''----------------------------------------------------------
    Welcome to Vay's Farm!
    
    You took out a loan to buy a small farm.
    You have 20 days to pay off your debt of $100.
    You might even be able to make a little profit (who knows).
    How successful will you be?
    ----------------------------------------------------------
    1) Start a new game
    2) Load your saved game
    
    0) Exit game''')

    #Option-1 <Start New Game>
    #1.1 (defect with file name)
    def New_Game():
        import string as s
        import random
        name = random.choice(s.ascii_letters)
        Game=['+--------------------------------------------------+\n', 
           f'| Day {Base_class.day}       Energy: {Base_class.energy}         Money: ${Base_class.money }        |\n', 
           '| You have no seeds.                               |\n', 
           '+--------------------------------------------------+\n']
        with open (f"{name}.txt",'w') as file:
            file.writelines(Game)
        with open (f"{name}.txt", 'r') as file:
            content=file.read()
            print(content)

    #Option-2 <Load Saved Game>
    #1.2
    def Resume_Game():
        with open ("Game1.txt", 'r') as file:
            print(file.read())
    #Town menu
    def Town():
        return('''You are in Albatross Town
    --------------------------
    1) Visit Shop
    2) Visit Farm
    3) End Day
    
    9) Save Game
    0) Exit Game
    --------------------------''')

#Visit Shop 
#2.1
class VShop(Base_class):

    def ShopFTime ():
        return('''Welcome to Pierce's Seed Shop!
    What do you wish to buy?
    Seed              Price     Day to Grow      Crop Price
    -------------------------------------------------------
     1) Lettuce        2             2                3
     2) Potato         3             3                6
     3) Cauliflower    5             6                14
    
     0) Leave
    -------------------------------------------------------''')

    def Shop ():
        return('''What do you wish to buy?
    Seed              Price     Day to Grow      Crop Price
    -------------------------------------------------------
     1) Lettuce        2             2                3
     2) Potato         3             3                6
     3) Cauliflower    5             6                14
    
     0) Leave
    -------------------------------------------------------''')

    #seeds (1)
    #Lettuce
    def Lettuce():
        price = 2
        
        print(f"You have ${Base_class.money}")
        
        L = int(input ("How many do you wish to buy? "))
        Base_class.LET+=L
        while Base_class.LET< 0 :
            print("Invalid quantity. Please try again.")
            Base_class.LET= int (input ("How many do you wish to buy? "))
            
        if (price * Base_class.LET) > Base_class.money:
            print("You can't afford that!")
            print(VShop.Shop())     
            
        else:
            Base_class.money -= price * Base_class.LET
            Game1 = ['+--------------------------------------------------+\n',
            f'| Day {Base_class.day}       Energy: {Base_class.energy}         Money: ${Base_class.money}        |\n', 
            f'|    Lettuce  :       {Base_class.LET}                            |\n', 
            f'|    Potato   :       {Base_class.POT}                            |\n', 
            f'|  Cauliflower:       {Base_class.Caul}                            |\n', 
             '+--------------------------------------------------+\n']
            with open ("Game1.txt", 'w') as file:
                file.writelines(Game1)
            with open ("Game1.txt", 'r') as file:
                print(file.read())
            print(VShop.Shop())
    #seeds (2)
    #Potato
    def Potato():
        price = 3
        
        
        print(f"You have ${Base_class.money}")
        
        P = int(input ("How many do you wish to buy? "))
        Base_class.POT+=P
        while Base_class.POT< 0 :
            print("Invalid quantity. Please try again.")
            Base_class.POT = int (input ("How many do you wish to buy? "))
                    
        if (price * Base_class.POT) > Base_class.money:
            print("You can't afford that!")
            print(VShop.Shop())        
            
        else:
            Base_class.money -= price * Base_class.POT
            Game1 = ['+--------------------------------------------------+\n',
            f'| Day {Base_class.day}       Energy: {Base_class.energy}         Money: ${Base_class.money}        |\n', 
            f'|    Lettuce  :       {Base_class.LET}                            |\n', 
            f'|    Potato   :       {Base_class.POT}                            |\n', 
            f'|  Cauliflower:       {Base_class.Caul}                            |\n', 
             '+--------------------------------------------------+\n']
            with open ("Game1.txt", 'w') as file:
                file.writelines(Game1)
            with open ("Game1.txt", 'r') as file:
                print(file.read())
            print(VShop.Shop())
       
    #seeds (3)
    #Cauliflower 
    def Cauliflower():
        price = 5
        
        print(f"You have ${Base_class.money}")
        
        C = int(input ("How many do you wish to buy? "))
        Base_class.Caul+=C
        while Base_class.Caul < 0 :
            print("Invalid quantity. Please try again.")
            Base_class.CAUL = int (input ("How many do you wish to buy? "))
        if (price * Base_class.Caul) > Base_class.money:
            print("You can't afford that!")
            print(VShop.Shop())            
            
        else:
            Base_class.money -= price * Base_class.Caul
            Game1 = ['+--------------------------------------------------+\n',
            f'| Day {Base_class.day}       Energy: {Base_class.energy}         Money: ${Base_class.money}        |\n', 
            f'|    Lettuce  :       {Base_class.LET}                            |\n', 
            f'|    Potato   :       {Base_class.POT}                            |\n', 
            f'|  Cauliflower:       {Base_class.Caul}                            |\n', 
             '+--------------------------------------------------+\n']
            with open ("Game1.txt", 'w') as file:
                file.writelines(Game1)
            with open ("Game1.txt", 'r') as file:
                print(file.read())
            print(VShop.Shop())
#Move options
#2.2.1
#need to deal with energy first
def Move(move):
    global x, y, a, b, c, grid
    if move.upper() == "W":      
        if (y-4) < 2:
            print("You are not allowed to move further.")
        else:
            grid[y][x]=' '
            y-=4
            b-=4
            c-=4
            grid[y][x]='X'
            Base_class.energy-=1

    elif move.upper() == "S":
        
        if (y+4) > 18:
            print("You are not allowed to move further.")
        else:
            grid[y][x]=' '
            y+=4
            b+=4
            c+=4
            grid[y][x]='X'
            Base_class.energy-=1
    elif move.upper() == "A":
        
        if (x-6) < 3:
            print("You are not allowed to move further.")
        else:
            grid[y][x]=' '
            x-=6
            a-=4
            grid[y][x]='X'
            Base_class.energy-=1

    elif move.upper() == "D":
        
        if (x+6) > 27:
            print("You are not allowed to move further.")
        else:
            grid[y][x]=' '
            x+=6
            a+=4
            grid[y][x]='X'
            Base_class.energy-=1

#Plant Seed
#2.2.2
#check if user has seeds first
class Plant_seed(Base_class):
    pDict={}
    def Check():       
        if Base_class.LET > 0 or Base_class.POT > 0 or Base_class.Caul > 0:
            if grid[b][a].isspace():
                return True
            else:
                return False

    def Display_seed():
        print('''-------------------------------------------------------------------------
    Seed          Price     Day to Grow      Crop Price       Available
-------------------------------------------------------------------------''')
        i=0
        
        if Base_class.LET>0:
            plant=f"{i+1}) Lettuce        2             2                3                {Base_class.LET} "
            print(plant)
            Plant_seed.pDict["Lettuce"] = plant
            i+=1
               
        if Base_class.POT>0:
            plant1=f"{i+1}) Potato         3             3                6                {Base_class.POT} "
            print(plant1) 
            Plant_seed.pDict["Potato"] = plant
            i+=1

        if Base_class.Caul>0:
            plant2=f"{i+1}) Cauliflower    5             6                14               {Base_class.Caul} "
            print(plant2) 
            Plant_seed.pDict["Cauliflower"] = plant
            
    def Choose_seed(seed):
        if seed == "Lettuce":
            grid[b][a] = "LET"
            grid[c][x] = f"{Base_class.lTime}"
            Base_class.energy-=1
            Base_class.LET-=1

        elif seed == "Potato":
            grid[b][a] = "POT"
            grid[c][x] = f"{Base_class.pTime}"
            Base_class.energy-=1
            Base_class.POT-=1

        elif seed == "Cauliflower":
            grid[b][a] = "CAU"
            grid[c][x] = f"{Base_class.cTime}"
            Base_class.energy-=1
            Base_class.Caul-=1 
    
    def Plant(boolean):
        
        pList=list(Plant_seed.pDict.keys())
        if boolean == True:
            print("What do you wish to plant?")
            print(Plant_seed.Display_seed())
            ask=int(input("Your choice? "))
            if 0<=ask<=3:
                
                if ask == 1:
                    print(Plant_seed.Choose_seed(pList[0]))
                elif ask ==2:
                    print(Plant_seed.Choose_seed(pList[1]))
                elif ask == 3:
                    print(Plant_seed.Choose_seed(pList[2]))
                else:
                    pass
                    #return to farm
            else:
                print("Invalid input.")
        with open ("hehe.txt", 'w') as file:
            for i in range(len(grid)):
                for j in grid[i]:
                    file.write(j)  
        with open ("hehe.txt", 'r') as file:
            print(file.read())


print(Main.Main_menu())
user_input = int(input("Your choice? "))

#Main menu options
if user_input == 1:
    Main.New_Game()
    Main.Town()
elif user_input == 2:
    Main.Resume_Game()
    Main.Town()
else:
    print("Goodbye!")

#Town menu > Shop
while True:
    option = int(input ("Your choice? "))
    if option == 1:
        Main.Resume_Game()
        print(VShop.ShopFTime())
        ask = int(input ("Your choice? "))
        while ask < 0 or ask > 3:
            print("Invalid input.")
        while True:
            if ask == 1:
                VShop.Lettuce()
                
                ask = int(input ("Your choice? "))
            elif ask == 2:
                VShop.Potato()
                
                ask = int(input ("Your choice? "))
            elif ask == 3:
                VShop.Cauliflower()
                
                ask = int(input ("Your choice? "))
            elif ask == 0:
                print(Main.Town())
                break
                
        
    
    elif option == 2:
    #Visit Farm
    #2.2
        grid = [
            ['+-----+-----+-----+-----+-----+\n'],
            ['|', ' ', '   ', ' ', '|',  ' ', '   ', ' ','|', ' ', '   ', ' ','|',  ' ', '   ', ' ','|', ' ', '   ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['+-----+-----+-----+-----+-----+\n'],
            ['|', ' ', '   ', ' ', '|',  ' ', '   ', ' ','|', ' ', '   ', ' ','|',  ' ', '   ', ' ','|', ' ', '   ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['+-----+-----+-----+-----+-----+\n'],
            ['|', ' ', '   ', ' ', '|',  ' ', '   ', ' ','|', ' ', '   ', ' ','|',  ' ', '   ', ' ','|', ' ', '   ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['+-----+-----+-----+-----+-----+\n'],
            ['|', ' ', '   ', ' ', '|',  ' ', '   ', ' ','|', ' ', '   ', ' ','|',  ' ', '   ', ' ','|', ' ', '   ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['+-----+-----+-----+-----+-----+\n'],
            ['|', ' ', '   ', ' ', '|',  ' ', '   ', ' ','|', ' ', '   ', ' ','|',  ' ', '   ', ' ','|', ' ', '   ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['|', ' ', ' ', ' ',' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|',' ', ' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|', ' ',' ', ' ', ' ', ' ', '|\n'],
            ['+-----+-----+-----+-----+-----+\n']
        ] 
        y=10 #row of X
        x=15 #col of X
        b=9  #row of Plant/HSE
        a=10 #col of Plant/HSE int(x-(x/3))
        c=11 #row of plant's day
        grid [b][a]="HSE"  
        grid [y][x]='X'
        with open ("hehe.txt", 'w') as file:
            for i in range(len(grid)):
                for j in grid[i]:
                    file.write(j)  
        with open ("hehe.txt", 'r') as file:
            print(file.read())
        
        #Move options
    
        while True:
            print(f"Energy: {Base_class.energy}")
            if Plant_seed.Check()!=True:
            
                print("[WSAD] Move\nR)eturn to Town\n")
            else:
                print("[WSAD] Move\nP)lant seed\nR)eturn to Town\n")
            ask = input("Your choice? ")
            if ask.upper() in {"W", "S", "A", "D"}:
                print(Move(ask.upper()))
                with open ("hehe.txt", 'w') as file:
                    for i in range(len(grid)):
                        for j in grid[i]:
                            file.write(j)  
                with open ("hehe.txt", 'r') as file:
                    print(file.read())
                
            elif ask.upper() == 'P':
                check=Plant_seed.Check()
                if check == True:
                    print(Plant_seed.Plant(check))

            elif ask.upper() == 'R':
                break
                print(Town())
            else:
                print("Invalid input.")


    elif option == 3:
        Base_class.day+=1
        Base_class.energy=10
        for i in range(len(grid)):
            for j in grid[i]:
                if j == f"{Base_class.lTime}":
                    j-=1
                elif j == f"{Base_class.pTime}":
                    j-=1
                elif j == f"{Base_class.cTime}":
                    j-=1
    elif option == 0:
        break


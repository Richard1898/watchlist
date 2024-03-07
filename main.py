# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
import json
watchlist_file = open('watchlist.json') 
watchlist = json.load(watchlist_file) 
m={}
while True:
    command = input("\nChoose command(1-8):")
    if command == "1":
        m = {
        "Nosaukums": input("Uzrakstiet Nosaukumu: "),
        "Reitings": int(input("Uzrakstiet Reitingu: ")),
        "Skatiju": input("Uzrakstiet Skatiju(Ja vai Ne): ")
        }
        if 10 >= m["Reitings"] and m["Reitings"]> 0:  
            if 120 >= len(m["Nosaukums"]) and len(m["Nosaukums"])>= 2: 
                watchlist.append(m)
            else:
                print("Inncorrect nosaukums")
        else:
            print("Inncorrect reiting")
    if command == "2":
        c = int(input("Ievadi indeksu kuri grib dzest: "))
        watchlist.pop(c)
        
    if command == "3":
        for x in watchlist:
            if watchlist["Skatiju"] == (x["Ja"]):
                print (watchlist["Skatiju"])
            else:
                pass
    if command == "4":
        for x in watchlist:
            if watchlist["Skatiju"] == (x["Ne"]):
                print (watchlist["Skatiju"])
            else:
                pass
    if command == "5":
        def Reitings(n):
                return int(n["Reitings"])
        watchlist.sort(key = Reitings, reverse=True)
        print(watchlist[:10])
    if command == "6":
        watchlist.clear()
    if command == "7":
        v = input("Ieraksti Kadu filmu grib")
        if v in watchlist["Nosaukums "]:
            print (watchlist["Nosaukums "])
        else:
            print("Neatradu tādu filmu :( ")
    if command == "8":
        with open('watchlist.json', 'w') as outfile:
            json.dump(watchlist, outfile)
            exit()
    
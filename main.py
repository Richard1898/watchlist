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
    command = input("\nChoose command(1-9):")
    if command == "1":
        m = {
        "Nosaukums": input("Uzrakstiet Nosaukumu: "),
        "Reitings": int(input("Uzrakstiet Reitingu: "))
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
        print(watchlist)
        g = int(input("uzrakstiet kuru filmu skatijies: "))
        watchlist[g]['Skatiju'] = 'Ja'
    if command == "4":
        watched = []
        for movie in watchlist:
            if 'Skatiju' in movie and movie['Skatiju'] == 'Ja':
                watched.append(movie)
        print(watched[:20])
    if command == "5":
        not_watched = []
        for movie in watchlist:
            if 'Skatiju' in movie and movie['Skatiju'] == 'Ne':
                not_watched.append(movie)
        print(not_watched[:20])
    if command == "6":
        def Reitings(n):
                return int(n["Reitings"])
        watchlist.sort(key = Reitings, reverse=True)
        print(watchlist[:10])
    if command == "7":
        watchlist.clear()
    if command == "8":
        x = input("uzrakstiet nosaukumu:")
        for movie in watchlist:
            if x in movie["Nosaukums"]:
                print(movie["Nosaukums"])
    if command == "9":
        with open('watchlist.json', 'w') as outfile:
            json.dump(watchlist, outfile)
            exit()
    
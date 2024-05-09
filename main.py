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
add_film={}
while True:
    command = input("\nChoose command(1-9):")
    if command == "1":
        add_film = {
        "Nosaukums": input("Uzrakstiet Nosaukumu: "),
        "Reitings": int(input("Uzrakstiet Reitingu: "))
        }
        if 10 >= add_film["Reitings"] and add_film["Reitings"]> 0:  #валидация рейтинга
            if 120 >= len(add_film["Nosaukums"]) and len(add_film["Nosaukums"])>= 2: #валидация названия
                watchlist.append(add_film)
            else:
                print("Inncorrect nosaukums")
        else:
            print("Inncorrect reiting")
    if command == "2":
        dzest_filmu = int(input("Ievadi indeksu kuri grib dzest: "))
        watchlist.pop(dzest_filmu)
        
    if command == "3":
        print(watchlist)
        watched_film = int(input("uzrakstiet kuru filmu skatijies: "))
        watchlist[watched_film]['Skatiju'] = 'Ja'
    if command == "4":
        watched = []
        for movie in watchlist:#meklejam visas filmus kuras skatijamies
            if 'Skatiju' in movie and movie['Skatiju'] == 'Ja':#saglabajam ka šis filmu skatijam
                watched.append(movie)
        print(watched[:20])
    if command == "5":
        not_watched = []
        for movie in watchlist:#meklejam visas filmus kuras skatijamies
            if 'Skatiju' in movie and movie['Skatiju'] == 'Ne':#saglabajam ka šis filmu ne skatijam
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
        search_film_name = input("uzrakstiet nosaukumu:")
        for movie in watchlist:#meklejam visas filmus nosaukumu
            if search_film_name in movie["Nosaukums"]:#atradam lidzīgu nosaukumu
                print(movie["Nosaukums"])
    if command == "9":
        with open('watchlist.json', 'w') as outfile:
            json.dump(watchlist, outfile)
            exit()
    
import matplotlib.pyplot as plt
import sys
from datetime import datetime, timedelta


#Fonction qui créer une liste de toutes les dates jusqu'au jour
def liste_dates_novembre_jusqu_a_aujourd_hui_formattee():
    # Définir la date de début du mois de novembre 2023
    date_debut = datetime(2023, 9, 23)

    # Obtenir la date actuelle
    date_actuelle = datetime.now()

    # Initialiser la liste des dates formatées
    liste_dates_formattees = []

    # Boucler à travers les jours du mois jusqu'à aujourd'hui
    jour_courant = date_debut
    while jour_courant <= date_actuelle:
        # Formater la date comme une chaîne de caractères "JJ/MM/AA"
        date_formattee = jour_courant.strftime("%d/%m/%y")
        liste_dates_formattees.append(date_formattee)

        # Passer au jour suivant
        jour_courant += timedelta(days=1)

    return liste_dates_formattees


#Choix du bon fichier selon la data demandée sinon interruption
def name_file(data_wanted):
    
    if data_wanted == "Cardio" or data_wanted == "cardio" or data_wanted == "Cardio " or data_wanted == "cardio ":
        name_f = "Cardio_data.txt"
        return name_f, "0"
    elif data_wanted == "Aerobic" or data_wanted == "Aerobic " or data_wanted == "aerobic" or data_wanted == "aerobic ":
        name_f = "Aerobie_data.txt"
        return name_f, "0"
    elif data_wanted == "Cadence" or data_wanted == "Cadence " or data_wanted == "cadence" or data_wanted == "cadence ":
        name_f = "Cadence.txt"
        return name_f, "spm"
    elif data_wanted == "Quit" or data_wanted == "quit":
        sys.exit()
    else :
        print("Error no data !")
        sys.exit()
      
        
#Ouverture du fichier + suppression de la première ligne
def file_open(n_file):
    with open(n_file,"r") as file :
        lines_with_0 = file.readlines()
    lines  = lines_with_0[1:]
    lignes = [l.strip() for l in lines]
    return lignes


#Créer listes pour la date, données1, 2 et 3
def lists_base(L):
    Date = []
    D1 = []
    D2 = []
    D3 = []
    elts = []
    for i in range(len(L)):
        elts = L[i].split(" ")
        Date.append(elts[0])
        D1.append(int(elts[1]))
        D2.append(int(elts[2]))
        D3.append(int(elts[3]))
    return Date, D1, D2, D3


#Créer listes pour la date et données1
def lists_base_cad(L):
    Date = []
    V1 = []
    elts = []
    for i in range(len(L)):
        elts = L[i].split(" ")
        Date.append(elts[0])
        V1.append(int(elts[1]))
    return Date, V1


#Créer un dico de base (date, valeur)
def dico_base(Date, V):
    dico = {}
    for i in range(len(V)):
        dico[Date[i]] = V[i]
    return dico


#Créer la liste de base en rajoutant les jours vides
def goodsizelist(DX, date):
    L = []
    N = len(date)
    for i in range(N):
        if date[i] in DX : 
            L.append(DX[date[i]])
        else :
            L.append(0)
    return L


#Créer la liste de bonne taille et avec les valeurs des jours précedents
def goodlist(L):
    for i in range(1,len(L)):
        if L[i] == 0:
            L[i] = L[i-1]
        else :
            L[i] += L[i-1]


#Créer la liste de bonne taille et avec les valeurs des jours précedents sans additionner
def goodlist_cad(L):
    for i in range(1,len(L)):
        if L[i] == 0:
            L[i] = L[i-1]

                      
#Fonction qui permet de réduire le main
def crea_list(date, D, DATE):
    d_donnee = dico_base(date, D)
    l_vide = goodsizelist(d_donnee, DATE)
    goodlist(l_vide)
    return l_vide


#Fonction qui réduit la liste selon le mois
def months_list(period, date, data1, data2, data3):
    elts = period.split("/")
    elts2 = []
    I = []
    if period == "09/23":
        date = date[:8]
        data1 = data1[:8]
        data2 = data2[:8]
        data3 = data3[:8]
        return date, data1, data2, data3
    for i in range(len(date)):
        elts2 = date[i].split("/")
        if elts2[2] == elts[1] and elts2[1] == elts[0] :
            I.append(i)
    min = I[0]
    max = I[-1]
    date = date[min:max+1]
    data1 = data1[min:max+1]
    data2 = data2[min:max+1]
    data3 = data3[min:max+1]
    return date, data1, data2, data3
    
                   
#Fonction qui réduit la liste selon l'année
def year_list(period, date, data1, data2, data3):
    year = period[2:5]
    elts = []
    I = []                                                                                              
    for i in range(len(date)):
        elts = date[i].split("/")
        if elts[2] == year :
            I.append(i)
    min = I[0]
    max = I[-1]
    date = date[min:max+1]
    data1 = data1[min:max+1]
    data2 = data2[min:max+1]
    data3 = data3[min:max+1]
    return date, data1, data2, data3
        
     
#Permet de lancer le bon programme selon la période
def choose_period(period, date, data1, data2, data3, type, mode, lines):
    if period =="Beginning":
        affichage(type, date, data1, data2, data3)
    elif "/" in period and mode == "Z" :
        date, data1, data2, data3 = months_list(period, date, data1, data2, data3)
        affichage(type, date, data1, data2, data3)
    elif period in ["2023","2024"] and mode == "Z" :
        date, data1, data2, data3 = year_list(period, date, data1, data2, data3)
        affichage(type, date, data1, data2, data3)
    elif "/" in period and mode == "0" :
        Date, D1, D2, D3 = lists_base(lines)
        dico1 = dico_base(Date, D1)
        dico2 = dico_base(Date, D2)
        dico3 = dico_base(Date, D3)
        l1_vide = goodsizelist(dico1, date)
        l2_vide = goodsizelist(dico2, date)
        l3_vide = goodsizelist(dico3, date)
        date, data1, data2, data3 = months_list(period, date, l1_vide, l2_vide, l3_vide)
        goodlist(data1)
        goodlist(data2)
        goodlist(data3)
        affichage(type, date, data1, data2, data3)   
        
    elif period in ["2023","2024"] and mode == "0" :
        Date, D1, D2, D3 = lists_base(lines)
        dico1 = dico_base(Date, D1)
        dico2 = dico_base(Date, D2)
        dico3 = dico_base(Date, D3)
        l1_vide = goodsizelist(dico1, date)
        l2_vide = goodsizelist(dico2, date)
        l3_vide = goodsizelist(dico3, date)
        date, data1, data2, data3 = year_list(period, date, l1_vide, l2_vide, l3_vide)
        goodlist(data1)
        goodlist(data2)
        goodlist(data3)
        affichage(type, date, data1, data2, data3)
         
    elif period == "Quit" or period == "quit" :
        sys.exit()  
        
    else :
        print("Period of time doesn't exist !")
        sys.exit()
        
 
def choose_period_cad(period, date, data1, data2, data3, type, lines):
    if period =="Beginning":
        Date, D1 = lists_base_cad(lines)
        colors = D1
        plt.scatter(Date, D1, c=colors, cmap='plasma_r', linewidths=0.3)
        plt.colorbar(label='SPM')
        plt.plot(Date, D1, color = "navy", linewidth = 0.5)
        plt.title("Cadence")
        plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
        plt.xlabel("Days")
        plt.ylabel("spm")
        plt.show()
        
    elif "/" in period :
        Date, D1 = lists_base_cad(lines)
        dico1 = dico_base(Date, D1)
        dico2 = dico_base(Date, data2)
        dico3 = dico_base(Date, data3)
        l1_vide = goodsizelist(dico1, date)
        l2_vide = goodsizelist(dico2, date)
        l3_vide = goodsizelist(dico3, date)
        date, data1, data2, data3 = months_list(period, date, l1_vide, l2_vide, l3_vide)
        goodlist_cad(data1)
        affichage(type, date, data1, data2, data3)   
        
    elif period in ["2023","2024"] :
        Date, D1 = lists_base_cad(lines)
        dico1 = dico_base(Date, D1)
        dico2 = dico_base(Date, data2)
        dico3 = dico_base(Date, data3)
        l1_vide = goodsizelist(dico1, date)
        l2_vide = goodsizelist(dico2, date)
        l3_vide = goodsizelist(dico3, date)
        date, data1, data2, data3 = year_list(period, date, l1_vide, l2_vide, l3_vide)
        goodlist_cad(data1)
        affichage(type, date, data1, data2, data3)
         
    elif period == "Quit" or period == "quit" :
        sys.exit()  
        
    else :
        print("Period of time doesn't exist !")
        sys.exit()          


#Fonction qui permet d'afficher les données
def affichage(type, date, data1, data2, data3):
    if type == "Cardio" or type == "Cardio " or type == "cardio" or type == "cardio ":
        plt.plot(date, data1, label = 'Aerobic', color = "#00D803")
        plt.plot(date, data2, label = 'Threshold', color = "#F4811B")
        plt.plot(date, data3, label = 'Maximum', color = "#E61D1D")
        plt.title("Cardio")
        plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
        plt.legend()
        plt.xlabel("Days")
        plt.ylabel("Minutes")
        plt.show()
        
    elif type =="Aerobic" or type == "Aerobic " or type == "aerobic" or type == "aerobic ":
        plt.plot(date, data1, label = 'Low aerobic', color = "#19DBDE")
        plt.plot(date, data2, label = 'High aerobic', color = "#F4811B")
        plt.plot(date, data3, label = 'Anaerobic', color = "#7F16CD")
        plt.title("Aerobic")
        plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
        plt.legend()
        plt.xlabel("Days")
        plt.ylabel("Minutes")
        plt.show()
        
    elif type =="Cadence" or type == "Cadence " or type == "cadence" or type == "cadence ":
        plt.scatter(date, data1, c=data1, cmap='plasma_r', linewidths=0.3)
        plt.plot(date, data1, color = "navy", linewidth = 0.5)
        plt.colorbar(label='SPM')
        plt.title("Cadence")
        plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
        plt.xlabel("Days")
        plt.ylabel("spm")
        plt.show()
        
              
#Fonction principale
def main():
    print("Press enter !")
    while input() != "Quit" or input() != "quit" :
        print("What data would you like to see ? (Cardio, Aerobic or Cadence)")
        type = input()
        name_f, cad = name_file(type)
        lines =  file_open(name_f)                                                                                                                                                                                                                                                                                        
        dates_formattees = liste_dates_novembre_jusqu_a_aujourd_hui_formattee() # liste de toutes les dates depuis le 23/09/23
        if cad == "0" :    
            Date, D1, D2, D3 = lists_base(lines)
            list1 = crea_list(Date, D1, dates_formattees)#listes du 23/09/23 à ajd completes
            list2 = crea_list(Date, D2, dates_formattees)
            list3 = crea_list(Date, D3, dates_formattees)
        elif cad == "spm" :
            Date, C = lists_base_cad(lines)
            list_cad = crea_list(Date, C, dates_formattees)
            V1 = []
            V2 = []
            
               
        print("Over what period of time ? (Beginning(23th Sept 2023), 202X or just a month (mm/yy))")
        period = input()
        mode = " "
        if period == "Quit" or period == "quit" :
            sys.exit()
        elif period != "Beginning" and cad == "0":
            print("Zoom or Start at 0 ? (Z or 0)")
            mode = input()
            if mode == "Quit" or mode == "quit":
                sys.exit()
        if cad == "0" :
            choose_period(period,dates_formattees, list1, list2, list3, type, mode, lines)
        elif cad == "spm" :
            choose_period_cad(period,dates_formattees, list_cad, V1, V2, type, lines)
        print("Press enter !")
    
    
            


#Lancement du main()
if __name__=="__main__":
    main()
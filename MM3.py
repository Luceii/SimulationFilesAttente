import ciw
#Création de système N
N = ciw.create_network(
    arrival_distributions=[ ciw.dists.Exponential(0.2) ], # la distribution des inter-arrivées
    service_distributions=[ ciw.dists.Exponential(0.1)], # la distribution de temps de service 
    number_of_servers=[3] # le nombre de serveur
)
ciw.seed(1) #Définition de seed 
Q = ciw.Simulation(N)  #Créer l'objet de simulation
Q.simulate_until_max_time(480, progress_bar=True) # 480min est le temps maximum de simulation

#Récupérer la liste de tous les individus qui ont fini leur service à la fin de la simulation
print ("***************************************************************************")
print("Liste de tous les clients qui ont fini leur services :")
print ("***************************************************************************")
print  (Q.nodes[-1].all_individuals)

#Récupérer la liste de tous les individus qui sont en attente ou en service
print ("***************************************************************************")
print("Liste de tous les clients qui sont en service :")
print ("***************************************************************************")
print (Q.nodes[1].all_individuals)

#Récupérer les informations d'un seul client (le premier qui a terminé le service par exemple)
print ("***************************************************************************")
print("Les informations d'un client :")
print ("***************************************************************************")
client=Q.nodes[-1].all_individuals[0]
informations= client.data_records[0]
print ("client :  "+str(client))
print("Date d'arrivée:  "+str(informations.arrival_date))
print("Durée d'attente:  "+str(informations.waiting_time))
print("Date de début de service:  "+str(informations.service_start_date))
print("Durée de service:  "+str(informations.service_time))
print("Date de fin de service:  "+str(informations.service_end_date))
print("Date de quitter le système:  "+str(informations.exit_date))

#Récupérer les infrmations de tous les clients
print ("********************************************************************************************************")
print("Les informations de tous les client:")
print ("********************************************************************************************************")
print ("client\t\t Date d'arrivée\t\t Durée d'attente\t Date début de service\t Durée de service\t Fin de service ")
for client in Q.nodes[-1].all_individuals:
	data=client.data_records[0]
	print(str(client)+"\t\t"+str(round(data.arrival_date,3))+"\t\t\t"+str(round(data.waiting_time,3))+
    "\t\t\t"+str(round(data.service_start_date,3))+"\t\t\t"+str(round(data.service_time,3))+
    "\t\t\t"+str(round(data.service_end_date,3)))

import ciw

N = ciw.create_network(
    arrival_distributions=[ ciw.dists.Exponential(5) ], 
    service_distributions=[ ciw.dists.Exponential(7.5)], 
    number_of_servers=[1] # le nombre de serveur
)
ciw.seed(1) 
Q = ciw.Simulation(N)  
#Supposons le service est en cours pendant 8h/j 5j/sem pendant un mois 8X5X4 = 1200
Q.simulate_until_max_time(200, progress_bar=True) 
data=Q.get_all_records()

#Calcul de la durée moyenne de service
service_times=[client.service_time for client in data ]
moy_service_times=sum(service_times)/ len(service_times)
print ("La durée moyenne de service est : "+str(round (moy_service_times, 3)))

#Calcul de la durée moyenne d'attente
waiting_times=[client.waiting_time for client in data ]
moy_waiting_times=sum(waiting_times)/ len(waiting_times)
print ("La durée moyenne d'attente est : "+str (moy_waiting_times))

#Calcul de la durée moyenne dans le système
system_times=[client.service_end_date-client.arrival_date for client in data ]
moy_system_times=sum(system_times)/ len(system_times)
print ("La durée moyenne dans le système est: "+str(round(moy_system_times, 3)))
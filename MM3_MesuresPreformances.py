import ciw
import matplotlib.pyplot as plt

N = ciw.create_network(
    arrival_distributions=[ ciw.dists.Exponential(0.2) ], 
    service_distributions=[ ciw.dists.Exponential(0.1)], 
    number_of_servers=[3] # le nombre de serveur
)
ciw.seed(1) 
Q = ciw.Simulation(N)  
Q.simulate_until_max_time(480, progress_bar=True) 

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
print ("La durée moyenne dans le système est: "+str(round(moy_system_times,3)))


#plt.hist(service_times);
#plt.show()

#plt.hist(waiting_times);
#plt.show()

plt.hist(system_times);
plt.show()

print ("Pourcentage d'activité des serveurs :  "+str(Q.transitive_nodes[0].server_utilisation))

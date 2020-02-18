import ciw
import matplotlib.pyplot as plt
N = ciw.create_network(
    arrival_distributions=[ ciw.dists.Exponential(1) ], # la distribution des inter-arrivées
    service_distributions=[ ciw.dists.Exponential(1/6)], # la distribution de temps de service 
    number_of_servers=[2], # le nombre de serveur
    queue_capacities=[7] #taille de la file d'attente
)

ciw.seed(1)
Q=ciw.Simulation(N)
Q.simulate_until_max_time (8,progress_bar=True)
data=Q.get_all_records()

service_times=[client.service_time for client in data ]
moyenne_service_times=sum(service_times)/ len(service_times)
print ("La durée moyenne de service est: "+str(round(moyenne_service_times,3)))

waiting_times=[client.waiting_time for client in data ]
moyenne_waiting_times=sum(waiting_times)/ len(waiting_times)
print ("La durée moyenne d'attente est: "+str(round(moyenne_waiting_times,3)))

system_times=[client.service_end_date-client.arrival_date for client in data ]
moyenne_system_times=sum(system_times)/ len(system_times)
print ("La durée moyenne dans le système est: "+str(round(moyenne_system_times,3)))

print ("Le nombre de clients durant les 8h est:  "+str(len(Q.get_all_records())))
print ("Le nombre de clients rejetés pendant les 8h est:  "+str(len(Q.rejection_dict[1][0])))
print ("Le pourcentage de rejet est: "+str(round(len(Q.rejection_dict[1][0])/len(Q.get_all_records()) *100,2))+ "%")
print ("La liste des dates ou des clients ont été rejetés:")
print (Q.rejection_dict[1][0])
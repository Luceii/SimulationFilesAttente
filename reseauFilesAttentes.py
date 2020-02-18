import ciw

N = ciw.create_network(
   arrival_distributions=[ciw.dists.Exponential(0.3), # 0.3=1/18 aliments froids 
                           ciw.dists.Exponential(0.2), # 0.2=1/12  aliments chauds
                           ciw.dists.NoArrivals()],
    service_distributions=[ciw.dists.Exponential(1.0), # 1 minute
                           ciw.dists.Exponential(0.4), #  1/2.5 min
                           ciw.dists.Exponential(0.5)], #  1/2 min
    routing=[[0.0, 0.3, 0.7],
             [0.0, 0.0, 1.0],
             [0.0, 0.0, 0.0]],
     number_of_servers=[1, 2, 2]
 )
ciw.seed(1)
Q=ciw.Simulation(N)
Q.simulate_until_max_time (200,progress_bar=True)

completed_custs = []
rslt = Q.get_all_records()
num_completed = len([r for r in rslt if r.node==3 and r.arrival_date < 180])
completed_custs.append(num_completed)
moyenne_client_system=sum(completed_custs) / len(completed_custs)
print ("le nombre moyen de clients ayant transité par le système: "+str(moyenne_client_system))


data=Q.nodes[-1].all_individuals
#test=[d.data_records[0].waiting_time for d in data]
#print (test)
waiting_times=[client.data_records[0].waiting_time for client in data ]
moyenne_waiting_times=sum(waiting_times)/ len(waiting_times)
print ("La durée moyenne d'attente est: "+str(round(moyenne_waiting_times,3)))
system_times=[client.data_records[0].service_end_date-client.service_start_date for client in data ]
moyenne_system_times=sum(system_times)/ len(system_times)
print ("La durée moyenne dans le système est: "+str(round(moyenne_system_times,3)))
system_times=[client.service_end_date-client.arrival_date for client in data ]
moyenne_system_times=sum(system_times)/ len(system_times)
print ("La durée moyenne dans le système est: "+str(round(moyenne_system_times,3)))
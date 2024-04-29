class SearchProblem: # Problema di ricerca generico
    def __init__(self, init, goal, graph, charging_stations, min_battery_at_goal):
        self.init = init
        self.goal = goal
        self.graph = graph
        self.charging_stations = charging_stations
        self.min_battery_at_goal = min_battery_at_goal

    # def getSuccessors(self, state): # MultiDiGraph
    #     electric_constant = 0.05
    #     successors = set()
    #     for neighbor, edge_data in self.graph[state].items():
    #         action = (state, neighbor)
    #         distance = edge_data[list(edge_data.keys())[0]]['length']
    #         speed = edge_data[list(edge_data.keys())[0]].get('speed_kph', 50)  # Velocità in km/h
    #         energy_consumed = electric_constant * (distance / 1000) * speed # k * d(km) * v(km/h) = kWh * °C
    #         time = edge_data[list(edge_data.keys())[0]]['travel_time']
    #         successors.add((action, neighbor, energy_consumed, time))
    #     return successors

    # def getSuccessors(self, state): #DiGraph
    #     # electric_constant = 0.05
    #     electric_constant = 0.5
    #     successors = set()
    #     for neighbor, edge_data in self.graph[state].items():
    #         action = (state, neighbor)
    #         distance = edge_data.get('length', 100)
    #         speed = edge_data.get('speed_kph', 50)  # Velocità in km/h
    #         energy_consumed = electric_constant * (distance / 1000) * speed # k * d(km) * v(km/h) = kWh * °C
    #         time = edge_data.get('travel_time', 10)
    #         successors.add((action, neighbor, energy_consumed, time))
    #     return successors

    # def getSuccessors(self, state):
    #     return set(self.graph[state].keys())

    def getSuccessors(self, state): #DiGraph
        electric_constant = 0.06
        # electric_constant = 1
        successors = set()
        for neighbor in self.graph.neighbors(state):
            action = (state, neighbor)
            distance = self.graph.edges[state, neighbor].get('length', 100) # Distanza in metri
            speed = self.graph.edges[state, neighbor].get('speed_kph', 50)  # Velocità in km/h
            energy_consumed = electric_constant * (distance / 1000) * speed # k * d(km) * v(km/h) = kWh * °C

            time = self.graph.edges[state, neighbor].get('travel_time', 10) # Tempo di percorrenza in secondi
            successors.add((action, neighbor, energy_consumed, time))
        return successors

    # def getSuccessors(self, state): # Ritorna i successori di uno stato
    #     successors = set() # Insieme dei successori
    #     for neighbor in self.graph.neighbors(state): # Per ogni vicino dello stato
    #         action = (state, neighbor)
    #         # Per MultiGraph, potrebbe essere necessario specificare la chiave per l'arco
    #         # Se il grafo non è un MultiGraph, usa il seguente codice:
    #         distance = self.graph.edges[state, neighbor].get('length', 1) # Calcola la distanza
    #         # Se il grafo è un MultiGraph, usa il seguente codice:
    #         # for key in self.graph[state][neighbor]:
    #         #     distance = self.graph[state][neighbor][key].get('length', 1)
    #         successors.add((action, neighbor, distance))
    #     return successors

    def isGoal(self, state, battery_level): # Verifica se uno stato è l'obiettivo e la batteria è sufficiente
        return state == self.goal and battery_level >= self.min_battery_at_goal

    def is_charging_station(self, state): # Verifica se uno stato è una stazione di ricarica
        return state in self.charging_stations

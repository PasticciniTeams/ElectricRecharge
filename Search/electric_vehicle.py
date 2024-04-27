from ASTAR import AStar, AstarNode
from queue import PriorityQueue

class ElectricVehicleNode(AstarNode):
    def __init__(self, state, parent=None, action=None, g=0, h=0, battery=100, temperature=20):
        super().__init__(state, parent, action, g)
        self.battery = battery
        self.temperature = temperature
        self.charging_time = 0  # Aggiunto attributo per il tempo di ricarica
        self.h = h

    def __lt__(self, other):
        # Considera sia il tempo di viaggio che il tempo di ricarica
        # return (self.g + self.h + self.charging_time, self.battery) < (other.g + other.h + other.charging_time, other.battery)
        return (self.g + self.h + self.charging_time) < (other.g + other.h + other.charging_time)

class ElectricVehicleAStar(AStar):

    def __init__(self, graph, heuristic, view=False, battery_capacity=100, min_battery=20, temperature=20):
        super().__init__(heuristic, view)
        self.graph = graph
        self.battery_capacity = battery_capacity
        self.min_battery = min_battery
        self.temperature = temperature
        self.charging_power = 22  # Potenza di ricarica in kW
        

    def solve(self, problem):
        reached = {}
        frontier = PriorityQueue()
        frontier.put(ElectricVehicleNode(problem.init, h=self.heuristic(problem.init, problem.goal), battery=self.battery_capacity))
        reached[(problem.init, self.battery_capacity)] = 0 # Dizionario degli stati raggiunti
        self.reset_expanded()
        while not frontier.empty():
            n = frontier.get()
            if problem.isGoal(n.state, n.battery):
                return self.extract_solution(n)
            for action, s, cost, time in problem.getSuccessors(n.state):
                new_battery = n.battery - (cost/self.temperature)
                if new_battery > 0:
                    charging_time = 0
                    if problem.is_charging_station(n.state):
                        desired_battery_level = 50
                        if desired_battery_level > n.battery:
                            charging_time = (desired_battery_level - n.battery) / self.charging_power
                            new_battery = desired_battery_level
                    new_state = (s, new_battery)
                    new_g = n.g + time + charging_time
                    if new_state not in reached or new_g < reached[new_state]:
                        self.update_expanded(s)
                        reached[new_state] = new_g
                        new_h = self.heuristic(s, problem.goal, self.graph)
                        frontier.put(ElectricVehicleNode(s, n, action, new_g, new_h, new_battery))
        return None
    
    def calculate_desired_battery_level(self, current_state, next_state, problem):
        # Imposta un livello di carica desiderato fisso per semplicità
        desired_battery_level_percentage = 80  # Livello di carica desiderato in percentuale della capacità totale
        # Calcola il livello di carica desiderato in termini di capacità della batteria
        desired_battery_level_kwh = (desired_battery_level_percentage / 100) * self.battery_capacity
        return desired_battery_level_kwh
    
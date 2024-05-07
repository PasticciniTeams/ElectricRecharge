# EVOPT-Maps

EVOPT Maps is a project developed as a university assignment for the "Intelligent Systems" course. The project leverages the osmnx library to implement real-world streets and simulate the journey of an electric vehicle.

## Introduction

EVOPT Maps aims to develop a system for electric vehicle charging. It provides a user-friendly interface for users to automatically locate and reserve charging stations.

## Features

- Download real-world map with real information
- Automate searching and locating charging stations
- Choose the battery percentage to have at the end of the journey

## Installation

To install and run the EVOPT-Maps project, follow these steps:

1. Clone the repository: 

```bash
git clone https://github.com/PasticciniTeams/EVOPT-Maps.git
```

2. Install the required dependencies: 

```bash
pip3 install folium
pip3 install osmnx
pip3 install numpy
pip3 install geopy
pip3 install scikit-learn
pip3 install customtkinter
```

3. Run the program: 

```bash
python3 gui.py
```

## Usage

1. Clone the repository to your local machine.
2. Install the necessary dependencies.
3. Run the program and specify the parameters for vehicle and location.
4. The program will then download the map and find the best route for your vehicle.
5. Open path.html to view the map with the optimal route.

## UI examples

![GUI preview](https://github.com/PasticciniTeams/EVOPT-Maps/master/example/gui_example.png)
![MAPS preview](https://github.com/PasticciniTeams/EVOPT-Maps/master/example/maps_example.png)

## Documentation

The documentation is available [here](https://raw.githack.com/PasticciniTeams/EVOPT-Maps/main/docs/_build/html/index.html).

## License

Everything used inside the project is free license!

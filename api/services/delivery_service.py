from typing import Dict, List, Tuple, Any
import requests
import heapq
import networkx as nx
from api.models.models import DeliveryCreate, DeliveryOut, DeliveryInDB


def get_time_between_coordinates():
    api_url = "https://mocki.io/v1/10404696-fd43-4481-a7ed-f9369073252f"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        G = nx.MultiDiGraph()

        # Add edges with time as weight
        for start, destinations in data.items():
            for end, time in destinations.items():
                G.add_edge(start, end, time=float(time))

        return G
    else:
        # Manejar el error de alguna manera
        pass


def get_movement_time(start, end, graph):
    # Check that the start and end points are valid
    if start not in graph:
        raise ValueError("Invalid start position")
    if end not in graph:
        raise ValueError("Invalid end position")

    # Initialize the heap and visited set
    heap = [(0, start)]
    visited = set()

    # Loop until the heap is empty
    while heap:
        # Pop the smallest cost point from the heap
        current_cost, current_point = heapq.heappop(heap)

        # Check if we've reached the end point
        if current_point == end:
            return current_cost

        # Add the current point to the visited set
        visited.add(current_point)

        # Loop over the neighbors of the current point
        for neighbor, cost in graph[current_point].items():
            # Skip neighbors that have already been visited
            if neighbor in visited:
                continue

            # Calculate the new cost to reach the neighbor
            new_cost = current_cost + cost[0]["time"]

            # Add the neighbor to the heap
            heapq.heappush(heap, (new_cost, neighbor))

    # If we reach here, there is no path between the start and end points
    raise ValueError("No path between start and end points")


from typing import Tuple


def get_delivery_path(start: str, pickup: str, destination: str) -> tuple[str, float]:
    # Get the graph of travel times between positions
    graph = get_time_between_coordinates()

    # Find shortest path from start to pickup
    path_1 = nx.shortest_path(graph, start, pickup, weight='time')

    # Find shortest path from pickup to destination
    path_2 = nx.shortest_path(graph, pickup, destination, weight='time')

    # Combine the two paths into a single route
    route = list(path_1) + path_2[1:]

    # Calculate the time for each segment of the route
    total_time = 0
    route_times = []
    for i in range(len(route) - 1):
        start_pos = route[i]
        end_pos = route[i + 1]
        segment_time = get_movement_time(start_pos, end_pos, graph)
        total_time += segment_time
        route_times.append(segment_time)

    # Convert the route to a string
    route_str = ",".join(route)

    return route_str, total_time


def get_last_deliveries() -> List[DeliveryInDB]:
    """Returns a list of the last 10 deliveries."""
    # TODO: Implement this function to retrieve the last 10 deliveries from a database or file
    return []


def create_delivery_service(delivery_create: DeliveryCreate) -> DeliveryOut:
    """Creates a delivery based on the provided input and returns the delivery details."""
    # TODO: Implement the creation of a delivery using the input parameters and get_delivery_path function
    start = delivery_create.start
    pickup = delivery_create.pickup
    destination = delivery_create.destination
    route, time = get_delivery_path(start, pickup, destination)
    delivery_out = DeliveryOut(start=start, pickup=pickup, destination=destination, route=route, time=time)
    return delivery_out


def list_deliveries_service() -> List[DeliveryInDB]:
    """Returns a list of all deliveries."""
    # TODO: Implement this function to retrieve all deliveries from a database or file
    return []


def get_delivery_service(delivery_id: int) -> DeliveryInDB:
    """Returns the details of a specific delivery."""
    # TODO: Implement this function to retrieve a specific delivery from a database or file
    return None

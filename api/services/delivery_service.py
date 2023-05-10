from typing import Dict, List, Tuple
import requests

from api.models.models import DeliveryCreate, DeliveryOut, DeliveryInDB


def get_all_possible_moves() -> Dict[str, Dict[str, float]]:
    """Returns all possible moves between chessboard coordinates."""
    res = requests.get("https://mocki.io/v1/10404696-fd43-4481-a7ed-f9369073252f")
    return res.json()


def get_delivery_path(start: str, pickup: str, destination: str) -> Tuple[str, float]:
    """Returns the fastest delivery path and time elapsed."""
    # Get all possible moves
    all_moves = get_all_possible_moves()

    # Dijkstra's shortest path algorithm
    distances = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != destination:
        visited.add(current_node)
        destinations = all_moves[current_node]
        weight_to_current_node = distances[current_node][1]

        for next_node, weight in destinations.items():
            if next_node not in visited:
                weight = float(weight)
                distance = weight_to_current_node + weight

                if distances.get(next_node):
                    if distances[next_node][1] > distance:
                        distances[next_node] = (current_node, distance)
                else:
                    distances[next_node] = (current_node, distance)

        next_destinations = {node: distance for node, distance in distances.items() if node not in visited}
        if not next_destinations:
            return None, None

        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Get the delivery path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = distances[current_node][0]
        current_node = next_node
    path = path[::-1]

    # Calculate the time elapsed
    time_elapsed = distances[destination][1]

    # Return the delivery path and time elapsed
    delivery_path = '-'.join(path)
    return delivery_path, time_elapsed


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

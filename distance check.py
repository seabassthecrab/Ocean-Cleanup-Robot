from math import radians, sin, cos, sqrt, atan2

#Haversine formula to calculate the distance between two sets of coordinates:
def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert coordinates to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Calculate differences
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    # Radius of earth in kilometers. Use 3956 for miles
    radius = 6371000.0

    # Calculate and return distance
    distance_m = radius * c
    return distance_m

#publish distance to MQTT topic?
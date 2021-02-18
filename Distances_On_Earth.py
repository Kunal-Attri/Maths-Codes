from math import radians, sin, cos, acos

from Basic_Functions import get_float

print('This code calculates distance between any two coordinates on earth. Provide following data.')
while True:
    print("Input coordinates of two points:")
    start_lat = radians(get_float("Starting latitude: "))
    start_lon = radians(get_float("Starting longitude: "))
    end_lat = radians(get_float("Ending latitude: "))
    end_lon = radians(get_float("Ending longitude: "))

    dist = 6371.01 * acos(sin(start_lat) * sin(end_lat) + cos(start_lat) * cos(end_lat) * cos(start_lon - end_lon))
    print(f"The distance is {dist} km.")

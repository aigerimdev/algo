# Problem 1: Closest Delivery Locations
# The story:
# You’re a delivery driver. Your warehouse is at point (0, 0).
# There are many delivery locations with coordinates like (x, y).
# You can only go to X locations.
# You want to pick the X closest locations.
# What to do:
# Find the distance of each location from (0, 0) using:
# distance = x² + y² (don’t need square root)
# Pick the X locations with the smallest distances.
# Input:
# A list of coordinates: [[1, 2], [3, 4], [1, -1]]
# A number: X = 2 (how many to pick)
# Output:
# Return the X closest points, like [[1, -1], [1, 2]]

def closest_locations(locations, X):
    # Step 1: Make a list of (distance, location)
    distance_list = []
    for loc in locations:
        x = loc[0]
        y = loc[1]
        distance = x * x + y * y  # No need to do square root
        distance_list.append((distance, loc))
    
    # Step 2: Sort by distance (smallest first)
    distance_list.sort()
    
    # Step 3: Pick the first X locations
    result = []
    for i in range(X):
        result.append(distance_list[i][1])  # Take only the location part
    
    return result
locations = [[1, 2], [3, 4], [1, -1]]
X = 2
print(closest_locations(locations, X))
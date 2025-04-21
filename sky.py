def see_building(buildings):
    result = []
    max_high = 0
    
    for building in buildings:
        if building > max_high:
            max_high = building
            result.append(building)
    return result
print(see_building([1, 3, 2, 5, 3, 7]))
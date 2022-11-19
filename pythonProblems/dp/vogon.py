def vogon(arr_len: int, destroyer_machine_cost: int):
    planets = [int(x) for x in input().split(" ")]
    orbit_map = {}
    for eachplanet in planets:  # O(n)
        if eachplanet in orbit_map:
            orbit_map[eachplanet] += 1
        else:
            orbit_map[eachplanet] = 1
    min_cost = 0
    for eachkey in orbit_map:
        min_cost += destroyer_machine_cost if destroyer_machine_cost < orbit_map[eachkey] else orbit_map[eachkey]
    return min_cost


if __name__ == '__main__':
    test_cases = int(
        input())
    for i in range(test_cases):
        arr_len, machine_cost = [int(x) for x in input().split(" ")]
        print(vogon(arr_len, machine_cost))

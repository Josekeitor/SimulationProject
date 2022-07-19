def randomNumber(seed, a, c, m):
    return ((a * seed) + c) % m

def randomNumbers(seed, a, c, m, i):
    numbers = []
    seeds = [seed]
    for j in range(i):
        number = randomNumber(seeds[j], a, c, m)
        numbers.append(number / m)
        seeds.append(number)

    return numbers



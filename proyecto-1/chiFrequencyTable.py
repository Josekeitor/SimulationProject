import math

def getChiFrequencyTable(decimals, file_name, classes, interval, start, end):
    file_data = open(file_name, 'r')
    raw_data = []

    for element in file_data.readlines():
        raw_data.append(round(float(element), decimals))


    min_num = start
    max_num = end

    factor = 10 ** decimals

    raw_interval = (max_num - min_num) / classes

    if not interval:
        interval = math.ceil(raw_interval * factor) / factor

    results = {}
    categories = []
    category_strings = []

    for i in range(classes):
        results[i] = 0
        lower_bound = round((min_num + interval * i), decimals)
        upper_bound = round(min_num + interval * (i + 1), decimals)
        categories.append((lower_bound, upper_bound, i))
        category_strings.append('[' + str(lower_bound) + ' , ' + str(upper_bound) + ']')

    for data_point in raw_data:
        for category in categories:
            if data_point >= category[0] and data_point < category[1]:
                results[category[2]] += 1

    return results

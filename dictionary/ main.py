populations = {'New York': 8467513, 'Los Angeles': 3849297,
               'Chicago': 2696555, 'Houston': 23288250,
               'Phoenix': 1624569, 'Philadelphia': 1576251}

largest = {k:v for k,v in populations.items() if v > 2000000}

print(largest)
# {'New York': 8467513, 'Los Angeles': 3849297,
# 'Chicago': 2696555, 'Houston': 23288250}
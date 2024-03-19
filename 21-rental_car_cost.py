def rental_car_cost(d):
    return d * 40 - (50 if d >= 7 else 20 if d >=3 else 0)
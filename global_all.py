def calc_speed(time: float, distance: float) -> float:
    """
        time - время(часы)
        distance - растояние(киллометры)
        speed - скорость(км/ч)
    """
    speed = distance / time
    return speed


user_time = input("Назовите время(часы):")
user_time = int(user_time)

user_distance = input("Назовите растояние(киллометры):")
user_distance = int(user_distance)

speed = calc_speed(user_time, user_distance)
print(calc_speed)
import time
import threading
from piosdk import Pioneer
from edubot_sdk import EdubotGCS

drone_0 = Pioneer(ip="127.0.0.1", mavlink_port=8002)
drone_1 = Pioneer(ip="127.0.0.1", mavlink_port=8000)
drone_2 = Pioneer(ip="127.0.0.1", mavlink_port=8001)
drone_3 = Pioneer(ip="127.0.0.1", mavlink_port=8003)

rts_1 = EdubotGCS(ip="127.0.0.1", mavlink_port=8005)
rts_2 = EdubotGCS(ip="127.0.0.1", mavlink_port=8004)

rts = [rts_1, rts_2]

barrier = [[0.6, -0.1], [-1.87, -0.52], [-3, 1.6], [3, 1]]  # центры преград

start_places = [[-1.85, 3.4], [1.85, 3.4]]  # стартовые площадки

log_centres = [[-3.3, -0.2], [-0.1, 2.3]]  # логические центры

shops = [[3.17, -0.44], [-0.18, -2.28]]  # магазины

localities = [[-3.5, 3.5], [3.7, 3.5], [-3.5, -2], [3.5, -2]]  # координаты нас пунктов


# rts_1.get_local_position_lps()
# def point_reached(self):   """ Была ли достигнута предыдущая заданная точка """

def ooo():
    print()
    return


threads = [threading.Thread(target=ooo) for _ in range(2)]


# ДЛЯ РТС1

def route_rts_1():
    # обходим преграду 1
    x = barrier[2][0] - 1
    y = barrier[2][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    # едем в логический центр
    x = log_centres[0][0]
    y = log_centres[0][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    # обходим преграду 2
    x = localities[2][0] - 0.8
    y = localities[2][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    x = localities[2][0]
    y = localities[2][1] - 0.8
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    # едем в магазин
    x = shops[1][0]
    y = shops[1][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(5)

    # обходим преграды
    x = localities[2][0]
    y = localities[2][1] - 0.8
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    x = localities[2][0] - 0.8
    y = localities[2][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    x = barrier[2][0] - 0.8
    y = barrier[2][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)

    # едем домой
    x = start_places[0][0]
    y = start_places[0][1]
    rts_1.go_to_local_point(x, y)
    while not rts_1.point_reached():
        rts_1.go_to_local_point(x, y)
    time.sleep(3)


# ДЛЯ РТС 2

def route_rts_2():
    # едем в логический центр
    x = log_centres[1][0]
    y = log_centres[1][1]
    rts_2.go_to_local_point(x, y)
    while not rts_2.point_reached():
        rts_2.go_to_local_point(x, y)
    time.sleep(3)
    # обходим преграду 1
    rts_2.go_to_local_point(x, y)
    x = barrier[3][0] + 1
    y = barrier[3][1] + 0.7
    while (rts_2.point_reached() == False):
        rts_2.go_to_local_point(x, y)
    time.sleep(3)

    # едем в магазин
    x = shops[0][0]
    y = shops[0][1]
    rts_2.go_to_local_point(x, y)
    while not rts_2.point_reached():
        rts_2.go_to_local_point(x, y)
    time.sleep(3)
    # обходим преграды
    x = barrier[3][0] + 1
    y = barrier[3][1] + 0.7
    rts_2.go_to_local_point(x, y)
    while not rts_2.point_reached():
        rts_2.go_to_local_point(x, y)
    time.sleep(3)

    # едем в логический центр
    x = log_centres[1][0]
    y = log_centres[1][1]
    rts_2.go_to_local_point(x, y)
    while not rts_2.point_reached():
        rts_2.go_to_local_point(x, y)
    time.sleep(3)

    # едем домой
    x = start_places[1][0]
    y = start_places[1][1]
    rts_2.go_to_local_point(x, y)
    while not rts_2.point_reached():
        rts_2.go_to_local_point(x, y)
    time.sleep(3)


# добавляем потоки
thread_RTS_1 = threading.Thread(target=route_rts_1)
thread_RTS_2 = threading.Thread(target=route_rts_2)

thread_RTS_1.start()
thread_RTS_2.start()

drones = [drone_0, drone_1, drone_2, drone_3]

localities = [[-3.5, 3.5], [3.7, 3.5], [-3.5, -2], [3.5, -2]]  # координаты нас пунктов
bases = [[-1.5, 1.3], [1.5, 1.2], [-1.5, -1.4], [1.4, -1.4]]  # координаты баз

plan = [[0, 1, 2, 3],  # план полетов
        [0, 1, 2, 3],
        [0, 1, 2, 3],
        [1, 3, 0, 2],
        [1, 3, 0, 2],
        [0, 1, 2, 3],
        [0, 1, 2, 3],
        [3, 2, 1, 0]]

start_locations_drones = [[-2.9, -3.6], [-1.75, -3.6], [1.4, -3.6], [2.7, -3.6]]

threads_1 = [threading.Thread(target=ooo) for _ in range(4)]


def land_disarm_0(drone_number):
    drones[drone_number].land()
    while not drones[drone_number].disarm():
        drones[drone_number].disarm()
    time.sleep(5)


def land_disarm():  # садится и выкл двигатеи
    for drone_number in range(0, len(drones)):
        process_1 = threading.Thread(target=land_disarm_0(drone_number))
        process_1.start()
        process_1.join()


def go_to(drone_number, x, y):  # дрон летит в точку
    drones[drone_number].arm()
    drones[drone_number].takeoff()
    drones[drone_number].go_to_local_point(x, y, 1)


def go_to_point(point_number):  # все дроны летят на свои точки в соответствии с пунктом плана
    if point_number % 2 == 0:
        for drone_number in range(0, len(drones)):
            base_number = plan[point_number][drone_number]  # передаем число, соответсвующее "координате"
            xy = bases[base_number]
            process_0 = threading.Thread(target=way(drone_number, xy[0], xy[1]))
            process_0.start()
            threads_1[drone_number] = process_0
            process_0.join()

    else:
        for drone_number in range(0, len(drones)):
            locality_number = plan[point_number][drone_number]
            xy = localities[locality_number]
            process_0 = threading.Thread(target=way(drone_number, xy[0], xy[1]))
            process_0.start()
            threads_1[drone_number] = process_0
            process_0.join()


def way(drone_number, x, y):  # дрон летит на указанную точку
    thread = threading.Thread(target=go_to(drone_number, x, y))
    thread.start()
    thread.join()


for point_number in range(6):
    go_to_point(point_number)
    time.sleep(5)
    land_disarm()

go_to_point(3)

go_to_point(7)
time.sleep(5)
land_disarm()

for drone_number in range(0, len(drones)):
    drones[drone_number].go_to_local_point(start_locations_drones[drone_number][0],
                                           start_locations_drones[drone_number][1], 1)
    while not drones[drone_number].point_reached(): pass
    drones[drone_number].land()
    drones[drone_number].disarm()

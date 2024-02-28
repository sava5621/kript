import math


def get_point(a: int, b: int, p: int) -> list:
    list_point = list()

    for x in range(p):
        y2 = (x ** 3 + a * x + b) % p
        for y in range(0, p):
            if y * y % p == y2:
                list_point.append({'x': x, 'y': y})

    return list_point


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)


def obr(a, b):
    # Находит а^(-1) mod b, то есть такое с, что ac=1(mod b)
    g = gcdex(a, b)
    if g[0] == 1:
        return g[1] % b
    else:
        return 0


def summ_point(x1, y1, x2, y2, p, a) -> dict:
    if x1 != x2:
        k = (y2 - y1) * obr(x2-x1, p)
        x_buf = (k*k - (x1 + x2)) % p
        y_buf = (k*(x1 - x_buf) - y1) % p
        return {'x': x_buf, 'y': y_buf}
    elif x1 == x1 and y1 + y2 == 0:
        return {'x': 0, 'y': 0, 'status': 'бесконечна'}
    else:  # x1 == x2 and y1 == y2
        k = ((3 * x1 ** 2 + a) * obr(2 * y1, p)) % p
        x_buf = (k ** 2 - 2 * x1) % p
        y_buf = (k * (x1 - x_buf) - y1) % p
        return {'x': x_buf, 'y': y_buf}


def get_n_p(n, x, y, p, a):
    list_pow_2 = list()
    max_pow = 0
    while n != 0:
        k = 0
        while n - 2**k >= 0:
            k += 1
        k -= 1
        if max_pow < k:
            max_pow = k
        n -= 2**k
        list_pow_2.append(2**k)

    # Получаем все nP, где n это 2 в степени
    n_p_data = dict()
    n_p_data[1] = {'x': x, 'y': y}
    for pow_item in [2**pow_2_item for pow_2_item in range(1, max_pow+1)]:
        n_p_data[pow_item] = summ_point(x1=n_p_data[int(int(pow_item / 2))]['x'],
                                        y1=n_p_data[int(int(pow_item / 2))]['y'],
                                        x2=n_p_data[int(int(pow_item / 2))]['x'],
                                        y2=n_p_data[int(int(pow_item / 2))]['y'],
                                        p=p, a=a)

    result = False
    list_pow_2.reverse()
    for pow_2 in list_pow_2:
        if not result:
            result = n_p_data[pow_2]
            continue

        # if not n_p_data[pow_2].get('status')

        result = summ_point(x1=result['x'],
                            y1=result['y'],
                            x2=n_p_data[pow_2]['x'],
                            y2=n_p_data[pow_2]['y'],
                            p=p, a=a)

    return result


def get_prim_point(a, b, p):
    for x in range(p):
        y2 = (x ** 3 + a * x + b) % p
        for y in range(0, p):
            if y * y % p == y2:
                if x == 0 or y == 0:
                    continue
                for k in range(4, p):
                    print(k)
                    point = get_n_p(n=k, x=x, y=y, p=p, a=a)
                    if point and point['y'] == 0:
                        return f'x:{x}, y:{y}, k={k*2}'
                else:
                    print(f'Не нашел x:{x}, y:{y}')

                # point_buf = {'x': x, 'y': y}
                # for k in range(1, int(math.log(p, 2))):
                #     point_buf = summ_point(x1=point_buf['x'],
                #                            y1=point_buf['y'],
                #                            x2=point_buf['x'],
                #                            y2=point_buf['y'],
                #                            p=p, a=a)
                #     if point_buf.get('status', False):
                #         return f'x:{x}, y:{y}, k={2 ** k}'
                # else:
                #     print(f'Не нашел x:{x}, y:{y}')

    # for point in get_point(a=a, b=b, p=p):
    #     if point['x'] == 0 and point['y'] == 0:
    #         continue
    #     point_buf = {'x': point['x'], 'y': point['y']}
    #     for k in range(0, math.log(p, 2)):
    #         point_buf = summ_point(x1=point_buf['x'],
    #                                y1=point_buf['y'],
    #                                x2=point_buf['x'],
    #                                y2=point_buf['y'],
    #                                p=p, a=a)
    #         if point_buf.get('status', False):
    #             return f'x:{point["x"]}, y:{point["y"]}, k={2**k}'
    #     else:
    #         return 'Не нашел'


# nP
print(get_n_p(n=21, x=1, y=785, p=2027, a=9))
# get_n_p(151, 1, 139, 19319, 1)
# get_n_p(151, 3, 16565, 313241, 20)


# Кол-во точек
# print(len(get_point(a=20, b=22, p=313241)))
print(len(get_point(a=9, b=7, p=2027)))
# print(len(get_point(1, 0, 19319)))


# print(get_n_p(78296, 3, 16565, 313241, 20))
# print(get_prim_point(a=9, b=7, p=2027))
# print(get_prim_point(a=1, b=0, p=19319))
# print(get_prim_point(a=20, b=22, p=313241))

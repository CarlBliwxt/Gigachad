def smooth_a(lista, n):
    res = []
    for i in range(0, len(lista)):
        temp_high = (i + n) - (len(lista) - 1)
        temp_low = ((i - n) * -1)
        if i-n < 0 and i+n > len(lista) - 1:
            res.append((sum(lista[0:len(lista)])+temp_high*lista[-1] + temp_low*lista[0])/(2*n+1))
        elif i-n < 0:
            res.append((sum(lista[0:i+n+1]) + lista[0] * temp_low)/(2*n+1))
        elif i+n > len(lista) - 1:
            res.append((sum(lista[i-n:len(lista)]) + temp_high*(lista[-1]))/(2*n+1))
        else:
            res.append(sum(lista[i-n:i+n+1])/(2*n+1))
    return res

def smooth_b(lista, n):
    res = []

    for i in range(0, len(lista)):
        temp_high = (i + n) - (len(lista) - 1)
        temp_low = ((i - n) * -1)
        if i-n < 0 and i+n > len(lista) - 1:
            goof = temp_low + temp_high
            res.append((sum(lista[0:len(lista)]))/(2*n+1-goof))
        elif i-n < 0:
            res.append((sum(lista[0:i+n+1]))/(2*n+1-temp_low))
        elif i + n > len(lista) - 1:
            res.append((sum(lista[i - n:len(lista)]) ) / (2 * n + 1- temp_high))
        else:
            res.append(sum(lista[i - n:i + n + 1]) / (2 * n + 1))
    return res


def round_list(calc_list, n):
    return [round(z, n) for z in calc_list]

x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
print('smooth_b(x, 1): ', smooth_b(x, 1))
print('smooth_b(x, 2): ', smooth_b(x, 2))


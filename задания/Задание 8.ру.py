def area(figure, data):
    if figure == 'круг':
        print(data[0])
        res = 3.14*(data[0]**2)
    if figure == 'квадрат':
        a,b = data
        res = a*b
    if figure == 'треугольник':
        res = (a*b)/2
    return ' Площадь {} = {}'.format(figure, res)
figure = input('фигура >>>  ')
data = [ float(i) for i in input('данные через пробел >>> ').split()]
print(area(figure, data))


def sum_arf_arr(*arrays, res = []):
    for arr in arrays:
        summ, arf = sum(arr), sum(arr) / len(arr)
        res.append((summ, arf))
    return res
 
print( sum_arf_arr([1,2,3], [4,5,6], [2,2,3]) )

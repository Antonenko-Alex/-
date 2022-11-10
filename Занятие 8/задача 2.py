def sum_arf_arr(*arrays, res = []):
    for arr in arrays:
        summ, arf = sum(arr), sum(arr) / len(arr)
        res.append((summ, arf))
    return res
 
print( sum_arf_arr([1,2,3], [4,5,6], [2,2,3]) )

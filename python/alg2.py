def count_bits(n):
    N = n 
    bin_n = format(N , "b")
    bin_count = bin_n.count('1')
    return bin_count, bin_n, N
bin_count, bin_n, N = count_bits(n = 1234)
print(f'Число: {N}\nДвочиный формат числа {N}:{bin_n}\nКоличество едbниц в двоичном формате числа {N}:{bin_count}')

def To_bin(n):
    n 
    bin = ""
    while n > 0:
        ost = n % 2
        bin= str(ost) + bin  # добавляем остаток в начало
        n = n // 2  # делим на 2 (целочисленное деление)
    return bin

print(To_bin(504))
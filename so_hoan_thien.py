# in ra các số hoàn thiện từ 1 đến n
# hàm kiểm tra 1 số có phải số hoàn thiện
def check_perfect_number(n):
    s = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            s += i
    if s == n: 
        return True
    else:
        return False

def perfect_number(n):
    print('Các số hoàn thiện từ 1 đến ' + str(n) + ' là: ')
    for i in range(1, n):
        if check_perfect_number(i) == True:
            print(i, end=' ')

if __name__ == '__main__':
    n = int(input('n = '))
    if check_perfect_number(n) == True:
        print(str(n) + " là số hoàn thiện!")
    else:
        print(str(n) + " không là số hoàn thiện!")
    perfect_number(n)

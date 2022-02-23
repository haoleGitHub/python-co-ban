# tìm UCLN
def hcf_or_gcd(num1, num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            factor = i
    return factor

# tìm BCNN
def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            break
        greater += 1
    return greater

num1 = int(input("Nhập số thứ 1: "))
num2 = int(input("Nhập số thứ 2: "))
print("Bội chung nhỏ nhất: " + str(lcm(num1, num2)))
print("Ước chung lớn nhất: " + str(hcf_or_gcd(num1, num2)))

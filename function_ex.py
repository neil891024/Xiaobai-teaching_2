#為什麼需要函式?
#函式用在大量重複的地方

def print_info(name,age,height,weight):
    print(f"{name}今年{age}歲")
    print(f"{name}身高{height}公分")
    print(f"{name}體重{weight}公斤")

print_info("小白", 24, 179, 70)
print_info("小黑", 10, 159, 44)
print_info("小藍", 59, 159, 44)
print_info("小綠", 33, 159, 44)
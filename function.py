#函式(函數) function
#函式可以大量減少重複的地方

def print_info(name):
    print(f"{name}今年24歲")
    print(f"{name}身高179公分")

print_info("")

def print_info(name,age,height):
    print(f"{name}今年{age}歲")
    print(f"{name}身高{height}公分")

print_info("小綠", 30, 160)
print_info(name="小綠", height=160 , age=30) #可以做直接指定的動作，避免變數輸入錯誤

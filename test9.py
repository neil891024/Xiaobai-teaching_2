# find_max 函數找出最大的
# find_min 函數找出最小的
# max_min 函數 最大-最小
# max_min 函數中使用find_max跟find_min 得出最大-最小

def find_max(num1,num2,num3): #找最大
    if type(num1) != int or type(num2) != int or type(num3) !=int:
        return "請輸入整數" #避免輸入錯誤

    if num1>=num2 and num1>=num3: 
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

def find_min(num1,num2,num3): #找最小
    if num1<=num2 and num1<=num3:
        return num1
    elif num2<=num1 and num2<=num3: 
        return num2
    else:
        return num3
    
def max_min(num1,num2,num3): #最大-最小
    if type(num1) != int or type(num2) != int or type(num3) !=int:
        return "請輸入整數" #避免輸入錯誤
    
    else:
     max = find_max(num1,num2,num3)
     min = find_min(num1,num2,num3)
     ans = max-min
     return ans
    
num = max_min(1,2,3)
print(num)

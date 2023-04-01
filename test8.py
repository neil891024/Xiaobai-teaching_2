#函式練習 找出最大的數
#碰到return 會直接回傳，return下面的程式就不會被執行

def find_max(num1,num2,num3):
    if type(num1) != int or type(num2) != int or type(num3) !=int:
        return "請輸入整數"
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

max = find_max(10,20,30)
print(max)
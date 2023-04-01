#判斷輸入的數是奇數還是偶數
num = int(input ("請輸入一個整數:\n"))
rem = (num%2)

if rem != 0:
    print("奇數")
else:
    print("偶數")

print(rem)

num = int(input("請輸入一個整數:\n")) #另一種寫法
if num % 2 == 0:
    print("偶數")
else:
    print("奇數")
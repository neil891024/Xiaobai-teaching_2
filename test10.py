#綜合健康計算機 (BMI BMR TDEE)
def get_bmi(height,weight):
    height /= 100
    bmi = round(weight/height**2,1)
    return bmi

def get_bmr(sex,height,weight,age): #計算基礎代謝率
    if sex == "男":
        bmr = 66 +(13.7*weight+5*height-6.8*age)
    elif sex == "女":
        bmr = 655 +(9.6*weight +1.8*height-4.7*age)
    bmr = round(bmr,2)
    return bmr

def get_TDEE(sex,height,weight,age,time): #計算總熱量消耗
    bmr = get_bmr(sex,height,weight,age)
    TDEE = bmr*time
    TDEE = round(TDEE,2)
    return TDEE

print("歡迎使用綜合健康計算機~")
print("(1)計算bmi")
print("(2)計算基礎代謝率(bmr)")
print("(3)計算總熱量消耗(TDEE)")
pro = input("請選擇要計算的項目 (輸入1 or 2 or 3 )")

if pro == "1":
    height = float(input("請輸入您的身高(公分)"))
    weight = float(input("請輸入您的體重(公斤)"))
    bmi = get_bmi(height,weight)
    print(f"您的BMI:{bmi}")

elif pro == "2":
    sex = input("請輸入您的性別(男or女)")
    height = float(input("請輸入您的身高(公分)"))
    weight = float(input("請輸入您的體重(公斤)"))
    age = int(input("請輸入您的年齡"))
    bmr = get_bmr(sex,height,weight,age)
    print(f"您的BMR:{bmr}")

elif pro == "3":
    sex = input("請輸入您的性別")
    height = float(input("請輸入您的身高(公分)"))
    weight = float(input("請輸入您的體重(公斤)"))
    age = int(input("請輸入您的年齡"))
    bmr = get_bmr(sex,height,weight,age)

    print("(1)久坐幾乎沒運動")
    print("(2)每週低強度運動1~3天")
    print("(3)每週低強度運動3~5天")
    print("(4)每週低強度運動6~7天")
    print("(5)勞力密集工作或是每天高強度訓練")

    time = input("請選擇您的運動量(輸入1~5)")
    if time == "1":
        TDEE = round(bmr*1.2,2)  
        print(f"您的總熱量消耗(TDEE):{TDEE}")
    elif time == "2":
        TDEE = round(bmr*1.375,2)  
        print(f"您的總熱量消耗(TDEE):{TDEE}")
    elif time == "3":
        TDEE = round(bmr*1.55,2)  
        print(f"您的總熱量消耗(TDEE):{TDEE}")
    elif time == "4":
        TDEE = round(bmr*1.725,2)  
        print(f"您的總熱量消耗(TDEE):{TDEE}")
    elif time == "5":
        TDEE = round(bmr*1.9,2)  
        print(f"您的總熱量消耗(TDEE):{TDEE}")
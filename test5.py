#BMI 計算機
#輸入身高換行後輸入體重，計算出BMI
height_cm = float(input("請輸入您的身高(公分)\n"))
weight = float(input("請輸入您的體重(公斤)\n"))

height_m = height_cm/100

BMI = weight / (height_m**2)
BMI = round(BMI,1)

#下方為進階版BMI計算機的程式
if BMI<18.5:
    print(f"您的BMI是: {BMI} (體重過輕) " )

elif 18.5<=BMI<24:
    print(f"您的BMI是: {BMI} (正常體位) " )

elif 24<=BMI<27:
    print(f"您的BMI是: {BMI} (體重過重) " )

elif 27<=BMI<30:
    print(f"您的BMI是: {BMI} (輕度肥胖) " )

elif 30<=BMI<35:
    print(f"您的BMI是: {BMI} (中度肥胖) " )

else:
    print(f"您的BMI是: {BMI} (重度肥胖) " )

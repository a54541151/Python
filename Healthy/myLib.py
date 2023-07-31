class Healthy:
    # def __init__(self):
    #     pass
    def BMI(self, high, weight):
        self.bmi = round(weight / (high/100) ** 2, 1)   #BMI = 體重(公斤) / 身高2(公尺2)  round取小數第一位
        print(f"BMI:{self.bmi}")
        # return self.bmi
    def BMR(self, sex, high, weight, age):
        if sex == "男":
            self.bmr = (13.7 * weight) + (5 * high) - (6.8 * age) + 66  #BMR(男)=(13.7×體重(公斤))+(5×身高(公分))-(6.8×年齡)+66
        else:
            self.bmr = (9.6 * weight) + (1.8 * high) - (4.7 * age) + 655  #BMR(女)=(9.6×體重(公斤))+(1.8×身高(公分))-(4.7×年齡)+655
        print(f"BMR:{round(self.bmr,1)}")
        return round(self.bmr,1)
    def TDEE(self, sex, high, weight, age, sport):
        self.bmr = self.BMR(sex, high, weight, age)
        if sport == "幾乎沒動":
            self.tdee = self.bmr * 1.2
        elif sport == "運動1~3天":
            self.tdee = self.bmr * 1.375
        elif sport == "運動3~5天":
            self.tdee = self.bmr * 1.55
        elif sport == "運動6~7天":
            self.tdee = self.bmr * 1.725
        elif sport == "7天以上":
            self.tdee = self.bmr * 1.9
        print(f"TDEE:{round(self.tdee, 1)}")
        # else:
        #     self.tdee = 0
        return round(self.tdee, 1)


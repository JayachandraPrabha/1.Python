class multipleFunctions():
    def OddEven():
        number=int(input("Enter  number:"))
        if(number%2==1):
            result=print(number,"is Odd number")
        else:
            result=print(number,"is Even number")
        return result
    def BMI():
        bmi=int(input("Enter the BMI Index:"))
        if bmi<18:
            print("Under weight")
            mes="Under weight"
        elif bmi<25:
            print("Healthy weight")
            mes="Healthy weight"
        elif bmi<30:
            print("Over weight")
            mes="Over weight"
        elif bmi<35:
            print("Very Over weight")
            mes="Very Over weight"
        elif bmi<40:
            print("Severly Obese")
            mes="Severly Obese"
        else:
            print("Morbidly Obese")
            mes="Morbidly Obese"
        return mes
def bmi():
    height = float(input("Input your height(cm): "))
    weight = float(input("Input your weight(kg): "))

    BMI = weight / (height / 100.0) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            print('Your BMI: %.1f. Category: %s' % (BMI, status))
            break

if __name__ == '__main__':
    bmi()

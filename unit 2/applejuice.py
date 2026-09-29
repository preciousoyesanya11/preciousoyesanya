num_apples = input("how many apples")
num_people = input("how many people")

def serve(num_apples, num_people):
    print("served " + num_people + "glasse(s) of apple juice at " + num_apples + "per glass.")

def portion(num_apples, num_people):
    calc = float(num_apples) / int(num_people)
    return calc

def divide(num_apples, num_people):
    calc = float(num_apples) / int(num_people)
    return calc

calc = divide(num_apples, num_people)

print("each person will get  " + str(calc) + "apples per glass of apple juice.")

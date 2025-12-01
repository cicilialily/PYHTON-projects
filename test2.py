print("welcome to the capitals quiz game!\n")
score = 0
capital = {"Greece": "Athens",
           "USA": "washington",
           "Nigeria": "Abuja",
           "Mozamboque": "Maputo",
           "South Africa": "Lesotho",
           "UK": "London",
           "Ethopia": "AdisAbaba",}

for country in capital:
    user_answer = input(f"what is the capital of {country} ? ")
    if user_answer == capital[country]:
        print("correctt!")
        score = score + 1
    else:
        print("incorrect!")
        print(f"the capital of {country} is {capital[country]}.")

        print("game over!")
        print(f"you scored {score} out of 10.")
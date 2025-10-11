# ~Exercise 3~
print("Welcome to KBC")
print("You will be asked 15 questions")
questions = [
    ["What is the capital of India?", "Chandigarh", "Delhi", "Mumbai", "Lucknow", 2],
    ["What is the national animal of India?", "Lion", "Tiger", "Elephant", "Leopard", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who is known as the Father of Nation in India?", "Subhash Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Bhagat Singh", 2],
    ["Which is the largest state in India by area?", "Rajasthan", "Maharashtra", "Uttar Pradesh", "Madhya Pradesh", 1],
    ["Which is the longest river in India?", "Yamuna", "Brahmaputra", "Ganga", "Godavari", 3],
    ["Which is the national flower of India?", "Rose", "Lotus", "Lily", "Sunflower", 2],
    ["Which is the fastest land animal?", "Cheetah", "Tiger", "Horse", "Lion", 1],
    ["Which country is known as the Land of Rising Sun?", "China", "Japan", "Korea", "Thailand", 2],
    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["What is H2O commonly known as?", "Salt", "Water", "Sugar", "Acid", 2],
    ["Which is the largest ocean?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    ["Who invented the light bulb?", "Newton", "Edison", "Einstein", "Tesla", 2],
    ["Which is the smallest continent?", "Africa", "Australia", "Europe", "Antarctica", 2],
    ["What is the national currency of India?", "Dollar", "Yen", "Rupee", "Pound", 3],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 
          160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

safe_money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\nYour question for Rs.{levels[i]} is:")
    print(question[0])  # print the question text
    print(f"a. {question[1]} \nb. {question[2]} \nc. {question[3]} \nd. {question[4]}")
    
    try:
        reply = int(input("Enter your answer (1/2/3/4): "))
    except ValueError:
        print("Invalid input! Game over.")
        break

    if reply == question[-1]:
        print(f"✅ Correct answer! You have won Rs.{levels[i]}")
        
        if i == 4:
            safe_money = 10000
            print("🎉 Congratulations! You have reached the safe level of Rs. 10,000")
        elif i == 9:
            safe_money = 320000
            print("🎉 Congratulations! You have reached the safe level of Rs. 3,20,000")
        elif i == 14:
            safe_money = 10000000
            print("🎉 Congratulations! You have won Rs. 1 Crore")
            break
    else:
        print("❌ Wrong answer! Game over.")
        print(f"You will take home Rs.{safe_money}")
        break
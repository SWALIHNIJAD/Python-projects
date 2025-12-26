questions = [
    ["Who is Sha Rukh Khan?", "WWE Wrestler", "Astronut", "Actor", "Plumber", 33],
    ["What is the capital of France?","Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as red planet?", "Earth", "Venus", "Mars","Jupiter", 3 ],
    ["Which is largest mammal?", "Shark", "Elephant", "Bluwhale", "Giraffe",3],
    ["Whick is the smallest country in the World?", "San Marino", "Vatican City", "Monaco", "London", 2],
    ["Which country is known as the Land of rising sun?","India", "South Korea", "Japan", "China", 3],
]   

prizes = [10000, 20000, 40000, 50000, 60000, 100000]

i = 0 
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"c.{question[4]}")
    #Check whether the option is correct!

    a = int(input("Enter your Answer, 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if (question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect! the answer for this question is {question[5]}")
        print("Better luck next time!")
        break
    print(f"You won {prizes[i]}")
    i += 1
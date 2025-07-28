#if/elif/else Statements 

StudentName = input("Enter your name: ")
StudentScore = int(input("Enter your score: "))

if StudentScore >= 85:
    print(f"Congratulations {StudentName}, you have passed with distinction!")
elif StudentScore >= 70 and StudentScore < 85:
    print(f"Good job {StudentName}, Keep Practicing .")
else:
    print(f"{StudentName}, You have to Work Bit more .")




total = 0

for i in range(10):
    total+= 10
    print("You have completed ",total," Jumping Jacks.")

    tired = input("Are you tired (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You have completed ",total,"Jumping Jacks.")
            break
        else:
            print("Okay Continue !")
            print("Remaining Jumping Jacks = ",100-total)

    else:
        print("Jumping Jacks remaining : ",100-total)

if total ==100:
    print("Congratulations you have completed the workout !")
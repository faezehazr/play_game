import time
import random 
while True:
    user_name = input("enter yr name: ")
    random_num=random.randint(0,100)
    print(random_num)
    start_time = time.perf_counter()
    while True:
        try:
            num = int(input("enter a number in range limit:"))
            if num < random_num:
                print("the main number is bigger than yours")
            elif num > random_num:
                print("the main number is smaller than yours,enter a number smaller than this")
            else:
                print("u got it")
                break

        except ValueError:
            print("invalid input,pls enter an integer")

    end_time = time.perf_counter()
    elapsed_time = round(end_time - start_time)
    print(f"Elapsed time: {elapsed_time} seconds")
    desktop_path = r"C:\Users\ASUS\Desktop\git hub\play_game\elapsed_time.txt"
    with open(desktop_path, "w") as file:
        file.write(f"The elapsed time is: {elapsed_time}")
    print(f"Result saved to {desktop_path}")


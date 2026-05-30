def limit(x):
    if x<=0:
        print("Invalid number")
    for i in range(x):
        if i%2==0:
            print(f"First even number:{i}")
            break
limit(12)                
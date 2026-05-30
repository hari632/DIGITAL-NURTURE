def limit(x):
    if x<=0:
        print("Invalid number")
    for i in range(x):
        total=0
        if i%2==0:
            continue
        total+=i
    print(f"Total :{total}")
limit(12)   
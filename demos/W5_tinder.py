def interests():
    print("Enter all interests, one after the other or \"stop\" to stop")
    s1 = set()
    interest = ""
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        s1.add(interest)
    return s1
#print(interests())         (to test if works)
def run():
    print("First person: ")
    p1 = interests()
    print("Second person: ")
    p2: interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"You are a match made in heaven! you have {len(common)} hobbies in common")
    else:
        print(f"Oh no! It will probably not work. Find another human.")
run()
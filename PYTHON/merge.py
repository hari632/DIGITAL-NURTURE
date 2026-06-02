def skill(skill1,skill2):
    if not skill1 and not skill2:
        print("INVALID")
        return
    c= skill1 & skill2
    print("common :",c)
skill1={"Python","SQL","C"}
skill2={"Python","SQL","AI"}
skill(skill1,skill2)    
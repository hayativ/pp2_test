def my_func(str):
    upper_cnt = 0
    lower_cnt = 0
    for s in str:
        if s.isupper():
            upper_cnt += 1
        elif s.islower():
            lower_cnt += 1
    print(f"{upper_cnt} uppercase letters")
    print(f"{lower_cnt} lowercase letters")

str = input()
my_func(str)



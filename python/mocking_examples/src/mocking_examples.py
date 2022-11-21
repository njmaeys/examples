def older_times_two(age: int) -> int:
    print('HERE: person older times two')
    new_age = age * 2
    return new_age

def person_older(name: str, age: int) -> str:
    print('HERE: person older')
    age_times_two = older_times_two(age)
    return f"{name} is {age_times_two}"
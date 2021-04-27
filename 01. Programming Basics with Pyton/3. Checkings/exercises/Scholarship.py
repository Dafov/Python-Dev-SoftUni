import math

income = float(input())
medium_score = float(input())
min_wage = float(input())

social = math.floor(min_wage * 0.35)
excellence = math.floor(medium_score * 25)

# Case 1 - Students with > 5.5 medium_score get excellence
if medium_score >= 5.50 and income >= min_wage:
    print(f'You get a scholarship for excellent results {excellence} BGN')

# Case 2 - Student has between 4.5 and 5.5 medium score and income = less then min_wage - get social
elif 4.50 <= medium_score < 5.50:
    if income < min_wage:
        print(f'You get a Social scholarship {social} BGN')
    elif income >= min_wage:
        print('You cannot get a scholarship!')

# Case 3 - income < min wage and medium_score < 5.5 - take the bigger scholarship
elif medium_score >= 5.50 and income <= min_wage:
    if social >= excellence:
        print(f'You get a Social scholarship {social} BGN')
    elif excellence > social:
        print(f'You get a Social scholarship {excellence} BGN')

# Case 4 - medium_score < 4.50
elif medium_score < 4.50:
    print('You cannot get a scholarship!')
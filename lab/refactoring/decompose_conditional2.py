# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

def check_cholostrol(total_cholostrol):
    if total_cholostrol < 200:
        return "good"
    elif 200 < total_cholostrol < 240:
        return "high"
    else:
        return "very high"

def check_ldl(ldl):
    if ldl < 100:
        return "good"
    elif ldl > 160:
        return "very high"
    else:
        return "high"

def check_triglyceride(triglyceride):
    if triglyceride < 150:
        return "good"
    elif ldl >= 200:
        return "very high"
    else:
        return "high"

if check_cholostrol(total_cholostrol) == "good" and check_ldl(ldl) == "good" and check_triglyceride(triglyceride) == "good":
    # good level
    print('*** Good level of cholestrol ***')
elif check_cholostrol(total_cholostrol) == "very high" or check_ldl(ldl) == "very high" or check_triglyceride(triglyceride) == "very high":
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif check_cholostrol(total_cholostrol) == "high" or check_ldl(ldl) == "high" or check_triglyceride(triglyceride) == "high":
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')

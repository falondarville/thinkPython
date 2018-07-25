# Volume of a sphere r is 4/3 pi*r squared. What is the volume of a sphere with radius 5?
import math 

r = 5

print((4/3) * math.pi * r**3)

# The cover price of a book is $24.95, but bookstores get 40% off. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
# Note that we have to account for the discount first, and then multiple the cost of the book by 60 units. After that, we add the cost of shipping. 
print((24.95 * .6)* 60 + (.75 * 59) + 3)

# If I leave my house at 6:52am and run 1 mile at 8:15 pace, then 3 miles at tempo (7:12 pace), and 1 mile at 8:15 pace again. What time do I get home for breakfast?

# convert times to seconds
time1 = ((8 * 60) + 15) * 2
time2 = ((7 * 60) + 12) * 3

# convert start time to seconds
start_time = ((6 * 3600) + (52 * 60))

# add all the seconds together
seconds_total = start_time + time1 + time2

# convert seconds back to hours and minutes
convert_hours = seconds_total/3600
# returns 6.65
# get the numbers after the decimal point
frac, whole = math.modf(convert_hours)

converted_frac = int(frac * 60)

converted_whole = int(whole)

print(f"I get home for breakfast at {converted_whole}:{converted_frac}!")

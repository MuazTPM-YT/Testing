def simple_interest_1(p, t, r):
    s_i = (p * t * r) / 100
    return (s_i)

def simple_interest_2(p, t, r=10):
    s_i = (p * t * r) / 100
    return (s_i)

prin = int(input("Principle Amount: "))
time = int(input("Time (Years): "))
r_o_i = int(input("Rate of Interest: "))

sim_int1 = simple_interest_1(prin,time,r_o_i)
sim_int2 = simple_interest_2(prin,time)

print("\nWithout Default Variables:-")
print("Simple Interest:",sim_int1)
print("Total Amount:",prin + sim_int1)
print()
print("With Default Variable (Rate of Interest):-")
print("Simple Interest:",sim_int2)
print("Total Amount:",prin + sim_int2)
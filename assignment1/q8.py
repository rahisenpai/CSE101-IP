def func(population,rate):
    population += population*rate/100
    return population

pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
curr_pop=0
for j in pop:
    curr_pop += j
print('current population is',curr_pop,'million')

prev_pop,Y = 0,0
while(1):
    totalpop=0
    for i in range(len(pop)):
        item = pop[i]
        for j in range(Y+1):
            rate = 2.5-(0.1*j)-(0.4*i)
            new_pop = func(item,rate)
            item = new_pop
        totalpop += new_pop
    if totalpop<prev_pop:
        break
    #the new population is less than the previous so the maximum is the previous population
    else:
        prev_pop=totalpop
        Y+=1
print('maximum population of',prev_pop,'million will be reached after',Y,'years')
import random

critrate=float(input('Enter crit rate: '))
critdmg=float(input('Enter  damage multiplier: '))
att=float(input('Enter your base attack dmg: '))
total=0
critcount=0
i=1
while (i<=100):
	dice = random.uniform(1,100)
	if (dice<=critrate):
		hitdmg=att*critdmg
		total=total+hitdmg
		critcount=critcount+1
		print("Critical hit " +format(hitdmg)+" - Critical hit dmg total: " +format(total)+" - Crit count: " +format(critcount))
	i=i+1
	   
	
    
           

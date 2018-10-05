
def crime_list(z):               #function definition
	f=open(z,"r")   #open csv file in read mode
	d1=dict()
	d2=dict()
	list1=[]
	list2=[]
	for line in f:
		line.strip()
		for lines in line.split(','):
			list1.append(lines[-1])
			list2.append(lines[-2])
	for y in list1:
		if y not in d1:
			d1[y]=1
		else:
			d1[y]=d[y]+1
	for z in list2:
		if z not in d2:
			d2[z]=1
		else:
			d2[z]+=1
	print("crime name",' '*15,"crimeid",' '*15,"crimecount")			#printing Headers	
	for k1,v in d1.items():
		for k2,v in d2.items():
			print(k1,k2,v, "\n")
file="Crime.csv"		
crime_list(file)		#function call


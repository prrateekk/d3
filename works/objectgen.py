import random

f=open('file.txt','w')
s=d=b=p=v=0
for states in range(1,5):
	x = random.randrange(4,8)
	s+=1
	for districts in range(1,x):
		y = random.randrange(4,8)
		d+=1
		for blocks in range(1,y):
			z = random.randrange(4,8)
			b+=1
			for panchayats in range(1,z):
				k = random.randrange(4,8)
				p+=1
				for villages in range(1,k):
					v+=1
					f.write('{"country":"India","state":"S'+str(s)+'","district":"D'+str(d)+'","block":"B'+str(b)+'","panchayat":"P'+str(p)+'","village":"V'+str(v)+'",')
					f.write('"data":[')
					for i in range(199):
						f.write(str(random.randrange(20,90))+',')
					f.write(str(random.randrange(20,90))+']},\n')


f.write('\n')
f.write('//States - '+str(s)+'\n')
f.write('//Districts - '+str(d)+'\n')
f.write('//Blocks - '+str(b)+'\n')
f.write('//Panchayats - '+str(p)+'\n')
f.write('//Villages - '+str(v)+'\n')

f.close()
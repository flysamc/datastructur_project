


def AddPath(a,s,r,j,l):
	if s not in j:
		j.append(s)
		for i in range(len(a[s])):
			w = a[s][i]
			if(w==r):
				j.append(w)
				l.append(j[:])
				j.remove(w)
			elif(w not in j):
				AddPath(a,w,r,j,l)
			else:
				pass
		#print(j)
		j.remove(s)
				

	




'''def AddPath(a,s,l):
	if s in a:
		
		for i in range(len(a[s])):
			l.append([])
			if s not in l[i]:
				l[i].append(s)
				if a[s][i] not in l[i]:
					l[i].append(a[s][i])
					AddPath(a,a[s][i],l)
			print(l,i)
			#AddPath(a,a[s][i],l)

'''








'''def AddPath(a,s,l):
	if s in a:
		print(l)
		for i in range(len(a[s])):
			l.append([])
			if s not in l[i]:
				l[i].append(s)
				if a[s][i] not in l[i]:
					l[i].append(a[s][i])
					AddPath(a,a[s][i],l)


'''






'''def AddPath(a,s,l):
	if s in a:
		for i in range(len(a[s])):
			l.append([])
			if a[s] in l[i]:
				pass
			else:
				l[i].append(a[s])
			#CheckPath(a,s,i,l[i])
'''
	
		
		
		

'''def CheckPath(a,s,j,d):
	if(a[s][j] in d):
		pass
	else:
		l[j].append(a[s][j])
		AddPath(a,a[s][j],l[j])
'''

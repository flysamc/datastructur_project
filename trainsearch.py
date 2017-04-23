

def Trainseach(allpath,trainlist):
	for i in allpath:
		for j in trainlist:
			trainstopage=trainlist[j]
			source=path[-len(path)]
			last=-1
			destination=path[last]
			if source in trainstopage:
				if destination in trainstopage:
					print("yes")
				else:
					while(last>(-len(path))):
						if(path[last] in trainstopage):
							if(path[last]==destination):
								pass
							else:
								source=path[last]
								
						else:
							last = last - 1
					
							


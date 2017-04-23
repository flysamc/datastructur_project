

def Create():
	graph = dict()
	return graph

def InsertVertex(graph,v):
	graph[v] = []
	return graph
	
def InsertEdge(graph,v1,v2):
	if(graph.has_key(v1)):
		graph[v1].append(v2)
	else:
		InsertVertex(graph,v1)
		graph[v1].append(v2)
	if(graph.has_key(v2)):
		graph[v2].append(v1)
	else:
		InsertVertex(graph,v2)
		graph[v2].append(v1)
	return graph

def DeleteVertex(graph,v):
	if(graph.has_key(v)):
		del graph[v]
	else:
		print("{0} is not in graph".format(v))
 

def DeleteEdge(graph,v1,v2):
	#if(graph.has_key(v1)):
	graph[v1].remove(v2)
	graph[v2].remove(v1)
	return graph

def IsEmpty(graph):
	if not graph:
		print("Its empty")
	else:
		print("not empty")

def ListAdjacent(graph,v):
	return graph[v]	


def PrintGraph(graph):
	print(graph)

#a=graph,s=starting station r=destination j=stack l=finallsit
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

def CheckTrainPath(source,destination,trainstopage,path,trainlist,i,storetrain):
	if source in trainstopage:
		samedestination = path.index(destination)
		while(samedestination>path.index(source)):
			#print(samedestination)
			if path[samedestination] in trainstopage:
				#print(trainstopage)
				#print(trainlist,i)
				if(path[samedestination] == destination):
					print(path,i)
					
				else:
					print(i)
					print(storetrain)
					source= samedestination
					Train(source,destination,trainlist,path,storetrain)
				break
			else:
				samedestination = samedestination - 1
							
	else:
		pass
		#print("Train has not stopage at {0}".format(path[source]))
		

def Train(source,destination,trainlist,path,storetrain):
	for i in trainlist:
		if i in storetrain:
			pass
		#print(trainlist)
		else:
			storetrain.append(i)
			trainstopage = trainlist[i]
			CheckTrainPath(source,destination,trainstopage,path,trainlist,i,storetrain)

def SearchForAllPath(allpath,trainlist):
	pathlist=[i for i in allpath]
	
	for path in pathlist:
		storetrain = []
		PassPath(path,trainlist,storetrain)

def PassPath(path,trainlist,storetrain):
	start= -len(path)
	finish = -1
	source=path[start]
	destination=path[finish]
	Train(source,destination,trainlist,path,storetrain)
	
		

def SameTrain(path,trainstopage):
	if path[0] in trainstopage:
		if path[-1] in trainstopage:
			for i in path:
				if i not in trainstopage:
						print(path)
						return False
						break
		else:
			print(path)
			return True
	else:
		return True





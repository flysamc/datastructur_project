

def SearchTrain(source,destination,path,trainlist,storetrain):
	for i in trainlist:
		if i in storetrain:
			pass
		else:
			trainstopage = trainlist[i]
			if source in trainstopage:
				print(i)
				if destination in trainstopage:
					storetrain.append(i)
					print(i,"ok")			
				else:
					for station in reversed(path):
						if station in trainstopage and station != source:
							storetrain.append(i)
							source = station
							SearchTrain(source,destination,path,trainlist,storetrain)

			else:
				pass

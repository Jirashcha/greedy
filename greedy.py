#Greedy Algorithm: Activity Selection (Activity n activity and room k room. Output; wants all events to be held with minimal room)
#Jirashcha Wanggum 1640702609 CS441 sec. 327E

def ActivitySelection(startList,finishList,roomList,actList):
    result = []
    for i in range(len(startList,-1):
        if startList[i+1] == finishList[i]:
            result.append(actList[i])
            startList.pop(i)
            finishList.pop(i)
            actList.pop(i)
    return result

act = int(input("Enter number of activities: "))
room = int(input("Enter number of rooms: "))
actList = []
startList = []
finishList = []
roomList = []
roomNum = []

if room >= 1:
    for i in range(room):
        roomNum.append(i+1)
        roomList.append([])
    
    for i in range(act):
        print("Enter start and finish time for activity", i+1, ":")
        start = int(input())
        finish = int(input())
        if start >= finish:
            print("Invalid input. Start time must be less than finish time.")
            exit()
        activity = {"activity":i + 1, "start":startActivity, "end":endActicity}
        actList.append(activity)

    #sort finish time
    for i in range(act):
        for j in range(act-i-1):
            if finishList[j] > finishList[j+1]:
                finishList[j], finishList[j+1] = finishList[j+1], finishList[j]
                startList[j], startList[j+1] = startList[j+1], startList[j]
                actList[j], actList[j+1] = actList[j+1], actList[j]
    
    #find room
    for k in range(room):
        roomList[k] = ActivitySelection(startList,finishList,roomList,actList)
    
    if len(actList) != 0:
        if len(roomList) > len(actList):
            for i in range(len(actList)):
                roomList[i].append(actList[i])
        else:
            print("No activity can be held.")
            exit()

    
    print("Can be held all activity.")
    print(roomList)
    # for i in range(len(roomList)):
    #     print("Room",i+1, ": Activity", roomList[i])               
                
else:
    print("No activity can be held.")
    exit()




if (act and room != 0):
	for i in range(act):
		print("Activity: ", i + 1)
		startActivity = int(input("Enter startActivity: "))
		endActicity = int(input("Enter endActicity: "))
		activity = {"room":i + 1, "start":startActivity, "end":endActicity}
		activityList.append(activity)
	for i in range(room):
		room = {"activityBooking": []}
		roomList.append(room)
	for i in range(len(activityList)):
		for x in range(len(roomList)):
			if (len(roomList[x]["activityBooking"]) == 0):
				try:
					if activityList[i]["start"] == 1 :
						roomList[x]["activityBooking"].append(activityList[i])
						if len(activityList) != 1:
							activityList.pop(i)
				except:
					pass
	for i in range(len(activityList)):
		for x in range(len(roomList)):
			for y in range(len(roomList[x]["activityBooking"])):
				if (roomList[x]["activityBooking"][y]["end"] == activityList[i]["start"]):
					print(roomList[x]["activityBooking"])
					print(activityList[i])
    

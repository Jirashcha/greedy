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
roomList = []

if room and act >= 1:
    for i in range(room):
        r = {"room":i+1 []}
        roomList.append(r)
    
    for i in range(act):
        print("Enter start and finish time for activity", i+1, ":")
        start = int(input())
        finish = int(input())
        if start >= finish:
            print("Invalid input. Start time must be less than finish time.")
            exit()
        activity = {"activity":i + 1, "start":startActivity, "finish":endActicity}
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

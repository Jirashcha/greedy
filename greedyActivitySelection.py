#Greedy Algorithm: Activity Selection (Activity n activity and room k room. Output; wants all events to be held with minimal room)

act = int(input("Enter number of activities: "))
room = int(input("Enter number of rooms: "))
actList = []
roomList = []
countActSelected = 0
countRoomSelected = 0

if room and act >= 1:
    for i in range(room):
        r = {"room":i+1,":":[]}
        roomList.append(r)

    for i in range(act):
        print("Enter start and finish time for activity", i+1, ":")
        start = int(input())
        finish = int(input())
        if start >= finish:
            print("Invalid input. Start time must be less than finish time.")
            exit()
        activity = {"activity":i + 1, "start":start, "finish":finish}
        actList.append(activity)
        
    for i in range(len(actList)):
        for j in range(len(actList)-1):
            if actList[j]["finish"] > actList[j+1]["finish"]:
                temp = actList[j]
                actList[j] = actList[j+1]
                actList[j+1] = temp
    
    for i in range(len(actList)):
        for j in range(len(roomList)):
            if len(roomList[j][":"]) == 0:
                roomList[j][":"].append(actList[i])
                countActSelected += 1
                countRoomSelected += 1
                break
            else:
                last = len(roomList[j][":"]) - 1
                if actList[i]["start"] >= roomList[j][":"][last]["finish"]:
                    roomList[j][":"].append(actList[i])
                    countActSelected += 1
                    break
    
    print("------------------------------------")
    if countActSelected != len(actList):
        print("Not all activities can be selected.")
    else:
        print("All activities can be selected.")
        print("The minimal number of rooms possible is:", countRoomSelected)  
    print("The activities selected in each room are:")       
    for i in range(len(roomList)):
        if len(roomList[i][":"]) != 0:
            print("Room", roomList[i]["room"], " held activity:", end=" ")
            for j in range(len(roomList[i][":"])):
                print(roomList[i][":"][j]["activity"], end=" ")
            print()
        else:
            break
    print("------------------------------------")
    
else:
    print("Invalid input. Number of rooms and activities must be greater than 0.")

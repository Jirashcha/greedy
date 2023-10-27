#Greedy Algorithm: Activity Selection (Activity n activity and room k room. Output; wants all events to be held with minimal room)
#Jirashcha Wanggum 1640702609 CS441 sec. 327E

act = int(input("Enter number of activities: "))
if act >= 1:
    actList = []
    roomList = []
    countAct = 0
    k = 0

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
    
    while len(actList) != countAct:
        r = {"room":k+1,":":[]}
        roomList.append(r)
        for i in range(len(actList)):
            if len(roomList[k][":"]) == 0:
                roomList[k][":"].append(actList[i])
                countAct += 1
                break
            else:
                last = len(roomList[k][":"]) - 1
                if actList[i]["start"] >= roomList[k][":"][last]["finish"]:
                    roomList[k][":"].append(actList[i])
                    countAct += 1
                    break
        k += 1
        
        
    print("------------------------------------")
    print("All activities can be selected.")
    print("The minimal number of rooms possible is:", k)  
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
    print("Invalid input. Number of activities must be greater than 0.")
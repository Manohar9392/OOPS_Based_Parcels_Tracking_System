import copy
class Parcel:
    def __init__(self,p_id,zone,day,cap,priority):
        self.Parcel_id=p_id
        self.Zone=zone
        self.Arrival_day=day
        self.Capacity=cap
        self.Priority=priority
class Locker:
    def __init__(self,l_id,zone,cap,max_parcels):
        self.Locker_id=l_id
        self.Zone=zone
        self.Capacity=cap
        self.Max_parcels=max_parcels
class LockerHub:
    def __init__(self,parcels,lockers):
        self.Parcels=parcels
        self.Lockers=lockers
    def assign_parcels(self,cutoff_day):
        self.Parcels=sorted(self.Parcels,key=lambda x:x.Priority,reverse=True)
        self.Lockers=sorted(self.Lockers,key=lambda x:x.Locker_id)

        for parcel in self.Parcels:
            if parcel.Arrival_day<=cutoff_day:
                for locker in self.Lockers:
                    if locker.Zone.upper()==parcel.Zone.upper() and parcel.Capacity<=locker.Capacity and locker.Max_parcels>0:
                        locker.Capacity-=parcel.Capacity
                        locker.Max_parcels-=1
                        print(f"{parcel.Parcel_id} {locker.Locker_id} {locker.Capacity}")
                        break

            else:
                pass

    def make_report(self,parcels,lockers):
        report={}
        for parcel in parcels:
            if parcel.Zone.upper() not in report:
                report[parcel.Zone.upper()]=[1,0,0,0]
            else:
                report[parcel.Zone.upper()][0]+=1
        for locker in lockers:
            report[locker.Zone.upper()][2]+=1
        updated_parcel = {}
        for parcel in parcels:
            if parcel.Zone.upper() not in updated_parcel:
                updated_parcel[parcel.Zone.upper()]=[0,0]
        for locker in self.Lockers:

            if locker.Zone.upper() not in updated_parcel:
                updated_parcel[locker.Zone.upper()]=[locker.Max_parcels,locker.Capacity]
            else:
                updated_parcel[locker.Zone.upper()][0]+=locker.Max_parcels
                updated_parcel[locker.Zone.upper()][1]+=locker.Capacity

        input_parcel = {}
        for parcel in parcels:
            if parcel.Zone.upper() not in input_parcel:
                input_parcel[parcel.Zone.upper()]=[0,0]
        for locker in lockers:

            if locker.Zone.upper() not in input_parcel:
                input_parcel[locker.Zone.upper()] = [locker.Max_parcels, locker.Capacity]
            else:
                input_parcel[locker.Zone.upper()][0] += locker.Max_parcels
                input_parcel[locker.Zone.upper()][1] += locker.Capacity
        for zone in report:
            report[zone][1]=input_parcel[zone][0]-updated_parcel[zone][0]
            if input_parcel[zone][1]!=0:
                report[zone][3]=int((input_parcel[zone][1]-updated_parcel[zone][1])/input_parcel[zone][1]*100)
        assigned=0
        for zone in report:
            assigned+=report[zone][1]
        if assigned==0:
            print("No Parcels Assigned")


        for zone in report:
            if report[zone][2]==0:
                print(f"{zone} {report[zone][0]} {report[zone][1]} {report[zone][2]} No_Lockers")
            else:

                print(f"{zone} {report[zone][0]} {report[zone][1]} {report[zone][2]} {report[zone][3]}")








parcels=[]
lockers=[]
no_of_parcels=int(input())
for i in range(no_of_parcels):
    temp=input().split(" ")
    p_id=temp[0]
    zone=temp[1]
    day=int(temp[2])
    cap=int(temp[3])
    priority=int(temp[4])
    parcels.append(Parcel(p_id,zone,day,cap,priority))
no_of_lockers=int(input())
for i in range(no_of_lockers):
    temp = input().split(" ")
    l_id = temp[0]
    zone = temp[1]
    cap = int(temp[2])
    max_parcels=int(temp[3])
    lockers.append(Locker(l_id,zone,cap,max_parcels))
lockers1 = copy.deepcopy(lockers)
parcels1 = copy.deepcopy(parcels)
hub=LockerHub(parcels,lockers)
cutoff_day=int(input())
hub.assign_parcels(cutoff_day)

hub.make_report(parcels1,lockers1)







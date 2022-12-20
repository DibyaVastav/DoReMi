from sys import argv
from datetime import date, timedelta


class Subs:
    allsubs = []
    def __init__(self, type, subtype, start_date):
        self.type = type
        self.subtype = subtype
        self.start_date = start_date
        

        def calculate_end_date(self):
            if self.subtype == "PERSONAL":
                if self.start_date.month != 12:
                    return(date(self.start_date.year, self.start_date.month + 1, self.start_date.day))
                else:
                    return(date(self.start_date.year + 1, 1, self.start_date.day))
            elif self.subtype == "FREE":
                if self.start_date.month != 12:
                    return(date(self.start_date.year, (self.start_date.month + 1), self.start_date.day))
                else:
                    return(date((self.start_date.year + 1), 1, self.start_date.day))
            elif self.subtype == "PREMIUM":                    
                if self.start_date.month < 10:
                    return(date(self.start_date.year, (self.start_date.month + 3), self.start_date.day))
                else:
                    m = self.start_date.month -9
                    return(date((self.start_date.year + 1), m, self.start_date.day))

        def calculate_cost(self):
            if self.subtype == "FREE":
                cost = 0
                return cost
            if self.subtype == "PERSONAL":
                if self.type == "MUSIC":
                    cost = 100
                elif self.type == "VIDEO":
                    cost = 200
                elif self.type == "PODCAST":
                    cost = 100

                return cost
            
            if self.subtype == "PREMIUM":
                if self.type == "MUSIC":
                    cost = 250
                elif self.type == "VIDEO":
                    cost = 500
                elif self.type == "PODCAST":
                    cost = 300
                return cost
        self.end_date = calculate_end_date(self)
        self.ren_date = self.end_date - timedelta (days= 10)
        self.cost = calculate_cost(self)
        #print ("Sub created")
        Subs.allsubs.append(self)


    def __repr__(self) -> str:
        return (f"{self.type}, {self.subtype}, {self.start_date}")


class Topup:
    alltopup = []
    def __init__(self, type, num):
        self.type = type
        self.num = num
        
        #print ("Topup created")
        def calculate_cost (type, num):
            if type == "FOUR_DEVICE":
                cost = 50 * int(num)
            elif type == "TEN_DEVICE":
                cost = 100 * int(num)
            return cost

        self.cost = calculate_cost(self.type, self.num)
        Topup.alltopup.append(self)

    def __repr__(self) -> str:
        return (f"{self.type}, {self.num}, {self.cost}")


if __name__ == "__main__":
 
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path1 = argv[1]
    f1 = open(file_path1, 'r')
    Lines1 = f1.read().splitlines()
    f1.close
    Lines1.pop()
    create_class = 0
    renewals = []
    Lines=[]
    for line in Lines1:
        Lines.append(line.split(" "))
    
    for line in Lines:
        if line[0] == "START_SUBSCRIPTION":
            temp = line[1].split("-")
            if 0<int(temp[0])<32 and 0 <int(temp[1]) <13:
                start_date = date( int(temp[2]), int(temp[1]), int(temp[0]))
            else:
                print("INVALID_DATE")
                start_date = "INVALID_DATE"
        
        elif line[0] == "ADD_SUBSCRIPTION":
            if start_date == "INVALID_DATE":
                print ("ADD_SUBSCRIPTION_FAILED INVALID_DATE")
    
            else:
                for inst in Subs.allsubs:
                    if inst.type == line[1]:
                        create_class = 1
                        
                if create_class == 1:
                    print ("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY")
                else:
                    sub1 = Subs(line[1], line[2], start_date)
                    renewals.append("RENEWAL_REMINDER" +" "+ line[1] + " " + sub1.ren_date.strftime("%d-%m-%Y"))

        elif line[0] == "ADD_TOPUP":
            if start_date == "INVALID_DATE":
                print ("ADD_TOPUP_FAILED INVALID_DATE")
                break
            if len(Subs.allsubs) == 0:
                print("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")

            elif len(Topup.alltopup)>0:
                print ("ADD_TOPUP_FAILED DUPLICATE_TOPUP")

            else:
                t1 = Topup(line[1], line[2])

        else:
            print ("invalid request")
    total_cost = 0
    for x in Subs.allsubs:
        total_cost += x.cost
    for y in Topup.alltopup:
        total_cost += y.cost

    if len(Subs.allsubs) == 0:
        print ("SUBSCRIPTIONS_NOT_FOUND")
    else:
        for renew in renewals:
            print (renew)
        print ("RENEWAL_AMOUNT" + " " + str(total_cost))
   
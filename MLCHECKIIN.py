
__Author__ ="Mouza Alameri"

__Date__ = "15/05/2025"


from sklearn.linear_model import LogisticRegression

class sec_check_in: 
    def __init__(self):
        pass

    def run(self): 
        print("Welcome, to the cybersecurity check in ")
        
        change = int(input("how many months ago did u change ur password ?  "))
        twof = input("do you 2f authentication ? ")
        link = input ("did u press on any sus links ? ")
        
        if change > 6 or twof == "no" or link == "yes" :
            print("ur at risk u need to make the following adjucements")
            
        if change > 6 : 
            print("change ur password its been too long!")
        if twof =="no": 
            print("implement two factor authentication") 
        if link =="yes": 
            print("run malware scan")
        else: 
            print("all is good")

prototype = sec_check_in()
prototype.run()
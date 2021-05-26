import random 
sportsman=[] 
results=[] 
mins=50 
b = sorted(results) 
def names(sportsman,results): 
    for i in range (3): 
        man=(input("имя спортсмена ?")) 
        result=random.randint(3,60) 
        sportsman.append(man) 
        results.append(result)
    return sportsman,results

def SpisokDej(jhj, asda):
    print("         \n лучшие результаты-BestRes \n дисквалификация-WorstRes\n 3 лучших результата-top3 \n         ")
    vibor=input("выбирай...")
    if vibor=='BestRes':
        luchshij(Fresults_dict)
        
    elif vibor=='WorstRes':
        Worst(Fresults_dict)
    
    elif vibor=='top3':
        top4ik(Fresults_dict)

def luchshij(fresults_dict):
    c = sorted(Fresults_dict)
    print('лучший результат это:',c[0],'минут',Fresults_dict[c[0]])

def top4ik(fresults_dict):
    c = sorted(Fresults_dict)
    print('первое место:',c[0],'минут',Fresults_dict[c[0]])
    print('второе место:',c[1],'минут',Fresults_dict[c[1]])
    print('третье место:',c[2],'минут',Fresults_dict[c[2]])   

def Worst(c):
    c = sorted(Fresults_dict)
    print('лучший результат это:',c[2],'минут',Fresults_dict[c[2]])
    c.pop(2)

sportsman, results=names(sportsman, results)
Fresults_dict = dict(zip(results, sportsman))
while True:
    SpisokDej(Fresults_dict, Worst)

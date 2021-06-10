import random
from merge import merge_dicts

# for determining pull rewards
def pull(one, ten, pullno, pack, distribution):

    #pull list (categorized)
    Srank = dict(Luci = "S")
    Arank = dict(kamui="A", Lucia="A", Lee="A", Watanabe="A", Liv="A")
    Brank = dict(weapon="B", weaponenhance="B", stamina="B", Luckybag="B", Stigs="B")
    Crank = dict(stigs="C")

    #pull list (whole)
    Whole = merge_dicts(Srank, Arank, Brank, Crank)

    #Making pull list according to pull type

    if(one):
        item = random.choices(list(Whole.items()), distribution)
        print(item)
    elif(ten):
        item = random.choices(list(Whole.items()), distribution, k=9)

        if pullno >=100 and pack>=10:
            item.append(list(Srank.items()))
        else:
            item.append(random.choices(list(Arank.items()), (.50, .50, .50, .50, .50)))
        print(item)
    else:
        #pack+=1
        print("nothing")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def pullcounter(pullno, pack):
    if pullno % 10 == 0:
        pack = pullno / 10
        distribution = [.00, .0, .0, .0, .0, .50, .80, .80, .80, .80, .80, .80]
        pullno = 1
        pack += 1
    elif pack  >= 10:
        distribution = [.100, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0]
    else:
        distribution = [.0, .10, .10, .10, .05, .05, .70, .80, .70, .80, .70, .80]
    return pullno,pack, distribution
#++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pullno = 0 #for incrementing
    pack = 0 #each 10 is counted as 1 pack
    one = 0 #no of pulls chosen by user
    ten = 0 #no of pulls chosen by user
    pulls = 0 #pull count for display

    while True:
        print("=======================================================")
        pull_type =int(input("Choose 1 or 10: "))
        if (pull_type == 1):
            one = True
            pullno += 1
            pulls += 1
        elif (pull_type == 10):
            ten = True
            pullno += 10
            pulls += 10
        count, pack, dis = pullcounter(pullno, pack)
        pull(one,ten, pulls, pack, dis)

        i = int(input(f"Pull count {pulls} Do you wish to continue: "))
        print("=======================================================")
        if(i == 1):
            exit(0)
        else:
            continue
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

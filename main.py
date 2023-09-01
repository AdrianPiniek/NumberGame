import random
numbers_used = []


def create_set(limit: int = 20):
    global ranking
    ranking = {}
    for i in range(1,limit+1):
        ranking[i] = None
    return ranking

def gen_number(user_number)->int:
    while True:
        rand = random.randint(1,user_number)
        if rand in numbers_used:
            continue
        numbers_used.append(rand)
        return rand 

def set_max_number(max_number:int = 999):
    if max_number <= len(ranking):
        print("Common make it harder :/")
        
        return False
    return True

def get_max_number():
    while True:
        num = int(input("Give how high the numbers should be: "))
        if set_max_number(num):
            return num
            
def print_ranking():
    for i in range(1,len(ranking)+1):
        print(f"{i}: {'----' if ranking[i] is None else ranking[i]}")
        
def check_place(place):
    if place > len(ranking):
        print("Out of scope!")
        return False 
    if ranking[place] is not None:
        print("Place already taken :(")
        return False
    return True


def check_game(): #IT COULD BE THE WORST OPTIMAZED PLACE CHEKCER EVER BUT WORKS AND NOBODY WOULD PLAY YHIS
    #TODO JESUS OPTIMAZE IT A LITTLE PLEASE
    i = 1
    
    while i < len(ranking)+1:
        if ranking[i] is not None:
            min_num = ranking[i]
            for j in range(i+1,len(ranking)+1):
                if ranking[j] is not None:
                    next_num = ranking[j]
                    if min_num > next_num:
                        print("YOU LOST!!")
                        return -1
                    
        i+=1    



def game_start(turns:int):
    saved_num = False
    points = 0
    create_set(user_ranking)
    
    given_number = get_max_number()
    
    while turns > 0:
        if not saved_num:
            number = gen_number(given_number)
        place = int(input(f"Give place for {number}: "))
        if check_place(place) == False:
            saved_num = True
            continue
        
        saved_num = False
        turns -= 1
        ranking[place] = number
        if check_game() == -1:
            print(f"Earned points: {points}")
            return False
        print_ranking()
        points += 1
    print("Congrats you made it!!!")
        
    
    
    
if __name__ == '__main__':
    user_ranking = int(input("Give how many numbers you want to place: "))
    
    game_start(user_ranking)

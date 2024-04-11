
from random import choice,randint
bots=['ahmet','mehmet','ayşe']
minimum_bet = 100
user_dict={
    '1':{
        'user_name':'beast',
        'password':'123',
        'safe':1200

    },
    '2':{
        'user_name':'savage',
        'password':'123',
        'safe':2000
    },
}
def assing_default_player(bot_lst:list)->str:
    return choice(bot_lst)
def roll_dice()->int:
    return  randint(2,12)
def gain_daily_chips()-> int:
    return randint(1000,2000)
def is_bet_valid(current_bet:int,safe:int)->bool:
    if minimum_bet<=current_bet<=safe:
        return True
    else:
        return False
def login(user_name:str,password:str)->dict:
    is_active=False
    user_id=''
    for i in range(1,len(user_dict)+1):
        if user_dict.get(str(i)).get('user_name')==user_name and user_dict.get(str(i)).get('password')==password:
            is_active=True
            user_id=str(i)
            break
    if is_active:
        return user_dict.get(user_id)
    else:
        return {}
def update_safe(user:dict,gained_chip:int)->None:
    user.update({
     'safe':user.get('safe')+gained_chip
    })
def main():
    auth_user=login(
        input('User Name : '),
        input('Password : ')
    )

    if auth_user!= {}:
        daily_chips=gain_daily_chips()
        update_safe(auth_user,daily_chips)
        print(f'Welcome {auth_user.get('user-name')},you gain {daily_chips} and so your safe is {auth_user.get("safe")}')
        while True:
            if auth_user.get('safe')>=minimum_bet:
                bet = int(input('please make a bet : '))
                if is_bet_valid(bet,auth_user.get('safe')):
                    player=assing_default_player(bots)
                    print(f'Your oppent name is {player}..!\nLets play ..!')

                    player_1_roll=roll_dice()
                    player_2_roll=roll_dice()

                    if player_1_roll>player_2_roll:
                        auth_user.update({
                            'safe':auth_user.get('safe')+(bet*2)
                        })
                        print(f'Your dice is {player_1_roll}\n{player} dice is {player_2_roll}')
                        print(f'Congratualtaions {auth_user.get('user_name')}..!\nYour current safe is {auth_user.get('safe')}')

                    elif  player_2_roll>player_1_roll:
                        auth_user.update({
                            'safe': auth_user.get('safe') - (bet)
                        })
                        print(f'Your dice is {player_1_roll}\n{player} dice is {player_2_roll}')
                        print(
                            f'You lose {auth_user.get('user_name')}..!\nYour current safe is {auth_user.get('safe')}')
                    else:
                        print('Players are tie ..!')
                else:
                    print('Please make a valid bet..!')
            else:
                print('Your safe is under the minimum table bet..!\n Do you want to buy any chips? ')
                break
    else:
        print('Invalid credantial ..! ')
main()
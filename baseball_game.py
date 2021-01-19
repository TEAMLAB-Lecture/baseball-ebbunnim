# -*- coding: utf-8 -*-
import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    for c in user_input_number:
        if not c.isdigit():
            return False
    return True


def is_between_100_and_999(user_input_number):
    return 100<=int(user_input_number)<1000


def is_duplicated_number(three_digit):
    return len(set(three_digit))!=3


def is_validated_number(user_input_number):
    if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number):
        return True
    return False


def get_not_duplicated_three_digit_number():
    while True:
        num=get_random_number()
        if len(set(str(num)))==3:
            return num


def get_strikes_or_ball(user_input_number, random_number):
    rand_num=str(random_number)
    strike,ball=0,0
    for i in range(3):
        target=user_input_number[i]
        if target==rand_num[i]:
            strike+=1
        elif target in rand_num:
            ball+=1
    return [strike,ball]


def is_yes(one_more_input):
    if one_more_input.lower() in ('y', 'yes'):
        return True
    return False


def is_no(one_more_input):
    if one_more_input.lower() in ('n', 'no'):
        return True
    return False


def main():
    print("Play Baseball")
    user_input=999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    flag=0
    user_input = input('Input guess number : ')
    while not flag:
        if is_validated_number(user_input):
            res=get_strikes_or_ball(user_input,random_number)
            print(f"Strikes : {res[0]} , Balls : {res[1]}")
            if res==[3,0]:
                user_input=input('You win, one more(Y/N)?')
                while True:
                    if is_yes(user_input):
                        random_number = str(get_not_duplicated_three_digit_number())
                        print("Random Number is : ", random_number)
                        user_input = input('Input guess number : ')
                        break
                    elif is_no(user_input):
                        flag=1
                        break
                    else:
                        print('Wrong Input, Input again')
                        user_input = input('Input guess number : ')
            else:
                user_input = input('Input guess number : ')
        elif user_input=='0':
            flag=1
            break
        else:
            print('Wrong Input, Input again')
            user_input = input('Input guess number : ')
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()

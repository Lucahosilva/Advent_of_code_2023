
def make_dic():
    dic={}

    with open('day2/input.txt', 'r') as file:
        for line in file:

            game_id = int(line.split(':')[0].split()[1])
            dic[game_id] = [x.strip() for x in line.split(":")[1].replace(";",",").split(",")]

    return dic


def match_game(dic: dict):

    sum_of_possible_game_ids = 0
    sum_of_power = 0

    for key, value in dic.items():
        red, green, blue = 0, 0, 0

        for  _, colors in enumerate(value):
            color = colors.split()[1]
            num = int(colors.split()[0])

            if color == "red" and num > red: 
                red = num
            if color == "green" and num > green: 
                green = num 
            if color == "blue" and num > blue: 
                blue = num

        if red <= 12 and green <= 13 and blue <= 14:              
            sum_of_possible_game_ids += int(key)
        sum_of_power += red*green*blue

    print(sum_of_power)


    
    

dic = make_dic()
match_game(dic)
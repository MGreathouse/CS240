# Marcus Greathouse
# Programming Project: Chapter 8-2


#gets the data from the file
def get_data_list(file_name):
    with open(file_name) as data_file:
        data_list = [line.strip().split(',') for line in data_file]
    return data_list


#convert the information into desired data
def get_efficiency(data_list):
    efficiency_list = []

    #convert each player's stats into an efficiency and return the list
    for stats in data_list:
        name = stats[1] + ' ' + stats[2]
        pts = int(stats[6])
        reb = int(stats[9])
        asts = int(stats[10])
        stl = int(stats[11])
        blk = int(stats[12])
        fga = int(stats[15])
        fgm = int(stats[16])
        fta = int(stats[17])
        ftm = int(stats[18])
        turnover = int(stats[13])
        gp = int(stats[4])
        efficiency = ((pts + reb + asts + stl + blk) - ((fga - fgm) + (fta - ftm) + turnover)) / gp

        efficiency_list.append((str(efficiency), name))

    return efficiency_list


#display top 50
def print_top_50(efficiency_list):
    efficiency_list.sort(reverse=True)

    print('Top 50 NBA players of Alltime')
    for player in efficiency_list[0:50]:
        print('{0:{width}}{1}'.format(player[1],player[0], width=25))


#main function
def main():
    data_list = get_data_list('player_career.csv')
    efficiency_list = get_efficiency(data_list[1:])
    print_top_50(efficiency_list)


if __name__ == '__main__':
    main()

# book provided function to read csv spreadsheet and split the data apart
def get_data_list(file_name):
    data_file = open(file_name, 'r')
    data_list = []              #start with an empty list
    for line_str in data_file:
        # strip end-of-line, split on commas and append items to list
        data_list.append(line_str.strip().split(','))
    return data_list


# book required function to get average for a month
def get_monthly_averages(data_list):
    current_date = data_list[0][0].split('-')
    current_data_pool = [] #blank list

    monthly_averages = [] #blank list
    for data in data_list:
        #get the date and see if it is in the right range
        data_date = data[0].split('-')
        if data_date[1] == current_date[1]:
            #this is the same month
            current_data_pool.append([int(data[5]), float(data[6])])#volume,adjusted price
        else:
            #time for the next month - calc average and setup for next
            vol_price = 0
            vol_total = 0
            for day in current_data_pool:
                vol_price += day[0] * day[1]
                vol_total += day[0]

            # get the average
            average_price = vol_price / vol_total
            average = (current_date[0] + '-' + current_date[1], "{0:.2f}".format(round(average_price,2)))
            monthly_averages.append(average)

            #clear out the old data and add in the new data
            current_data_pool = []
            current_date = data_date
            #first bit of data for new month
            current_data_pool.append([int(data[5]), float(data[6])])#volume,adjusted price

    return monthly_averages


# book require function to display averages
def print_info(monthly_averages):
    best_six = []
    worst_six = []

    #sort based off of the second value in the tuple (the average)
    monthly_averages.sort(key=lambda x: x[1], reverse=True)

    #get the best and worst six
    best_six = monthly_averages[0:6]
    worst_six = monthly_averages[-7:-1]

    #display results
    print(monthly_averages)
    print('Best Six Months')
    for month in best_six:
        print('{0}\t\t${1}'.format(*month))

    print('\nWorst Six Months')
    for month in worst_six:
        print('{0}\t\t${1}'.format(*month))


# main function
def main():
    data_list = get_data_list('table.csv')
    monthly_averages = get_monthly_averages(data_list[1:])
    print_info(monthly_averages)


if __name__ == '__main__':
    main()

def melon_delivery_report():
    '''Create a report of melons delivered'''

    #The 3 log files where data is stored
    files = ("um-deliveries-20140519.txt","um-deliveries-20140519.txt","um-deliveries-20140519.txt")

    #For every file index
    for i in range(len(files)):

        #Print Day number as header 
        print(f"\n\nDay {i+1}\n---------")
        
        #Open file for the day
        the_file = open(files[i])

        #Read file, line by line
        for line in the_file:
            
            #Strip any extra whitespace at end of line
            line = line.rstrip()

            #Split lines based on delimiter
            words = line.split('|')

            #Capture line components into melon, count, amount
            melon = words[0]
            count = int(words[1])
            amount = count * float(words[2])

            #Print report
            print(f"Delivered {count} {melon}s for total of ${amount}")

        #Close file
        the_file.close()

#Call above function
melon_delivery_report()
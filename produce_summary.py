def melon_delivery_report(file_name):
    '''Create a report of melons delivered'''

    #The 3 log files where data is stored
    files = {
        "um-deliveries-20140519.txt": 1,
        "um-deliveries-20140520.txt": 2,
        "um-deliveries-20140521.txt": 3
    }

    #Check that the file name argument is valid
    if file_name not in files:
        print("File does not exist, please check your input")
        return False

    else:

        #Print Day number as header 
        print(f"\n\nDAY {files[file_name]}\n---------")
     
        #Open file for the day
        the_file = open(file_name)

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
            print(f"Delivered {count:3} {melon}s for total of ${amount:.2f}")

    #Close file
    the_file.close()

#Call above function
melon_delivery_report("um-deliveries-20140519.txt")
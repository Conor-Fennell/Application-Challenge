
#I am assuming that the array may or not be ordered, and it may take positive and negative integers

def mostFreq(array):
    #Checking if the array is empty or is of type None
    if(array == None):
        return None

    if(len(array) < 1):
        return None
        
    frequency = {}  #Create a dictionary/hash table and store the pair (number: frequency)
    #Looping through the input array
    for num in array:
        if(num in frequency):  #If out number has already been encountered, iterate its frequency by 1
            frequency[num] = frequency[num] + 1
        else: #Else the number is being encountered for the first time, add it to the dictionary with frequency of 1 
            frequency.update({num: 1})

    print("Number: Frequency")    
    print(frequency)

    #This gives us the list containing the integer which appeared most frequently
    #If multiple integers appear most frequenctly we return a list containing each of those numbers
    mostFreq = [num for (num, freq) in frequency.items() if freq == max(frequency.values())]

    #If instead we assume that only a single integer will have the highest frequency,
    #or we assume we can just return the 1st integer we encounter with the highest frequency:
    #mostFreq = max(frequency, key=frequency.get)

    #^^^This is good because its quicker than making a list of max frequency values
    #But not so good because we are missing the other elements which appeared just as frequenctly

    print("The most frequent integer(s) in the array is: "+str(mostFreq))
    return mostFreq

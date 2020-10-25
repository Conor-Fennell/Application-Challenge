
def reverseIterative(string):
    if(string == None):  #If the string is None, return None
        print("Inputted None")
        return None
    n = (len(string)-1)  #Get the length of the string-1 (the iterable length)
    if(n<=0):    #If the iterable length is less or equal to 0, return ther string
        print("Inputted empty string")
        return string
    reverse_string = "" #Create an empty string, this will hold our reversed string
    print("Inputted: "+string)
    while(0<=n):
        reverse_string+=(string[n])  #add the chars of the input string to the empty string in reversed order
        n=n-1 #iterate down from last to first char
    print(string," -> ",reverse_string)
    return reverse_string

def reverseRecurse(string):
    if(string == None): #If the string is None, return None
        return None
    if(len(string)==0): #If the iterable length is less or equal to 0, return the string
        return string   
    #Now we return the last character of the string
    #and call reverseRecurse for every character except the last 
    return string[-1] + reverseRecurse(string[0:-1])
    
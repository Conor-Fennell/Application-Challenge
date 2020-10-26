from django.shortcuts import render
from django.http import HttpResponse
from .forms import inputForm #importing so we can use the data from the inputted string to pass to our reverse function

from .task2 import reverseIterative #lets use our task 2 to reverse the input string

# Create your views here
def home(request):
    if (request.method == 'POST'):
        form = inputForm(request.POST) #if we have a post request, form is our current forms input details

        if form.is_valid():
            string = form['string'] #string is the inputted string in our form
            #We get the inputted string as plain text using string.value()
            reversed_string = reverseIterative(string.value()) #calling the function we used in task 2 

            #Put out reversed string in a dictionary, we send this data and render it on the html page
            data = {
                'string': reversed_string,
                'form': form
            }
            return render(request, 'task3/home.html', {'data': data})

    form  = inputForm() #create an empty form

    return render(request, 'task3/home.html', {'form': form}) #renders our home.html page, displays on web browser

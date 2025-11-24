import webbrowser   # importing webbrowser and matplotlib modules. webbrowser allows the user to directly open a url in the default browser 
# matplotlib is used for data visualization 
import matplotlib.pyplot as plt 
print ('hello! how are you feeling today?') 
a=str(input()) # takeing string input from the user 
if 'anxious' in a :
    print('stay calm')
    print ('take some breath') # words of aiffermation are provided according to a keyword with the help of if conditional statement 
    print('i recommend you to perform guided meditations,sleep stories and breathing exercises to help reduce anxiety ') 
    print( 'the follwing app will provide help ') 
    url='https://www.calm.com/' # suggested app url 
    b=str(input('do you want to open app now? :'))
    if 'yes' in b: # using nested if to ask the user for redirecting them to the app 
        webbrowser.open(url) 
        
    if 'no' in b:
        print('okay,i suggest you to read the book- code review  anxiety workbook') 
        
if 'burnout'in a: 
    print('it is okay to take rest sometimes')
    print('i reccomend you to perform yoga and meditation ' )      # words of aiffermation are provided according to a keyword with the help of if conditional statement 
    print ( 'i can suggest you an app') 
    url1='https://www.headspace.com/'
    b=str(input('do you want to open app now? :'))
    if 'yes' in b:
        webbrowser.open(url1) 
    if 'no' in b:
        print('okay,i suggest you to read the book- i cant do it all:my burnout story-by molly struve') 
        
if 'stress' in a:
    print('Breathe.let your stress fly away')
    print('focus on one thing at a time') 
    print('i can help you by providing some articles to reduce stress')  # words of aiffermation are provided according to a keyword with the help of if conditional statement 
    url2='https://sanvello.com/'
    b=str(input('do you want to open article now? :'))
    if 'yes' in b:
        webbrowser.open(url2) 
    if 'no' in b:
        print('okay,i suggest you to read the book- it doesnt have to be crazy at work-by jason fried') 
        
if 'hopeless' in a : 
    print ('it is okay to feel bad sometimes')
    print('every thing will be okay')
    print('cheer up!') # words of aiffermation are provided according to a keyword with the help of if conditional statement 
    print('i can suggest you an app that will improve your mood')
    url='https://www.happify.com/'
    b=str(input('do you want to open app now? :'))
    if 'yes' in b:
        webbrowser.open(url) 
    if 'no' in b:
        print('okay,i suggest you to read the article- its okay not to be okay - by andrew montagne') 
        
if 'unhappy' in a:
    print('stay calm')
    print ('take some breath')# words of aiffermation are provided according to a keyword with the help of if conditional statement 
    print('i recommend you to perform guided meditations,sleep stories and breathing exercises to help reduce anxiety ') 
    print( 'the follwing app will provide help ') 
    url='https://www.calm.com/' 
    b=str(input('do you want to open app now? :'))
    if 'yes' in b:
        webbrowser.open(url) 
        
    if 'no' in b:
        print('okay,i suggest you to read the book- code review  anxiety workbook') 
        

if 'lost' in a: 
    print('it is okay to take rest sometimes')
    print('i reccomend you to perform yoga and meditation ' ) 
    print ( 'i can suggest you an app') 
    url1='https://www.headspace.com/'
    b=str(input('do you want to open app now? :'))# words of aiffermation are provided according to a keyword with the help of if conditional statement 
    if 'yes' in b:
        webbrowser.open(url1) 
    if 'no' in b:
        print('okay,i suggest you to read the book- i cant do it all:my burnout story-by molly struve') 
        
if 'negative' in a:
    print('Breathe.let your stress fly away')
    print('focus on one thing at a time') 
    print('i can help you by providing some articles to reduce stress')
    url2='https://sanvello.com/'
    b=str(input('do you want to open article now? :'))
    if 'yes' in b:
        webbrowser.open(url2) 
    if 'no' in b:
        print('okay,i suggest you to read the book- it doesnt have to be crazy at work-by jason fried') 
        
if 'sad' in a:
    print ('it is okay to feel bad sometimes')
    print('every thing will be okay')
    print('cheer up!')
    print('i can suggest you an app that will improve your mood')# words of aiffermation are provided according to a keyword with the help of if conditional statement 
    url='https://www.happify.com/'
    b=str(input('do you want to open app now? :'))
    if 'yes' in b:
        webbrowser.open(url) 
    if 'no' in b:
        print('okay,i suggest you to read the article- its okay not to be okay - by andrew montagne') 
        
c=str(input('do you want to generate -my feeling report ?'))  # asking the user if the want to generate my feeling report 
if 'yes' in c:
    moods=['happy','anxious','sad','normal','hopeless'] 
    days_in_month=[9,4,10,8,10] 
    plt.pie(days_in_month,autopct='%.1f%%',labels=moods)
    plt.legend()
    plt.show()    # using matplot lib library in order to plot a pie chart for monthly mood change tracker 
    print('thankyou!')
if 'no' in c:
    print('thankyou!') # salutation 




import urllib2
from HTMLParser import HTMLParser

# Open and read Positive words 

file = open("pos-words.txt")
poswords = file.readlines()

# Open and read Stopwords words 

file = open("stop-words.txt")
stopwords = file.readlines()
    

# Function - Filter Positive words 

def filter_poswords(if_pos_word):
    global poswords
    for words in poswords:
        if words.strip() == if_pos_word.strip():
            return "true"
    return "false"

# Function - Filter Stopwords words    
    
def filter_stopwords(filtered):
    global stopwords
    for words in stopwords:
        filtered = filtered.replace(" " + words.strip() + " ", " ")
    return filtered
    
# Class and function to Remove HTML 
    
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



# Start 
    
input = raw_input("Hi, I'm chatbot. What's your Name? ")
firstQ = input

# Call Filter Stopwords words 

response = filter_stopwords(" " + firstQ.lower() + " ")


# Second question
input = raw_input("Hey " + response.strip() + ", how are you feeling today? ")
secondQ = input

# Call Filter Stopwords words 

response = filter_stopwords(" " + secondQ.strip().lower() + " ")

# Call Filter Positive words 
if_pos_word = filter_poswords(" " +  response + " ")

# Check If positive or not

if if_pos_word == "true":
    input = raw_input( response.strip() + ", Well that's good for you. In that case what are you going to do today? ")
else:
    input = raw_input( response.strip() + ", Well don't tell me your problems. What are you going to do today? ")

# Third question
    
thirdQ = input    

# Loop wikipedia
        
while True:
    response = filter_stopwords(" " + thirdQ.strip().lower() + " ")
    
    # Open URL to wikipedia
    
    try:
        openURL = urllib2.urlopen("https://en.wikipedia.org/wiki/"+response)
        ReadURL = openURL.read()
        
        # find First <p> HTML tag
        
        find_first_p_tag = ReadURL.find("<p>") + len("<p>")
        find_last_p_tag = ReadURL.find("</p>", find_first_p_tag)

        p = ReadURL[find_first_p_tag:find_last_p_tag]
        p_no_html = strip_tags(p)
        
        # First paragraph 
        
        input = raw_input("Well "+ p_no_html + " " )

        thirdQ = input;
        
    # if HTTP Error like 404 | URL Error | HTTP Exception
    
    except urllib2.HTTPError, e:
        input = raw_input("what? Let's talk about somthing else " )
        thirdQ = input;
    
    except urllib2.URLError, e:
        input = raw_input("what? Let's talk about somthing else " )
        thirdQ = input;
        
    except httplib.HTTPException, e:
        input = raw_input("what? Let's talk about somthing else " )
        thirdQ = input;
        
        
        
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
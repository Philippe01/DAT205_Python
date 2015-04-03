#Import required modules
import twitter, datetime, urllib2, sched, time

# scheduler 60s tweet website
s = sched.scheduler(time.time, time.sleep)

def Tweet_website(sc): 
    file = open("/Users/phillipemarr/Library/Application Support/Google/Chrome/Default/Current Session" )
    Current = file.read()

    #Load twitter keys and secrets from the credentials file into a list
    file = open("Twitter-key.txt")
    cred = file.readline().strip().split(',')

    # Find last URL 
    finding_last_http = Current.rfind("http")
    lenght = Current.find(chr(0), finding_last_http)

    url = Current[finding_last_http:lenght]

    # Open URL and read
    try:
        openURL = urllib2.urlopen(url)
        ReadURL = openURL.read()

        # Find title of page with <title> html tag
        Start_Title = ReadURL.find("<title>") + len("<title>")
        End_Title = ReadURL.find("</title>", Start_Title)
        Title = ReadURL[Start_Title:End_Title]

        #Create a new API wrapper, passing in the credentials one at a time
        api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1], access_token_key=cred[2],access_token_secret=cred[3])

        # Find Current time and date
        Current_time = datetime.datetime.now()


        #Post status update and get the response from Twitter 
        response = "I was just at " + Title + " @ "+ url + " @ " + str(Current_time)
        tweet = api.PostUpdate( response )

        #Print out tweet that should be the status update
        print("Status updated to: " + tweet.text)
        
    # if HTTP Error like 404 | URL Error | HTTP Exception
    except urllib2.HTTPError, e:
        print("Fail to tweet website due to HTTP Error")

    except urllib2.URLError, e:
        print("Fail to tweet website due to URL Error")

    except httplib.HTTPException, e:
        print("Fail to tweet website due to HTTP Exception")
        
    # Call Tweet_website function every 60s
    sc.enter(60, 1, Tweet_website, (sc,))
    

# Call Tweet_website Function after 2s
s.enter(2, 1, Tweet_website, (s,))
s.run()
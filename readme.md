## TRENDING POST GENERATOR


### Description

An Automated LinkedIn post generator was developed to create 
custom content for the most trending events of the day.

The Trending Post Generator obtains the 'Top Google Searches' 
for the day and combines them with prompts sent to 
Chat-GPT to produce the ideal LinkedIn post.

The entire process is effortless, fast, 
and results in highly engaging content for the LinkedIn audience.


### How Does It Work?

The application employs a WebDriver instance with Selenium to 
access Google's daily trends, 
located at: https://trends.google.co.il/trends/trendingsearches/daily?geo=IL&hl=iw

For each trend-item, 
it verifies if the search_count exceeds the value defined as 
MIN_SEARCH_COUNT (specified in the `/helpers/selenium_helper.py` file).

If the condition is met, 
the application proceeds to access the associated article, 
extracts its content, 
and stores it in a dictionary within a search_results List, 
specifically linked to the respective trend-item.

Next, 
the application iterates through the search_results items 
and creates prompts by combining a basic-query text from the 
`base_linkedin_post_prompt.txt` file with the 
saved article content corresponding to each trend-item.

Subsequently, 
the application sends the generated prompt to Chat-GPT, 
utilizing the OpenAI API, 
and saves the resulting conversation's answer in a .txt file 
located in the `/linkedin-posts` directory.


### Instructions:

#### ENV Variables -
Create a `.env` file.

**Openai Api Key (Required)**: 
save your secret key in
`OPENAI_API_KEY` variable.

**Linkedin Login Credentials (Required)**:
save your email and password in
`LINKEDIN_EMAIL` and `LINKEDIN_PASSWORD` variables.

Your `.env` file should look like this:
```commandline
OPENAI_API_KEY=kfdgjlkvldnvkljfdkjdf

LINKEDIN_EMAIL=mymail@gmail.com
LINKEDIN_PASSWORD=secretpassword
```

**Change Prompt**: 

You can set your own default base prompt 
inside the `base_linkedin_post_prompt.txt` file 


**Change Minimum Search Count**: 

Set a different value to get a better results 
by changing the `MIN_SERACH_COUNT` value
in the `/helpers/selenium_helper.py` file


  
### Resources And Libraries
* Selenium
* Openai Api


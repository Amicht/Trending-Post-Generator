## TRENDING POST GENERATOR


### Description

Automated a LinkedIn post, custom for the most trending events of the day.

Trending Post Generator gets the `Top Google Searches` of the day,
combine them with a prompt sent to Chat-GPT 
to create the perfect LinkedIn post.

Effortless, fast and engaging.


### How Does It Work?

The App will first create a WebDriver instance with `Selenium` 
to view Google's daily trends in:
`https://trends.google.co.il/trends/trendingsearches/daily?geo=IL&hl=iw`

For each trend-item, it will check if the search_count 
is bigger then the MIN_SERACH_COUNT 
(defined in the `selenium_helper.py` file). 

If so, it will go to the attached article and take the 
content of that article,
and save it in a dictionary of the trend-item, 
inside a `search_results` List.

Then, the app will loop threw the search_results items
define the prompt by combining a basic-query text
(from the `base_linkedin_post_prompt.txt` file)
with the article-content saved in the trend-item. 

Finally, 
it will send the built prompt to Chat-GPT, 
using Openai API,
and create a `.txt` file with the chat's answer in the 
`linkedin-posts` directory.


### Instructions:

**Openai Api Key (Required)**: 

Create a `.env` file and save your secret key in 
`OPENAI_API_KEY` variable.


**Change Prompt**: 

You can set your own default base prompt 
inside the `base_linkedin_post_prompt.txt` file 


**Change Minimum Search Count**: 

Set a different value to get a better results 
by changing the `MIN_SERACH_COUNT` value
in the `selenium_helper.py` file


  
### Resources And Libraries
* Selenium
* Openai Api


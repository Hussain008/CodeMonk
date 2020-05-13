#for sublime to used external libraries apart from its python 3.3 sandbox
import sys;
sys.path.append('C:\\Users\\gunny\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages')




import sublime
import sublime_plugin

#import for selecting random gfg links
import random

#imports related to web scraping
import requests
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup

#selenium imports for dynamic content 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#import for making threads
import threading



class GeeksCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		res = '/*\n'
		#connect to the gfg page of having 160+ top interview questions
		response  = urllib.request.urlopen('https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/')

        #parse the page using BeautifulSoup
		soup = BeautifulSoup(response.read(),'html.parser')

		#We need to collect all the links in the page
		links = soup.findAll('a')

            #will store only the links of the problems
		valid_links = []


        #question problem links can be identified anc collected
		for link in links : 
			if link.has_attr('href')  and 'practice' in link['href'] and 'problems' in link['href']:
				valid_links.append(link['href'])
            

        #choose a random link 
		random_link = random.choice(valid_links)
		#connect to the problem link
		response  = urllib.request.urlopen(random_link)

		soup = BeautifulSoup(response.read(),'html.parser')

		#find and store the tile of the question
		title = '# '+soup.find(class_='col-lg-12').get_text().lstrip()+'\n\n'

        #find and store the question description and link
		question  = soup.find(class_='problemQuestion')

		res+= title + question.get_text() +'\n\n'+random_link + '\n\n */\n\n'

		#to remove random carraige returns that we were getting 
		res=res.replace('\r','')
            
		response.close()

		self.view.insert(edit, 0, res)



class LeetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		res="/*\n"
		#The below url directs to a random top interview question
		url="https://leetcode.com/problems/random-one-question/top-interview-questions"
        #We use a headless firefox , for the ajax and javascript to load in the website
		browser = self.createHeadlessFirefoxBrowser()

        #go to the url 
		browser.get(url)
		delay = 3

		try:
			#wait till the whole website loads! 
			myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-v3d350')))
			#page is ready

		except TimeoutException:
			print ("Loading took too much time!")
			return
        
        #parsing the html
		html = browser.page_source
		soup = BeautifulSoup(html, 'html.parser')

        
        #This will Print the Question Title
		title = soup.find(class_='css-v3d350').get_text()
		res+='\n'+title+'\n\n'

        #To print the description of the problem
		res+=soup.find(class_='content__u3I1 question-content__JfgR').get_text()+"\n"

        #To select the code section in the editor
		boiler_code = soup.select('div[class=\"CodeMirror-code\"]')[0]

		code = ""

        #we are skipping the first character as it is line number
		for line in boiler_code : 
			i=0
			while(line.text[i].isdigit()) : 
				i+=1
			code +=line.text[i:]+"\n"

        #we find the current problem link
		link_of_current_problem = soup.find_all(attrs={"data-key" : "description"})[0].find('a')['href']
		res+='\n\n'+'https://leetcode.com'+link_of_current_problem+'\n\n */'

		res+='\n\n\n\n\n' + code + '\n\n'

		browser.close()
		self.view.insert(edit, 0, res)


	def createHeadlessFirefoxBrowser(self):
		options = webdriver.FirefoxOptions()
		options.add_argument('--headless')
		return webdriver.Firefox(options=options,executable_path='C:\\Users\\gunny\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe')
		# return webdriver.Firefox(options=options,executable_path='geckodriver-v0.26.0-win64\\geckodriver.exe')



class codemodeCommand(sublime_plugin.TextCommand) : 
	def run(self,edit) : 
		code = '#include <bits/stdc++.h>\n#define ll long long\nusing namespace std;\nll mod = 1e9+7 ;\n\n\nint main()\n{\n\n\t#ifndef ONLINE_JUDGE\n\tfreopen("input.txt","r",stdin);\n\tfreopen("output.txt","w",stdout);\n\t#endif\n\n\n\t//fast I/O\n\tios_base::sync_with_stdio(false);\n\tcin.tie(NULL);\n\n\n\tint testcases;\n\tcin>>testcases;\n\n\n\twhile(testcases--){\n\n\t\tlong long n,k;\n\t\tcin>>n;\n\t\tll arr[n];\n\t\tfor (int i = 0; i < n; ++i)\n\t\t{\n\t\t\tcin>>arr[i];\n\t\t}\n\n\t}\n  return 0;\n}'
		self.view.insert(edit,0,code)
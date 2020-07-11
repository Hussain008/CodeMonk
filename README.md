# CodeMonk
Sublime Text Plugin for solving problems for Leetcode and GFG . This Sublime Text Plugin has 3 functionalities : 
- I) To fetch random top interview problems off Leetcode with boilerplate code
- II) To fetch random top interview problems off GeeksForGeeks 
- III) To insert a c++ template for competitve programming environment

## Requirements
- Python 3
- Libraries in python needed : Selenium , BeautifulSoup
- GeckoDriver

## Usage
Simply download and place the files in Packages folder of Sublime Text.
- I) Ctrl + Alt + L or run command Leetcode
- II) Ctrl + Alt + G  run command Geek for Geeks
- III) Ctrl + Alt + C or run command cpp template

 ![GFG_demo](img/gfg)
 
 ![Leetcode_demo](img/leetcode_final)




## Changes Needed 

In the DSA_Practice_Monk.py file , 

```python
sys.path.append('C:\\Users\\gunny\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages')
```
change the above location to your system's python site packages folder.

Also in the same file , in the function createHeadlessFirefoxBrowser , 
```python
return webdriver.Firefox(options=options,executable_path='C:\\Users\\gunny\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe')
```

change the above path to your local geckodriver file location.
		

from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import string

driver=webdriver.Chrome('S:\\softwares\\chromedriver.exe')
chrs=list(string.ascii_uppercase)
chrs.append("1")
url="https://www.filmyquotes.com/movies/list/"
urls=[]
for i in chrs:
        driver.get(url+i)
        elem=driver.find_elements_by_class_name("list-group-item")
        for i in range(1,len(elem)):
                urls.append(elem[i].get_attribute("href"))
movies_counter=0
movies=open("C:\\Users\\Sagar\\Desktop\\movies-names.txt","w")
quotes=open("C:\\Users\\Sagar\\Desktop\\movies-quotes.txt","w")
l=[]
for i in urls:
        movies_counter+=1
        driver.get(i)
        data=driver.find_elements_by_class_name("card-title")
        a=[]
        a.append(data[0].text)
        movies.write(str(movies_counter)+"~"+data[0].text+"\n")
        acpt=1
        quotes_counter=0
        for j in range(1,len(data)):
                if(acpt):
                        quotes_counter+=1
                        a.append(data[j].text)
                        quotes.write(str(movies_counter)+"~"+str(quotes_counter)+"~"+data[j].text+"\n")
                acpt=1-acpt
        l.append(a)
movies.close()
quotes.close()

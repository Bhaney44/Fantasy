#Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

def get_data():
    #--------
    #page 0
    #--------
    html = urlopen("LINK")
    soup = BeautifulSoup(html, 'html.parser')
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n').replace('\n', ' ').replace('\r', '')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip().replace('\n', ' ').replace('\r', '')
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    def write():
        #Openfile
        with open('database.csv', 'a') as csvfile:
            #define fieldnames
            fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date})
    #Call function
    write()

    #--------
    #page 1
    #--------
    
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n').replace('\n', ' ').replace('\r', '')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip().replace('\n', ' ').replace('\r', '')
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    def write():
        #Openfile
        with open('database.csv', 'a') as csvfile:
            #define fieldnames
            fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date})
    #Call function
    write()

    #--------
    #page 2
    #--------
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number 
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n').replace('\n', ' ').replace('\r', '')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip().replace('\n', ' ').replace('\r', '')
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    def write():
        #Openfile
        with open('database.csv', 'a') as csvfile:
            #define fieldnames
            fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date})
    #Call function
    write()

    #--------
    #page 3
    #--------
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n').replace('\n', ' ').replace('\r', '')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip().replace('\n', ' ').replace('\r', '')
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    def write():
        #Openfile
        with open('database.csv', 'a') as csvfile:
            #define fieldnames
            fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date})
    #Call function
    write()

    #--------
    #page 4
    #--------
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('Link'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n').replace('\n', ' ').replace('\r', '')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip().replace('\n', ' ').replace('\r', '')
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    def write():
        #Openfile
        with open('database.csv', 'a') as csvfile:
            #define fieldnames
            fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date})
    #Call function
    write()

get_data()

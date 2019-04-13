#!/bin/bash

sudo apt -y install python3-pip
sudo pip3 install tweepy
sudo pip3 install kafka
sudo pip3 install nltk
sudo pip3 install pandas
sudo pip3 install sklearn
sudo pip3 install unidecode
sudo pip3 install googlemaps
sudo pip3 install gmplot

#The user needs an api keys file located in the path specified above in the Twitter.py file

#main.py: change path in line 12
#gmaps.py: change path in lines 7, 9 and 17
#GeoCoding.py: change path in line 8

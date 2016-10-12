#!/usr/bin/python

from Language import LanguageClass

#------------------------ENGLISH------------------------------------------
Englishfilename = '/home/sachinpc/Desktop/MovieUpdate/MovieDB/English.txt'
EnglishSystemPath1 = '/home/sachinpc/Downloads/New Movies/English'
EnglishSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/English'
English = LanguageClass(Englishfilename)
English.ScrapeMoviesFromDirectories(EnglishSystemPath1,EnglishSystemPath2)
English.WriteListToFile()
#------------------------ENGLISH------------------------------------------


#-----------------------Malayalam-----------------------------------------
Malayalamfilename = '/home/sachinpc/Desktop/MovieUpdate/MovieDB/Malayalam.txt'
MalayalamSystemPath1 = '/home/sachinpc/Downloads/New Movies/Malayalam'
MalayalamSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/Malayalam'
Malayalam = LanguageClass(Malayalamfilename)
Malayalam.ScrapeMoviesFromDirectories(MalayalamSystemPath1,MalayalamSystemPath2)
Malayalam.WriteListToFile()
#-----------------------Malayalam-----------------------------------------

#-----------------------Tamil-----------------------------------------
Tamilfilename = '/home/sachinpc/Desktop/MovieUpdate/MovieDB/Tamil.txt'
TamilSystemPath1 = '/home/sachinpc/Downloads/New Movies/Tamil'
TamilSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/Tamil'
Tamil = LanguageClass(Tamilfilename)
Tamil.ScrapeMoviesFromDirectories(TamilSystemPath1,TamilSystemPath2)
Tamil.WriteListToFile()
#-----------------------Tamil-----------------------------------------


#-----------------------Hindi-----------------------------------------
Hindifilename = '/home/sachinpc/Desktop/MovieUpdate/MovieDB/Hindi.txt'
HindiSystemPath1 = '/home/sachinpc/Downloads/New Movies/Hindi'
HindiSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/Hindi'
Hindi = LanguageClass(Hindifilename)
Hindi.ScrapeMoviesFromDirectories(HindiSystemPath1,HindiSystemPath2)
Hindi.WriteListToFile()
#-----------------------Hindi-----------------------------------------

def SearchMovie():
	movieName = raw_input("Movie Name : ")
	#Searching for movieName in the list
	Languages = [Englishfilename, Malayalamfilename, Tamilfilename, Hindifilename]
	#for file in Languages:
	#	openedFile = open(file)
	#	print openedFile
		#for line in iter(Malayalamfilename):
			#print line
		#openedFile.close()
	for index in range(len(Languages)):
		openedFile = open(Languages[index])
		for line in iter(openedFile):
			print openedFile
			print line
	
#SearchMovie()
	


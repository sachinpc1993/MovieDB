#!/usr/bin/python

from Language import LanguageClass

#------------------------ENGLISH------------------------------------------
Englishfilename = '/home/sachinpc/git/MovieDBProject/MovieDB/English.txt'
EnglishSystemPath1 = '/home/sachinpc/Downloads/New Movies/English'
EnglishSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/English'
English = LanguageClass(Englishfilename)
English.ScrapeMoviesFromDirectories(EnglishSystemPath1,EnglishSystemPath2)
English.WriteListToFile()
#------------------------ENGLISH------------------------------------------


#-----------------------Malayalam-----------------------------------------
Malayalamfilename = '/home/sachinpc/git/MovieDBProject/MovieDB/Malayalam.txt'
MalayalamSystemPath1 = '/home/sachinpc/Downloads/New Movies/Malayalam'
MalayalamSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/Malayalam'
Malayalam = LanguageClass(Malayalamfilename)
Malayalam.ScrapeMoviesFromDirectories(MalayalamSystemPath1,MalayalamSystemPath2)
Malayalam.WriteListToFile()
#-----------------------Malayalam-----------------------------------------

#-----------------------Tamil-----------------------------------------
Tamilfilename = '/home/sachinpc/git/MovieDBProject/MovieDB/Tamil.txt'
TamilSystemPath1 = '/home/sachinpc/Downloads/New Movies/Tamil'
TamilSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/Tamil'
Tamil = LanguageClass(Tamilfilename)
Tamil.ScrapeMoviesFromDirectories(TamilSystemPath1,TamilSystemPath2)
Tamil.WriteListToFile()
#-----------------------Tamil-----------------------------------------


#-----------------------Hindi-----------------------------------------
Hindifilename = '/home/sachinpc/git/MovieDBProject/MovieDB/Hindi.txt'
HindiSystemPath1 = '/home/sachinpc/Downloads/New Movies/Hindi'
HindiSystemPath2 = '/media/sachinpc/Local Disk/Entertainment/Movies/Hindi'
Hindi = LanguageClass(Hindifilename)
Hindi.ScrapeMoviesFromDirectories(HindiSystemPath1,HindiSystemPath2)
Hindi.WriteListToFile()
#-----------------------Hindi-----------------------------------------
	


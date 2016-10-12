import os
import time

class LanguageClass:
		#Writing the Date and Time of data extraction
		Time = time.strftime("%H:%M:%S") # Class Variables that are common between languages
		Date = time.strftime("%d/%m/%Y") # Class Variables that are common between languages
		
		#Constructor to initialize class members
		def __init__(self,fileName):
			self.count = 0 # Count of movies in one Language
			self.movie = [] # List of movies in one Language
			self.fileName = fileName # Filename to write the list to.
		
		#Function crawls through the folders in Path1 and Path2. Appends all the movie names to a common list
		def ScrapeMoviesFromDirectories(self, Path1, Path2):
			#Scraping the Primary path
			for movieName in os.listdir(Path1):
				self.movie.append(movieName)
				
			#Scraping the secondary path
			for movieName in os.listdir(Path2):
				self.movie.append(movieName)

		#Function to Create a file so that the list of movies can be written
		def CreateFile(self): # function called inside WriteListToFile()
			self.movieList = open(self.fileName, 'w')

		#Function writes all the data into the file that is created by CreateFile()
		def WriteListToFile(self):
			self.CreateFile()

			self.movieList.write('Date : ')
			self.movieList.write(LanguageClass.Date)
			self.movieList.write('\n')
			self.movieList.write('Time : ')
			self.movieList.write(LanguageClass.Time)
			self.movieList.write('\n')
			self.movieList.write('Count: ')
			self.movieList.write('{}'.format(len(self.movie)))
			self.movieList.write('\n\n\n')

			for movieName in self.movie:
				self.count = self.count + 1
				self.movieList.write('{}'.format(self.count)) # Indexing each movie
				self.movieList.write(')')
				self.movieList.write(movieName)
				self.movieList.write('\n')


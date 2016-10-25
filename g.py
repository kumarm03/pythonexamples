import json
import csv
from csv import *
#author:kumar
with open("C:\\Users\\kumar\\Desktop\\aug03json\\ab.txt", "r") as fobj:
    data = json.load(fobj)
		
		
	
with open("C:\\Users\\Kumar\\Documents\\test\\web.csv", "w+") as web:
    writer = csv.writer(web)
    count = 0

    for item in data:
				
					if count == 0:
							header = data.keys()
							writer.writerow(header)
							count += 1
						 
						 
					if count == 1:
							 writer.writerow(data.values())
							 break
					
		
web.close()
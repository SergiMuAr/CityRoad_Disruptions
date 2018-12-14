import csv
csvFile = open('TwitterResults/ClassNTI.csv', 'w')
csvWriter = csv.writer(csvFile)

# NETEJAR -&gt DE LES DADES.

with open('TwitterResults/searchTwNTI.csv') as f:
  reader = csv.reader(f)
  for row in reader:
        csvWriter.writerow([row[1]])
   
csvFile.close()
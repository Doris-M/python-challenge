import os
import csv

my_folder = os.path.dirname(os.path.abspath('Resources'))
csvpath = os.path.join(my_folder,"Resources",'election_data.csv')

# dictionary created to store the candidate as key and the total of votes as value
candidateList = {}

# variable created to count the total votes
total_votes = 0

# variable created for the winner name
thewinner =''

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     
     for row in csvreader:
         total_votes = total_votes + 1
         # if the candidate in the dictionary count.. 
         if row[2] in candidateList:
            candidateList[row[2]] = candidateList[row[2]] + 1
         # if it not.. 
         else: 
         # add the candidate to the dictionary and starts counting the first vote  
            candidateList[row[2]] = 1

# function that prints the name of the candidates, total votes in percentage, and total votes per each candidate
def print_pecentages():
    for candidate, total in  candidateList.items():
        print(candidate +': ' + '{:.3%}'.format(total/total_votes) + ' (' + str(total) + ')')     

# function that prints the name of the candidates, total votes in percentage, and total votes in a text file format
def print_pecentages_file(myfilename):
    for candidate, total in  candidateList.items():
        myfilename.write(candidate +': ' + '{:.3%}'.format(total/total_votes) + ' (' + str(total) + ')\n')    

# function that returns the candidate with the highest number of votes
def get_winner():
    winner = max(candidateList, key=candidateList.get)
    return(winner)

# function that print the ouput on the terminal and export a text file
def print_output():
    
    print('Election Results')
    print('----------------------------')
    print ('Total Votes: ', total_votes)
    print('----------------------------')
    print_pecentages()          
    print('----------------------------')   
    thewinner = get_winner()
    print('Winner: ', thewinner)
    print('----------------------------')     

    # output file
    # change the directory when the output file will be saved ( os.chdir('analysis') )
    os.chdir('analysis')
    myfile=open("election_results.txt",mode="w") 
    myfile.write('Election Results\n')
    myfile.write('----------------------------\n')
    myfile.write ('Total Votes: '+ str(total_votes) + '\n')
    myfile.write('----------------------------\n')
    print_pecentages_file(myfile)         
    myfile.write('----------------------------\n')   
    myfile.write('Winner: '+ str(thewinner) +'\n')
    myfile.write('----------------------------\n')     

    myfile.close()

print_output()




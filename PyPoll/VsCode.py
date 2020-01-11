import os
import csv
csvpath=os.path.join(os.getcwd(),'election_data.csv')
print(csvpath)

with open(csvpath,'r',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader=next(csvreader)

    sr=0
    winning_votes=0
   
    ra=[]
    rs={}
    
    
    for row in csvreader:
        sr=sr+1
        candidate_name=row[2]
        if candidate_name not in ra:
            ra.append(candidate_name)
            rs[candidate_name]=0
        rs[candidate_name]=rs[candidate_name]+1
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes:{sr}") 
      
    # print(rs)
    for i in rs:
        number_of_candidate_votes=rs.get(i)
        percentage_of_candidate_votes=round(float(number_of_candidate_votes)/float(sr)*100,2)
        if winning_votes<number_of_candidate_votes:
            winning_votes=number_of_candidate_votes
            candidate=i
        num_votes=(rs[i])
        print(f"{i}: {percentage_of_candidate_votes}% ({num_votes})")
    print("-----------------------")
    print(f"Winner:{candidate}")
    print("-----------------------")




    output_file = os.path.join("election_data_text.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    datafile.write("Election Results\n")
    datafile.write("-----------------------\n")
    datafile.write("Total Votes:"+ str(sr)+"\n")
    for i in rs:
        number_of_candidate_votes=rs.get(i)
        percentage_of_candidate_votes=round(float(number_of_candidate_votes)/float(sr)*100,2)
        datafile.write(str(i)+":"+str(percentage_of_candidate_votes)+"%" +" " +"("+str(number_of_candidate_votes)+")"+"\n")
    datafile.write("Winner:"+str(candidate)+"\n")
    datafile.write("-----------------------") 
        # print(f"Election Results")
        # print("------------------------")
        # print(f"Total Votes: {sr}")
    # print (f"{percentage_of_candidate_votes}")
    # print(f"{candidate}")





        # names=row[2]   
        # if row[0]!=' ':
        #         sr=sr+1
        #         start_rw=str(start_rw)+row[2]
                
        # print(set(start_rw))


           



    # ra.append(sr)
    # rs.append(names)
    # length_list=sr
    # print(length_list)
            
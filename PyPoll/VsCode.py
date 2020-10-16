
import os
import csv

# finds election_data csv and creates a path for it

CSVPATH = os.path.join(os.getcwd(), 'Resources', 'election_data.csv')
print(CSVPATH)

# Puts the script into a function


def main():
    total_votes = 0
    winning_votes = 0
    candidate_list = []
    candidate_info_dict = {}

    # opens the csv and parses the csv
    # by comma

    with open(CSVPATH, 'r', newline='') as csvfile:
        CSVREADER = csv.reader(csvfile, delimiter=',')

        # loops through every row in csv

        for row in CSVREADER:

            # counts every row to get total number
            # of votes

            total_votes = total_votes+1

#            loops through third column to get each candidate

            candidate_name = row[2]

            # appends each unique candidate
            # to candidate_list

            if candidate_name not in candidate_list:
                candidate_list.append(candidate_name)

                # starts out by setting each candidate
                # equal to zero

                candidate_info_dict[candidate_name] = 0

                # for each time candidate name appears, add one
                # to the value pair

            candidate_info_dict[candidate_name] = candidate_info_dict[candidate_name]+1

            # loops through each key, value pair in candidate
            # dict

        for i in candidate_info_dict:

            # writes data to election_data_text.txt
                
            output_file = os.path.join("election_data_text.txt")
            with open(output_file, "w") as datafile:
                datafile.write("Election Results\n")
                datafile.write("-----------------------\n")
                datafile.write("Total Votes:" + str(total_votes)+"\n")

                # gets each value from each candidate
                # which is number of candidate votes

                number_of_candidate_votes = candidate_info_dict.get(i)

                # gets the percentage of candidate votes
                # per candidate

                percentage_of_candidate_votes = round(float(number_of_candidate_votes)/float(total_votes)*100, 2)
                datafile.write(str(i)+":"+str(percentage_of_candidate_votes)+"%" + " " + "("+str(number_of_candidate_votes)+")"+"\n")

                # if winning votes=number_of_candidate_votes
                # then we have the winner

                if winning_votes < number_of_candidate_votes:
                    winning_votes = number_of_candidate_votes
                    candidate = i
                 datafile.write("Winner:"+str(candidate)+"\n")
                 datafile.write("-----------------------") 

# calls the function

if __name__ == "__main__":
    main()      
<h2> <p align=center> Election Analysis </p></h2>

<h3><p align=center>Overview & Purpose of Election Audit: </p></h3>

A Colorado Board of Elections employee has assigned tasks listed below to complete the election audit of a recent congressional election. The following tasks form the ground of the entire analysis:

  1. Calculate the total number of votes cast.
  2. The voter turnout for each county
  3. The percentage of votes from each county out of the total count
  4. The county with the highest turnout
  5. Get a complete list of candidates who received votes.
  6. Calculate the total number of votes each candidate received.
  7. Calculate the percentage of votes each candidate won.
  8. Determine the winner of the election based on popular vote.

### Resources:
- Data Source: election_results.csv
- Software : Python 3.8.8, Visual Studio Code 1.60.0 


<h3><p align=center> Challenge Overview: <p></h3>
In this section, the code used to get the results of the election audit is discussed in detail. 
The dataset election_results.csv contained the entire voting data in 369,711 rows and 3 columns containing Ballot ID, County name and Candidate name.
The county wise counting and percentage calculations as well as candidate specific percentages and counting was achieved using only one **for loop**.
As the for loop iterated through all the voting data, row by row, the following algorithm was implemented:
  1. The total number of  votes required for the percentage calculations were tracked using **total_votes** variable.
  2. Conditional statement (if statement) was used inside the for loop, to create a list of unique candidates, which in turn was used to keep track of votes of respective candidates in a **candidate_votes{}** dictionary.
  3. Similarly, a second if statement was used to make a list of unique county names, which was then used to make **county_votes{}** dictionary holding county names and corresponding county votes.
  4. Using to this algorithm, by the end of all iterations of the for loop, we ended up with:
      - **Total number of votes**
      - **candidate_votes{} dictionary** with **unique candidate names** and **corresponding vote count**
      - **county_votes{} dictionary** with **unique county names** and **their corresponding vote count**

**<p align=center>A sneak peak into the code:</p>**

<pre>

<b> The main algorithm used to acquire relevant data for the present analysis</b>

   # For iterrating through each row in the dataset
   <b>for row in file_reader:</b>

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
  <b>   if candidate_name not in candidate_options: </b>

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
 <b>    if county_name not in county_options: </b>

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
        
        </pre>
      
  5. Once all the relevant data was acquired in one variable and two dictionaries, further analysis became simple.
      - The data from county_votes dictionary was extracted and printed to a text file using a for loop. The county percentages were also calculated during this phase and printed to the text file.
      - Similarly, data from candidate_votes dictionary was extracted using for loop and percentages were also calculated and added to the same text file.
      - Furthermore, the county with highest vote turnout and the winning candidate were decided within respective for loops using if conditional statements.
      
<b><p align=center> Example code for county votes calculations can be referred to in the code block below:</p> </b>
 
 <pre>
 
 # 6a: Write a for loop to get the county from the county dictionary.
 <b>for county_name in county_votes:</b>

        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
  <b>   county_vote_percentage =  float(county_vote_count)/float(total_votes)*100 </b>

        # 6d: Print the county results to the terminal.
        county_results = (
             f"{county_name}: {county_vote_percentage:.1f}%, ({county_votes[county_name]:,})\n"             
             )
        print(county_results, end="")   

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
   <b>  if (county_vote_count>largest_voter_turnout):  </b>
            largest_voter_turnout = county_vote_count
            largest_vote_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout_result = (f"\n-------------------------\n"
             f"Largest County Turnout: {largest_vote_county}\n"
             f"-------------------------\n")
    print(largest_turnout_result)

    # 8: Save the county with the largest turnout to a text file.
<b> txt_file.write(largest_turnout_result) </b>
 
 </pre>
 

<h2><p align=center> Election Audit Results: </h2> </p>

<p align=center> The results of the Election Audit analysis, as printed by above script in a text file are attached below: </p>

<p align=center> <img width="320" alt="Screen Shot 2021-11-09 at 11 25 49 PM" src="https://user-images.githubusercontent.com/90424752/141069345-36eb7b01-ed50-4ea0-b8c0-8de655a5ba48.png"> </p>


  * There were total 369,711 votes cast in the election.
  * The County Votes were:
    * Jefferson County was responsible for 10.5% and 38,855 number of votes.
    * Denver County was responsible for 82.8% and 306,055 number of votes.
    * Arapahoe County was responsible for 6.7% and 24,801 number of votes.
  * The County with the largest voter turnout was Denver with 82.8% and 306,055 number of the total votes.
  * The candidates were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
  * The candidate results were:
    * Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
    * Diana DeGette received 73.8% of the votes and 272,892 number of votes.
    * Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
  * The winner of the election based on popular votes was:
    * Candidate Diana DeGette who received 73.8% of the votes and 272,892 number of votes.
    
<h3><p align=center> Election Audit Summary:</p></h3>
The Python script used for this analysis can be used for all election audits with the same analysis requirements and similar datasets of even bigger sizes. In addition to that the script can be very easily modified to also accommodate following scenarios:
  1. If the dataset contains zipcodes instead of counties, county variables, lists and dictionaries could be changed accordingly. The data type for zipcode can be string to accommodate any aplha-numeric zipcodes.
  2. If there are two or more candidates with the same name, each candidate can be given a unique ID. The unique ID should be used to keep track of votes for the different candidates instead of candidate names.
  3. The present script can also be used to get the state wise election audit results, needing only to change county variables,lists and dictionary to state variables, lists and dictionary. 

<h2> <p align=center> Election Analysis </p></h2>

### Overview & Purpose of Election Audit: 

A Colorado Board of Elections employee has assigned tasks listed below to complete the election audit of a recent congressional election. The following tasks form the ground for the present analysis:

  1. Calculate the total number of votes cast.
  2. The voter turnout for each county
  3. The percentage of votes from each county out of the total count
  4. The county with the highest turnout
  5. Get a complete list of candidates who received votes.
  6. Calculate the total number of votes each candidate received.
  7. Calculate the percentage of votes each candidate won.
  8. Determine the winner of the election based on popular vote.

The Python code used for the election audit is discussed in detail in challenge overview section. Election audit results are then presented in the next section, followed by some comments and suggestions about the reusability of this Python script in different scenarios.

### Resources:
- Data Source: election_results.csv
- Software : Python 3.8.8, Visual Studio Code 1.60.0


### Challenge Overview:
In this section, the code used for the election audit is discussed in detail. 
The dataset election_results.csv cotanined the entire voting data in 369,711 rows and 3 columns. The three columns held the information about Ballot ID, County name and Candidate name.
To calculate county and candidate related percentages and votes, we go through the entire dataset once, using a **for loop**. The following two dictionaries are used to keep track of the data:
  - **candidate_votes{}**
    - This dictionary keeps track of unique candidates and their corresponding votes.
    - This dictionary uses candidate_name as a key and stores corresponding votes as thier values.
  - **county_votes{}**
    - This dictionary keeps track of unique county names and each counties vote count.
    - This dictionary uses county_name as keys to store each county's votes as it's values.

As the for loop iterates through all the voting data, row by row, the following algorithm is implemented:

  1. The total number of votes required for the percentage calculations are tracked using **total_votes** variable.
  2. Inside the for loop, a conditional if statement creates a list of unique candidates. Here, if a candidate_name is encountered for the first time, it is added to the **candidate_votes{}** dictionary as a key and corresponding **value** is **set to 0**. In the next step, **1 is added as it's value** for the vote count. For **each repeating instance** of the candidate name, the **corresponding value** for respective candidate in candidate_votes{} dictionary is **increased by 1**.
  
<pre>

<b>if candidate_name not in candidate_options: </b>

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
     <b>candidate_votes[candidate_name] += 1 </b>

</pre>

  3. Similarly, a second if statement makes list of unique county names and then tracks county wise votes in **county_votes{}** dictionary. 
  4. Using to this algorithm, by the end of all iterations of the for loop, we get:
      - **Total number of votes**
      - **candidate_votes{}** dictionary with **candidate names** and **corresponding vote count**
      - **county_votes{}** dictionary with unique **county names** and **their corresponding vote count**

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
      
  5. After all the relevant data is acquired in one variable (total_votes) and two dictionaries (county_votes{} & candidate_votes{}), the next steps are:
      - **Extract** **data** from **county_votes** **dictionary** and printed it to a text file using a for loop. The county percentages are also calculated during this phase and printed to the text file.
      - Similarly, data from candidate_votes dictionary is extracted using for loop and percentages are also calculated and added to the same text file.
      - Furthermore, the **county** **with** **highest** **vote** turnout and the **winning** **candidate** are decided within respective for loops while iterating through dictionaries, using **if** **conditional** **statements**.
      
      
<b><p align=center> Example code for the county votes calculations can be referred to in the code block below:</p> </b>
 
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
 

### Election Audit Results:

After running the script discussed above, the election results are printed to the terminal and also printed to a text file generated during the analysis. The screenshot of the results displayed on the terminal is attached here:

<img width="320" alt="Screen Shot 2021-11-09 at 11 25 49 PM" src="https://user-images.githubusercontent.com/90424752/141069345-36eb7b01-ed50-4ea0-b8c0-8de655a5ba48.png">

The Outcomes of Congressional Elections are stated below:

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
  * The camdidate results were:
    * Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
    * Diana DeGette received 73.8% of the votes and 272,892 number of votes.
    * Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
  * The winner of the election based on popular votes was:
    * Candidate Diana DeGette who received 73.8% of the votes and 272,892 number of votes.
    
### Election Audit Summary:
The Python script used for this analysis can be used for all election audits with the same analysis requirements and similar datasets of even bigger sizes. In addition to that, the script can be easily modified to accommodate following scenarios:
  1. If the dataset contains zipcodes instead of counties and if we need the zipcode wise calculations, the county variables, lists and dictionaries could be changed accordingly to hold zipcodes instead of county names. The data type for zipcode can be string to accommodate any aplha-numeric zipcodes.
  2. If there are two or more candidates with the same name, each candidate can be given a unique ID. The unique ID should be used to keep track of votes for the different candidates instead of candidate names. Candidate_name will be replaced by candidate_id in this scenario.
  3. The present script can also be used to get the state wise election audit results, needing only to replace county data by state data.


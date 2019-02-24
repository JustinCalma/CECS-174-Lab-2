#Get Data from the user
player_Name = input("Enter the player's name: ")
plate_Appearances = int(input("Enter the number of Plate Appearances: "))
at_Bats = int(input("Enter the number of At Bats: "))
walks = int(input("Enter the number of walks: "))
singles = int(input("Enter the number of singles: "))
doubles = int(input("Enter the number of doubles: "))
triples = int(input("Enter the number of triples: "))
home_Runs = int(input("Enter the number of home runs: "))

#Calculate the Total Hits
total_Hits = singles + doubles + triples + home_Runs
print("The total number of hits are: ", total_Hits)

#Calculate the Batting Average
batting_Average = total_Hits / at_Bats
print("The batting Average is:" , "{0:.3f}".format(batting_Average))

#Calculate the SLugging Percentage
slugging_Percentage = ((1 * singles) + (2 * doubles) + (3 * triples) + (4 * home_Runs)) / at_Bats
print("The Slugging Percentage is:" , "{0:.3f}".format(slugging_Percentage))

#Calculate the OBP and OPS
OBP = (total_Hits + walks) / plate_Appearances
OPS = OBP + slugging_Percentage
print("The On-base Plus Slugging is:" , "{0:.3f}".format(OPS))

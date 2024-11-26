Machine Learning w/ Basketball Stats
Kaleb Hannan
11-25-2024
HW5
Classwork for COS 470 at the Univerisy of Maine Orono

# Discription:  


# Dependencies:
python 3
pytourch
pandas
sklearn

# How to Run the Program:
python3 COS470HW5.py

# Approch
When first workin I started by Using pandas to load the data from the csv into a data frame so
that I could work with the data.  After loading the data into the program using pandas I split the
num of game won from the rest of the data.  Then acter getting the main data saperate from the num 
of games won I normilized the data so that all of the values would be between 0 and 1 so that not 
one field had more influance then the others.

For the data that I used to make a perdictoin I used all of the data but the 'Wins' witch i used as a lable the 'year'
and the 'team name' witch will not hold any value when making a perdiction.

After normilizing the data I started by createing my neural network with 3 liner layers using the nn.Sequential()
function to create a liner relu stack.  The first layer talks in all of the inputs 
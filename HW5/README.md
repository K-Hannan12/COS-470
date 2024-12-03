Machine Learning w/ Basketball Stats
Kaleb Hannan
11-25-2024
HW5
Classwork for COS 470 at the Univerisy of Maine Orono

# Discription:  
This program is a Machine Learning model that perdicts the number of wins that a Basketball team will get
based on there season statistics 

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
num of game won from the rest of the data.  Then after getting the main data saperate from the num 
of games won I normilized the data so that all of the values would be between 0 and 1 so that not 
one field had more influance then the others.

To split the data by percentage I used the sklean library and split the data into 85% traning 15% test.

For the data that I used to make a perdiction I used all of the data but the 'Wins' witch i used as a tagate, the 'year'
and the 'team name' whitch will not hold any value when making a perdiction.

After normilizing the data I started by createing my neural network with 3 liner layers using the nn.Sequential()
function to create a liner relu stack.  The first layer talks in all of the inputs and outputs 64 then the second layer 
takes 64 nutrons and outputs 32 then the 3rd layer takes 32 and retuns 16 then the 4th layer takes the 16 and 
then returns 1 value that represents the number of wins that the Model thinks the team got based on the stats given.

The loss functional that I used to train the model was Mean Squeared error.  I used it to see how far away my perdiction
was from the actual number of wins. 

I also used the SGD optmization function.

I first started by training with 100 epocs using this model I ended up with a loss of 32.96 when testing
when running the testing data against the model.

Next I tryed testing using 500 epochs at a learning rate of 0.001  

When testing with with the model trained with 500 epochs I got a test loss of 4.5929

After this I wanted to test and see what would happen when I changed the learning rate
and change it to 0.01.  When doing that it canged my loss from 4.5929 to 44.4561.
Then Next I changed the learning rate to 0.0001 to see if decressed my loss.  
When doing that I got a testing loss of 42.5763.


Then next I tried traning the model with 1000 epohcs to see if I can get the model to
be more acurate.  Traning the model with 1000 epohcs my loss was 4.0720.  But when 
looking at the epoch 750 the loss started to go back up.  So i tryed traning with 750
and got a test loss of 3.9790.

Then I when back and tryed the slower learning rate so I used 10,000 epochs at a learning rate of 0.0001 
and I was able to get a test loss of 3.8036

After this I wanted to test and see how my resalts would differ when using data that is split by year.
To do this I took the stats from 2010 and 2015 and used that test data and used the rest as traning data.


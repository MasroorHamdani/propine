# Question 1 - Design/Writing
In this question, we're looking at how you approach problem solving, and how clearly you convey your ideas. An effective engineer not only build things that work, a large part of their time is spent communicating how that worked and helping others.

Imagine you're working in an elevator company and you are asked to improve the elevator experience. Existing elevators find the shortest path to serve the passenger given a button input. It hasn't changed for more than 50 years. Now with advancement in technology, we have cameras at every level telling us how many people are waiting, how long each person have waited, and how many people are already in the lift. Describe how you would design a solution to best serve the passengers with the assumption you have limited resources and time. No code needed.

# ************
Current system in elevator uses shortest path algorithm. In order to solve the user experience problem we consider the following assumptions/facts:
There can be cases where people ended up waiting for a longer duration.
We have count of people inside lift at any given time
We have count of people waiting at each floor and  their individual waiting time

There can't be a perfect solution. In order to verify the solution given below, we need to run some simulations.
Keeping simulations aside (stochastic traffic control systems), we write down the solution in pure readable form.
Lift will use its usual algorithm with a small change. We hard define some base rules/parameters to start with :
At any given point when call button is pressed from multiple floors, the algorithm will get the total number of people inside the
lift and the total number of people waiting for lift along with the wait time of the first person.
 In case lift is completely occupied, it won't stop anywhere in between, it will directly go to end point. Lift will stop only if it has
some intake capacity.
If the lift has some empty space, then it will go in direction where people wait time is more.
Logic encoding - Priority order :
1. Person A on floor 7 press the call button. We have 2 person waiting at 7th floor for 10 mins.
2. Person B on floor 3 also press the call button at the same time. There we have 1 person waiting for 5 mins.
3. Lift will move towards 7th floor, pick people from there, then move towards 3rd floor.

Logic encoding - Priority Direction :
1. Person A on 7th floor press the call button. We have 2 people waiting at 7th floor for 10 mins and they have to go down the building.
2. Person B on 3rd floor press the call button at the same time. There is 1 person with wait time of 5 mins and has to go up.
3. Lift will first come to 7th floor, pick people and move down to their destinations. Once the lift is free it will then move toward the 3rd floor.

Normal scenarios, there are more than one lift:
1. Person A on 7th floor press the call button. We have 2 people waiting at 7th floor for 10 mins and they have to go down the building.
2. Person B on 3rd floor press the call button at the same time. There is 1 person with wait time of 5 mins and has to go up.
3. If any lift is on the way down, that will stop by 7th floor and pick people from there and move down and other lift will serve 3rd floor people to take them up.
4. In case both the lifts are in rest state, one of the lift will move towards the 7th floor and other will move towards the 3rd floor to serve people.

Given these fundamental modes, the elevator algorithm takes a call to improve the user experience.
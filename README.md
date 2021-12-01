# Lab 5

**Released on** Tuesday, November 30    
**Due on** Wednesday, December 1 (1 Day)   

**Modules Covered:** 1 - 11  

## Preparation Steps:

-	Watch all modules
-	Watch: https://www.youtube.com/watch?v=a7JCrbRr54w
-	Prepare extra time with partner if needed

## Pair Programming:

In order to perform pair programming in the online setting, you should set up a call with your partner (or group of three) during the lab time. One team member will share their screen and program while the other partner (or 2 partners) will give advice. You should switch programming every 10-15 minutes. One group member should not be doing all the programming here. Every partner will be responsible for submitting their own copy of the code.

## Submission: 

Each partner should submit their own code by pushing the code on GitHub. Make sure that every submitted file has a comment at the top with all group members’ names and student numbers. 

## Additional: 

Only use the programming skills that you have learned in modules for this assignment. While there sometimes may exist solutions that are “better” through using other skills, we ask that you only use what you have been taught in the modules up to this point. We must make sure that you understand the taught material for full marks. 
 
## Exercise for Submission:

As the final lab of this term, your job is to help keep track of how long various items take to blend in a blender and show them graphically in the graphs listed below. For this lab, some of the code has already been written and it is your job to add to that code. You must not change any of the code provided unless stated. 

Comments have been provided to help you find what code you need to change. You need to add code in where you will see ```# TODO X``` where X is a number 1-5. You should complete the TODO's in order.

### Part 1:

Read the code provided and make sure you understand what it is doing. After you are comfortable with it, start by finishing TODO 1, which involves reading in all the items from a csv file and storing them into a dictionary. ```items.csv``` stores the name of an item, three coefficients, and a constant. The constant represents the size of the item before it goes into the blender. A formula can be found below to calculate the size of an object given a time. When the size of pieces in the blender <= 0, the blender stops as it is considered blended fully.
 
![image](https://user-images.githubusercontent.com/77299347/122938062-d46dbe00-d348-11eb-99b1-adb777552eff.png)

### Part 2:

After reading in from the file, the program should calculate how long each item takes to blend entirely (TODO 2). You need to store the x (time) and y (size of pieces) values for each curve. If the piece size goes below zero, set it back to 0. It is your job to choose a step value that makes a smooth line graph in Part 3 but that also does not take too long to calculate.

After completing Parts 1 and 2 (i.e., after you have finished TODO 1 and 2), you should be able to run the program. Choices 2 and 5 will work after Part 2 has been completed (you can see a description of the different choices below).

### Part 3:

The program will now enter a loop where the user will be asked to choose one of six options by inputting a number between 1 and 6. For these all to work, you will need to complete TODOs 3-5, so that the choice 1 (TODO 3), choice 3 (TODO 4), and choice 4 (TODO 5) work.  

#### 1: Search Item’s Blend Time

The user inputs the name of an item, and the system should output the time it takes for this item to blend. The search is case-sensitive. If the item does not exist, inform the user that it is not in the database. - **TODO 3**

![Failed Search for iPhone](https://user-images.githubusercontent.com/1709150/143963454-3e97aa86-4271-4c6e-adca-98c6f750c779.png)
![Successful Search for iPhone](https://user-images.githubusercontent.com/1709150/143963513-a8199775-2386-4080-a58a-d8303936dc44.png)


#### 2: Longest Blend Time

The system should output the name of the item that takes the longest time to blend and the length of time it takes to blend entirely. – **Completed already.**

![Longest Blend Time](https://user-images.githubusercontent.com/1709150/143963688-b28aa4af-5b78-4612-9f95-1fa746936474.png)


#### 3: Shortest Blend Time

The system should output the name of the item that takes the shortest time to blend and the length of time it takes to blend entirely. To complete this one you can coy Choice 2 and adjust for the shortest blend time. - **TODO 4**

![Shortest Blend Time](https://user-images.githubusercontent.com/1709150/143963743-af104973-177e-4c3a-bd52-80236602f5a9.png)

#### 4: Compare Blend Times

The user will input 3 names of items followed by 3 colours. You must then show a line graph that uses the x and y values you calculated in Part 2 and has the following requirements: a title, x- and y-axis labelled, 3 lines (1 for each item), and a legend labelled with the names of items. The lines must each be coloured correctly and each one should have a unique marker.  - **TODO 5**

![Comparison Chart Setup](https://user-images.githubusercontent.com/1709150/143964551-b5deedfd-63b2-4d7b-9fe3-52ef5b27cd79.png)
![Comparison Chart](https://user-images.githubusercontent.com/1709150/143964510-13ef802b-7141-46c6-85b3-d348fc51cbe8.png)

#### 5: Percentage of Blend Times

The user will input a time and the system shows a pie chart that shows the percentage of items that took <= the time given to blend and the items that took > the time given to blend. This graph should have one pie slice blue and one pie slice red. The pie chart needs to have a title, a legend that is labelled properly should be shown, and the percentages on each piece. The <= time given should be slightly exploded from the rest of the graph. - **Complete already**

![Pie Chart Setup](https://user-images.githubusercontent.com/1709150/143964318-2064529a-afc0-4153-99bd-a428a906e71b.png)
![Pie Chart](https://user-images.githubusercontent.com/1709150/143964247-f57f26a9-d85b-4269-82a2-0304e5a1d5ca.png)

#### 6: Exit

The program stops running.

![Quitting](https://user-images.githubusercontent.com/1709150/143964638-a49d03ed-4b43-4af0-93c3-0e525122b8b3.png)
 
_Note: Make sure to exit your graph before trying to display another one!_

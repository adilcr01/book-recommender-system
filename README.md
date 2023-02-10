
# Book Recommendation using Machine learning

Recommender System is a system that seeks to predict or filter preferences
according to the user’s choices. Recommender systems are utilized in a variety
of areas including movies, music, news, books, research articles, search queries,
social tags, and products in general. 
Recommender systems produce a list of recommendations in any of the two ways – 
 

#### Collaborative filtering: 

    Collaborative filtering approaches build a model from the user’s past behavior
    (i.e. items purchased or searched by the user) as well as similar decisions 
    made by other users. This model is then used to predict items (or ratings for
    items) that users may have an interest in.

#### Content-based filtering:

    Content-based filtering approaches uses a series of discrete characteristics 
    of an item in order to recommend additional items with similar properties. 
    Content-based filtering methods are totally based on a description of the 
    item and a profile of the user’s preferences. It recommends items based on 
    the user’s past preferences.


## Project Explanation

In this project we are using a Collaborative filtering approach for book recommendation.
This type of recommendation systems, takes in a book that a user currently likes 
as input and compare it with books liked by other users having same behaviour/preference. This model is 
then used to predict books that users may have an interest in.
The idea behind it is that similar users will have similar preferences and that 
users have a tendency to like items that are similar to each another.


#### Nearest Neighbour Based Recommendation

To train the Nearest Neighbours model, we have created a compressed sparse row 
matrix taking ratings of each Book by each User individually. This matrix is 
used to train the Nearest Neighbours model and then to find n nearest neighbors 
using brute algorithm in NearestNeighbors.

###### brute algorithm:  We instruct the algo to calculate distance of all the points and then decide neighbors

## Dataset used

Book Recommeder Dataset 
https://www.kaggle.com/arashnic/book-recommendation-dataset
## Screenshot

#### home page

![book recommender 1](https://user-images.githubusercontent.com/93968656/141471168-e5f0aff8-4b47-4bcf-be99-10676a34629a.png)


![book recommender 2](https://user-images.githubusercontent.com/93968656/141471191-61d3ea4d-f4a0-4434-a1f6-04a445952e2f.png)

#### Recomendation page
![book recommender 3](https://user-images.githubusercontent.com/93968656/141471209-880b8106-4207-463f-81cf-8169093305a7.png)


## Tech Stacks

#### Programming Language : Python

#### WebFramework: Steamlit

#### Machine Learning Library: Numpy, Pandas, sklearn

## Deployement on Heroku

##### Login or signup in order to create virtual app. You can either connect your github profile or download Heroku cli to manually deploy this project.

![image](https://user-images.githubusercontent.com/93968656/141473301-75af8d20-2cef-4b1e-ab60-3b61c82de37d.png)

##### The next step would be to follow the instruction given in the Heroku Documentation to deploy a web app.

## How to run the project on local system?

   ##### 1. Clone this repository in your local system.
   ##### 2. Open your IDE from your project directory and Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt.
   ##### 3. Type command "streamlit run app.py" in the terminal to run the app.
   ##### 4. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
   ##### Hurray! That's it.


## Link to the application 

Check out the live demo: 
https://book-recommender1.herokuapp.com/

##### Note: You might expect problem in Safari and Chrome Browser. Use Firefox instead. 

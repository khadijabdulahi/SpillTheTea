![Screen Shot 2021-12-03 at 3 45 04 PM](https://user-images.githubusercontent.com/91164157/144683358-a3e9b50c-c7f8-42b7-9b8f-bba9e5dd5112.png)

## Table of Contents 
* [Overview](#overview)
* [About me](#about-me)
* [Tech Stack](#tech-stack)
* [Roadmap](#roadmap)
* [Features](#features)
* [Installation](#installation)
* Future Iterations(#future)

## <a name="overview"></a>Overview 

Spill the Tea! is a full-stack web application that allows users to learn about different types of teas. Users can go to each tea page and learn about the tea and its benefit. Users are also able to search by zipcode for the 12 closest tea cafes near them. User's can also have a tea recommended to them by taking our quiz. Users with registered accounts can favorite teas and have their favorite teas saved between sessions. 

## <a name="about-me"></a>About Me 
Learn more about Khadija Abdulahi on [LinkedIn](https://www.linkedin.com/in/khadijaabdulahi/).

## <a name="tech-stack"></a>Tech Stack 

**Backend**:  Flask, PostgreSQL, Python, SQLAlchemy <br/>
**Frontend**:  AJAX, Bootstrap, CSS, HTML, Jinja2, JavaScript, jQuery <br/>
**APIs**:  Yelp, Mapbox, Quote Generator 

## <a name="roadmap"></a>Roadmap

#### MVP :

- User's can register for an account
- User's can login to an account that exist 
- Users can view a list of teas and details about each tea along with their image
- Dropdown bar where users can search for teas 
- Map where user's can search for tea locations near them 

#### 2.0  : 

- Users can favorite teas
- Users can take a quiz to get a tea recommended to them
- User's can search for cafe location near them by entering zipcode
- User's can get directions to the cafe 
- User's can get different inspirational quotes by clicking on a button. 


## <a name="features"></a>Features
Insipirational Quote: <br>
![Hnet-image (5)](https://user-images.githubusercontent.com/91164157/144726588-393f233e-2a08-4835-81e3-4ddcca1a8f26.gif) <br>
Quiz: <br>
![Hnet-image](https://user-images.githubusercontent.com/91164157/144725920-604db10f-da5c-4c98-a185-1bce5956805a.gif) <br>
Favorite: <br>
![Hnet-image (1)](https://user-images.githubusercontent.com/91164157/144726221-c3605a13-4d52-4d46-9654-be63f49f1d34.gif) <br>
![Hnet com-image (1)](https://user-images.githubusercontent.com/91164157/144726798-d829bc26-3481-4e59-b3ca-c0b75f929cba.gif) <br>
Search for Cafe: <br>
![Hnet-image (3)](https://user-images.githubusercontent.com/91164157/144726380-53936e31-b629-47ac-99bb-6ebb4e7f773a.gif) <br> 
Get direction to Cafe: <br>
![Hnet-image (4)](https://user-images.githubusercontent.com/91164157/144726477-201895bd-1308-4feb-b6ab-05ff47f7e1f0.gif)<br>

## <a name="installation"></a>Installation 

### Requirements

* PostgreSQL
* Python 3

If you would like to run this app locally on your own computer, follow the below steps. 

first clone this repository:
```
$ git clone https://github.com/khadijabdulahi/SpillTheTea.git
```
Create and activate a virtual environment:
```
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
(env) $ pip3 install -r requirements.txt
```
Create a secrets.sh file and save your secret key for this app using the following syntax:
```
export yelp_token='***'
export mapbox_token='***'
```
Activate the secrets.sh file in your terminal:
```
(env) $ source secrets.sh
```
Create the database:
```
(env) $ createdb teas
```
Seed the database:
```
(env) $ python3 model.py
(env) $ python3 seed.py
```
Start the backend server:
```
(env) $ python3 server.py
```
Open your browser and type: localhost:5000 to view locally.

## <a name="future"></a>Future Iterations 
- Users able to favorite cafes to save to their favorites page. 
- Users able to upload profile photo, favorite quote and favorite tea to personal profile page. 
- Users able to leave review and ratings for each tea. 
- Adding more teas to the database



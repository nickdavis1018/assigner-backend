# Welcome to Assigner!

Looking for Frontend? Check out the <a href="https://github.com/nickdavis1018/assigner_frontend">Frontend Repo</a>.

Looking for Trello? Check out the <a href="https://trello.com/b/HFioMszG/assigner/">Assigner Trello</a>.

Looking for Heroku? Check out the <a href="https://dashboard.heroku.com/apps/assigner-database/">Assigner Database</a>.

Want to check out the site? Check out <a href="https://assigner.netlify.app/">Assigner</a>!

## Mission

Create a back-end application capable of authenticating users and allow access to an Assignments API, allowing Manager Roles full CRUD functionality. The primary goal of the this project was to teach myself Python / Django and implement basic SimpleJWT authentication.

Want more detail about how it functions? Check out the <a href="https://github.com/nickdavis1018/assigner_frontend">Frontend Repo</a>.

## Technologies Used 

- Python 
- Django
- SimpleJWT
- Postgresql
- Github
- Heroku (back-end)
- Netlify (front-end)

## MVP / Achieved Targets

- Allow full CRUD functionality
- Create User Authentication / Authorization
- Setup Customer Registration Serialized
- Utilized Multiple Models

## Original ERD

<img src="https://imgur.com/cZyqo4kpng.png"/>

## Wireframes

Original Dashboard View<br/>
<img src="https://imgur.com/aD5Mdyy.png"/>

## Stretch Goals

- Add Date Model for Assignment tracking
- Properly implement Group Permissions (current authorization method relies on "is_staff" status and is not best practice)
- Increase security and transition away from SimpleJWT

## Site Info

The Assigner site can be logged into from the home page (required):

<img src="https://imgur.com/9UJS8FU.png"/>

Users can utilize the Search bar to browse events and filter assignments by active status and assignment:

<img src="https://imgur.com/Z0UweME.png"/>

Managers have access to a Management Dashboard to view user performance:

<img src="https://imgur.com/YTYxyQo.png"/>

Managers can access Manage sections and Create + Edit files from there:

<img src="https://imgur.com/eAVsaaT.png"/>

## Code Snippets

Migrations / Model<br/>
<img src="https://imgur.com/88YmRpY.png"/>
<img src="https://imgur.com/xeqbxIq.png"/>

Serializers<br/>
<img src="https://imgur.com/HscxUOl.png"/>
<img src="https://imgur.com/Pg98XqO.png"/>

Routes<br/>
<img src="https://imgur.com/jGUORQx.png"/>
<img src="https://imgur.com/3BGq0wO.png"/>

Views<br/>
<img src="https://imgur.com/89F8PNN.png"/>
<img src="https://imgur.com/urB2GnX.png"/>

Nick Davis<br>
Development Lead<br>
<a href="https://github.com/nickdavis1018">Nick's Github</a>

<style>
    img{
        width: 200px;
        height: 200px;
        text-align: center;
    }
</style>
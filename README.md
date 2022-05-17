# SCUSS

This is a discussion forum, open for all with a motive to connect and share various topics through blog posts! As soon as a user registers an account they can create their own posts and interact with others by commenting and liking! Under the activity tab, the registered user can easily see all their created posts and all their previously liked posts. [Link to deplyed site.](https://blog-vt-21.herokuapp.com/)


## TABLE OF CONTENTS
1. [FEATURES](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)

2. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
      - [User Experience](#user-experience)
      - [Fonts](#fonts)
      - [Colors](#colors)

3. [DEPLOYMENT](#deployment)

4. [TESTING](#testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

5. [Credits](#credits)

## FEATURES

### Existing Features

- As the user firsts visit the page they can see all the posts and all comments but need to create an account to be able to write their own comments and posts. In the navigation bar at the top of the page, there is a link to registration. In the registration form, the user can set their username, full name, email address, and password. After creating an account the user is redirected to the home page where they have access to all functionality via the navigation bar.

- The user can at any time change any of the information that they saved as their profile. The user can also change their password via the same form.

- When the user is logged in they can easily create a post with a title and content. All posts will display both the author as username and the date and time it was created on.

- In the home view the posts are displayed as a list with the title and the first 200 characters of the content, if a user is particularly interested in a post they can click on the post title and they will be able to see all the post and the associated details as the number of likes and comments. The user can delete and update all of their posts.

- If the user is logged in they can like and unlike posts as well as comment on all posts and also delete their comments. The user has the ability to delete all comments on their own posts so that they are able to control the post's details. 

- Under the tab ‘My activity’ the user can see a list of all the posts that they have created. they can also see a list of all the posts that they liked.


### Features to be implemented

- A view for user profiles to interact with other users
- Functionality to add a profile picture
- Functionality to add images to posts
- Functionality to edit a comment

## UX

### User Stories 

- As a site user, I can create an account so that I can interact with the content.
- As a site user, I can update my account so that I can handle my information.
- As a site user, I can create, update and delete posts so that I can manage my content.
- As a site user, I can view a list of posts so that I can get an overview of all the content.
- As a site user, I can view a paginated list of posts so that I can select posts to view.
- As a site user, I can click a post so that I can see more.
- As a site user, I can like and unlike a post so that I can interact with the content.
- As a site user, I can view the number of likes a post has gotten so that I can see which is the most popular.
- As a site user, I can add and delete comments so that I can interact with the content.
- As a site user, I can view the comments of a post so that I can follow the post conversation
- As a site user, I can navigate around the site so that I can use all functionality.
- As a site user, I can view a list of my posts so that I can get an overview of my activity.
- As a site user, I can view the posts that I have liked so that I can get an overview of my activity.


### Design Choices

**User Experience:**
All clickable links are underlined when hovered over, the logo will take the user back to the home page but will not display an underline, it is simply clickable because of the common subconscious habit to use the logo as a form of navigation. The home view and the activity view have the same layout to create a familiar pattern in design. All forms are made with the same mindset.

**Fonts:**
The main font of the site is Bebas Neue used on all text elements except the page logo which is in the Barlow font, both taken from [Google Fonts](https://fonts.google.com/). As a secondary font, I choose Sans-Serif.

**Colors:**
The colors of the page are a clear white and a light purple color (#ddbadd). For small details such as borders or links, I’ve chosen a darker purple (#520652) to make these elements stand out more. I have made these color choices to make the website look simplistic but colorful and welcoming.

## DEPLOYMENT
 
This Project was deployed with Heroku, in the article linked below, there is a clear description of the deployment process. 
- [Heroku Deployment](https://www.freecodecamp.org/news/how-to-deploy-an-application-to-heroku/)
The article is taken from the website [freecodecamp.org](https://www.freecodecamp.org/) and is written by Stan Georgian.

## TESTING

### Fixed Bugs
**Bug:** Application error when deploying on Heroku, Item could not be created due to the user being unuthorized.
- Solution: Deployment was successful when doing a remote deployment via the Gitpod terminal.
 
 
**Bug:** The CSS did not load on the deployed version of the site.
- Solution: Added ‘{% load static %}’ to the top of index.html, the file extending the other templates of the repository, to load the stylesheet.

### Unfixed Bugs
- no bugs remaining

## CREDITS
 
**Stan Georgian for freecodecamp.org**
- For the article on the Heroku deployment process


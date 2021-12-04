# Impasta

Heroku Link: https://sleepy-castle-35232.herokuapp.com/

# Project Overview

We are building building and deploy a web app that allows users to find menu contents and nutrition information on restaurants of their choice. The app will have a signup/login functionality for the security layer. Once users login, they will be redirected to the home page. Which will display restaurants near them using the Google Maps API. Additionally, the OpenMenu and Nutritionix APIs will allow users to see the menus of a selected restaurant and the nutrition facts of each item on the menu of the restaurant they chose from the list.

## Technologies Used (Frameworks, Libraries, APIs)

- Backend:
    - Flask
- Frontend:
    - React
    - JavaScript
- Backend/Frontend Integration:
    - JavaScript Fetch API
    - React Router
- APIs:
    - Google Maps API
    - OpenMenu API
    - Nutritionix API
- Deployment
    - Heroku

## Technical Issues
1. Git Pull Request Conflicts
    - With multiple people working on different branches, we had issues with merging our code and making sure it all worked together. We solved this issue by troubleshooting at every push and merge to avoid further complications.
2. Linting Files & Making Changes
    - Modifying files led to merge conflicts and interfered with linting, which we solved by commenting out the linting code and making sure everything else was working before fully incorporating linting.
3. Unit Testing Difficulties
    - Unit Testing was difficult to successfully deploy without running into errorw, which we solved by continuously debugging to ensure seamless testing. 

## Installation Guide
    - `git clone https://github.com/esala1/Impasta.git`
### Flask and `create-react-app`

### Requirements

1. `npm install`
2. `pip install -r requirements.txt`

### Run Application

1. Run command in terminal (in your project directory): `npm run build`. This will update anything related to your `App.js` file (so `public/index.html`, any CSS you're pulling in, etc).
2. Run command in terminal (in your project directory): `python3 app.py`
3. Preview web page in browser 'localhost:8080/' (or whichever port you're using)

### Deploy to Heroku

1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku main`

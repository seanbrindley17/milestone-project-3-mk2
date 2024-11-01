# Milestone Project 3

https://milestone-project-3-sb2-855f59c8cfc4.herokuapp.com/

## UX 

### Project Goal

When brainstorming ideas for a database project, SwimTimes was the first idea I had. I am a competitive swimmer and have been involved with various swimming clubs since 2006. In that time I have accrued a lot of timed swims and therefore data which could be used for a database project. I thought that a simple time storing site like this would be perfect as it allows me to use the skills I've learned in the example projects to start me off and also challenge myself using new aspects that weren't covered in the walkthroughs. In the future, with greater knowledge and more Python skills, I'd like to come back and refine this to include more functionality such a graphing time progression, but that will have to wait until a future date.

The site was built with a simple design and colour palette, and not too many complex moving parts as for me I want to be able to come back to the project, look at the code and be able to understand what's going on. 

## User Stories

My site is targetted at club swimmers and casual swimmers who want to keep track of times.

### New Site Users

* As a first time user I want to understand what the site is for.
* As a first time user I want to be able to quickly and easily register for an account.
* As a first time user I want to easily be able to add entries and see them on my home page.

### Returning Site Users

* As a returning user I want to be able to log in to my account and view my entries created previously.
* As a returning user I want to be able to create more entries, edit entries and delete ones when I so please.
* As a returning user I want to be able to use the filter to filter my entries to the search criterea chosen.

## Design

### Wireframes

Wireframes were created on [balsamiq](https://balsamiq.com/) for desktop, tablet and mobile displays.

![register page wireframe](/readme-documentation/wireframes/Register.png)

![log in page wireframe](/readme-documentation/wireframes/Log%20In.png)

![main page wireframe](/readme-documentation/wireframes/Main%20page%20when%20logged%20in.png)

![add time page wireframe](/readme-documentation/wireframes/Add%20Time.png)

![log out page wireframe](/readme-documentation/wireframes/Log%20Out.png)

### User Journey Chart

User journey was created using [LucidChart](https://lucid.app/).

![user journey](/readme-documentation/screenshots/user_journey/lucidchart%20user%20journey%20mp3.png)

### Database Overview

As I used [MongoDB](https://www.mongodb.com/), a non relational database, there's no need for a true schema. I have provided a quick overview of what my database looks like.

![database overview](/readme-documentation/screenshots/database_documentation/mongodb_collections/collections.png)

### Colours/Background

As there's a theme of water, I decided to go for blue/green colours for my backgrounds and decided against water-based background images on the grounds that it would make the text more washed out in places. Plus I prefer simple things.

I used [Materialize's colour palette](https://materializecss.com/color.html) and will document the colour classes used from there below:

* Where there is white text on darker backgrounds, I used Materialize's `white-text` class.

* The main colour used as the background colour is `#00acc1`, corresponding to Materialize's `"cyan darken-1"` classes.

* The colour used in the desktop navbar and all cards is `#1a237e`, corresponding to Materialize's `"indigo darken-4"` classes.

* The colour used in the mobile navbar is `#303f9f`, corresponding to Materialize's `"indigo darken-2"` classes.

* The colour used in my edit entry button on the entries.hmtl page is `#1e88e5`, corresponding to Materialize's `"blue darken-1"` classes.

* The colour used in my delete entry button on the entries.html page and cancel button on edit_entry.html is `#00838f`, corresponding to Materializes's `"cyan darken-3"` classes.

* The colour used on my submit entry button on new_entry.html, log in button on login.html and login and register buttons on welcome.html is `#00acc1`, corresponding to Materialize's `"cyan darken-1"` classes.

### Fonts

The fonts I used were from [Google Fonts](https://fonts.google.com/).

For my main font I used [Oxanium](https://fonts.google.com/specimen/Oxanium).

#### Font Awesome Icons

In my site I used icons from [FontAwesome](https://fontawesome.com/) to make my menu items look less bland.

* For the home links I used [this water ladder icon](https://fontawesome.com/icons/water-ladder?f=classic&s=solid).

* For the add new entry links I used [this stopwatch icon](https://fontawesome.com/icons/stopwatch?f=classic&s=solid).

* For the log out link I used [this exit icon](https://fontawesome.com/icons/arrow-right-from-bracket?f=classic&s=solid).

* For the welcome link I used [this waves icon](https://fontawesome.com/icons/water?f=classic&s=solid).

* For the log in link I used [this open door icon](https://fontawesome.com/icons/door-open?f=classic&s=solid).

* For the register link I used [this keyboard icon](https://fontawesome.com/icons/keyboard?f=classic&s=solid).

* For the mobile collapsible navbar I used [this right arrow icon](https://fontawesome.com/icons/circle-chevron-right?f=classic&s=solid).

### Favicon

I used [this icon](https://www.favicon.cc/?action=icon&file_id=231637) I found on favicon.cc for my Favicon.

### Technology Used

#### Coding Languages Used

* HTML - For site content.

* CSS - For site design and layout.

* Javascript - To initialise Materialize components using JQuery.

* Python - For site interactivity and dynamic elements.

#### Databases Used

I used [MongoDB](https://www.mongodb.com/) for my databasing needs. MongoDB is a non-relational database system.

#### Software and Programs Used

##### Framework

* [Flask](https://flask.palletsprojects.com/en/stable/) - To use templating code and other built in features such as flash(), render_template() and redirect().

* [Materialize](https://materializecss.com) - For design work, using their rows and columns components.

##### Libraries and Packages

* [PyMongo](https://pypi.org/project/pymongo/) - Python driver for MongoDB.

* [bson.ObjectID](https://www.mongodb.com/docs/manual/reference/method/ObjectId/) - To allow MongoDB to use _id as a unique identifier.

* [Werkzeug](https://werkzeug.palletsprojects.com/en/stable/) - For password hashing.

* [JQuery]() - To initialize the Materialize components used.

##### Software

* [VSCode](https://code.visualstudio.com/) - IDE used to create project.

* [Google Fonts](https://fonts.google.com/) - Location of fonts used.

* [Font Awesome](https://fontawesome.com/) - Location of icons used.

* [Materialize](https://materializecss.com) - Location of design framework used.

* [Chrome](https://www.google.com/intl/en_uk/chrome/) - My default browser.
    * Chrome Dev Tools - For debugging and troubleshooting,

* [Git](https://git-scm.com/) - Version control.

* [Github](https://github.com/) - Secure code storage.

* [Heroku](https://www.heroku.com/) - Deployment.

* [balsamiq](https://balsamiq.com/) - To create the wireframes.

* [LucidChart](https://lucid.app/) - To create the user journey.

* [Snipping Tool](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b) - To crop and save screenshots.

## Features

### Existing Features

| Feature | Description | Screenshot |
| :---: | :---: | :---: |
| Navbar (logged out) | What a user who isn't logged in will see | ![screenshot of not log in navbar](/readme-documentation/screenshots/site_screenshots/logged%20out%20navbar.png) |
| Navbar (logged in) | What a user who is logged in will see | ![screenshot of logged in navbar](/readme-documentation/screenshots/site_screenshots/logged%20in%20navbar.png) |
| Navbar (logged out mobile) | What a user who isn't logged in will see on mobile | ![screenshot of not log in navbar mobile](/readme-documentation/screenshots/site_screenshots/logged%20out%20mobile%20navbar.png) |
| Navbar (logged in mobile) | What a user who is logged in will see on mobile | ![screenshot of logged in navbar mobile](/readme-documentation/screenshots/site_screenshots/logged%20in%20mobile%20navbar.png) |
| Welcome Box | The first thing a new user should see, brief overview of site as well as log in and register buttons | ![screenshot of welcome box](/readme-documentation/screenshots/site_screenshots/welcome%20box.png) |
| Register Form | Register form for user to create account | ![screenshot of register form](/readme-documentation/screenshots/site_screenshots/registration%20form.png) |
| Log In Form | Allows user to log into their account | ![screenshot of log in form](/readme-documentation/screenshots/site_screenshots/log%20in%20form.png) |

### Future Features

## Testing

Testing was done on [TESTING.md](TESTING.md)

## Deployment

The site was deployed on [Heroku](https://www.heroku.com/) (note for future, may migrate to somewhere that offers free service when the college credits run out).

To deploy on Heroku, the project needs a requirements.txt file and a Procfile. The requirements.txt contains applications and dependecies to run the app and the Procfile tells Heroku which files actually run the app and how it's run.

* Create requirements.txt by using the following code in the terminal: `pip3 freeze > requirements.txt`

* Create the Procfile by using the following code in the terminal: `echo web: python app.py > Procfile`
    * Procfile has a capital P and no extension (.xxx) at the end.
    * Check the Procfile and make sure there's no blank line underneath the contents. If so, remove the blank line and save the file.

* Log in to [Heroku](https://www.heroku.com/).

* Click "New" in the top right corner of the screen and then "Create new app". Create a name for the app, which must be unique so consider adding your initials to the name. Select a region and click create app.

* Connect Heroku app to the Github repository by navigating to "Deploy", down to "Deployment Method" and click on Github. Find the correct repository for the project and click connect.

* Once connected, Heroku requires certain configuration variables to build the app. To sort this out, click on "Settings" tab, navigate down to the Config Vars section and click the "Reveal Config Vars" button. In here, you need to add the key and value variables stored in the env.py file.

| Key | Value |
|:---: | :---: |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | {your SECRET_KEY goes here} |
| MONGO_URI | {your MONGO_URI goes here} |
| MONGO_DBNAME | {your MONGO_DBNAME goes here } |

* Navigate to "Deploy" tab and scroll down to Automatic deploys. You can now enable automatic deploys and Heroku will begin building the app.

* Navigate to "Settings" and scroll down to Domains, which allows you add a custom domain.

### Local Deployment

To create a local copy of the site, you can clone or fork this repository.

### Cloning

To clone the repository:

* Go to the Github repository for the site [here](https://github.com/seanbrindley17/milestone-project-3-mk2).
* Click on the green Code button above the files. ![screenshot of code button](/readme-documentation/screenshots/general/github%20green%20code%20button.png)
* From the dropdown, select which remote repository URL you'd like to use from HTTPS, SSH or Github CLI, then click the copy url button.
* Open the Terminal in your code editor and change the current working directory to the location you want the cloned repository to go.
* In the Terminal, type git clone followed by the link you copied earlier from the repository.
* Press enter.

### Forking

To fork this repository:

* Log into your Github account and go to the Github repository for the site [here](https://github.com/seanbrindley17/milestone-project-3-mk2).
* Locate the Fork button near the top of the page and click it. (Greyed out for me because I own it of course). ![screenshot of fork button](/readme-documentation/screenshots/general/github%20fork%20button.png)
* On the next page, you can change the name to distinguish it from the original. Once done, click Create Fork to create a copy of the repository to your Github account. 


## Credits

* [This guide](https://realpython.com/python-comments-guide/) on Real Python for commenting best practices.

* [This guide](https://docs.python.org/3/howto/sorting.html) on Python's own documentation written by Andrew Dalke and Raymond Hettinger for introducing me to the lambda function which enabled my filters to begin working.

* [This guide](https://www.geeksforgeeks.org/python-string-split/) on GeeksForGeeks explaining the split() function in a little more detail allowing me to work out how to prepopulate my race time input fields in the edit_entry() function.

* To try and sort out my dates and times and make them more easily sortable, I used [This guide on DateTime](https://docs.python.org/3/library/datetime.html#datetime.datetime) from Python's own documentation and [This guide on strptime()](https://www.ibm.com/docs/en/i/7.5?topic=functions-strptime-convert-string-datetime) from IBM.
    * HOWEVER, I didn't end up using this. So some of my commits will have this code in but not my finished project.
        * UPDATE: Decided to give this a go again as my filter wasn't being fixed by anything I tried. I used [this StackOverflow post](https://stackoverflow.com/questions/53248537/typeerror-not-supported-between-instances-of-datetime-datetime-and-str) and [this StackOverflow post](https://stackoverflow.com/questions/19887353/attributeerror-str-object-has-no-attribute-strftime) along with [this](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [this](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime) from Python's official docs to finally work it out and get the date filter working.

### Code Used From Outside Sources

* I used [this StackOverflow post](https://stackoverflow.com/questions/69950552/mongodb-update-i-cant-update-my-documents-in-mongodb-with-flask-api) to fix an issue with the update_one() method not working properly.

* I used [this StackOverflow post](https://stackoverflow.com/questions/5655207/footer-not-sticking-to-bottom-of-page?rq=3) to help with my welcome footer not sitting at the bottom of the welcome page.

* I used [this StackOverflow post](https://stackoverflow.com/questions/15591620/how-to-retrieve-session-data-with-flask) to help with retrieving my user session cookie data to use in my add_new_entry() function.

* I used [this StackOverflow post](https://stackoverflow.com/a/54239464) for help with changing the colour of the Materialize selected options in my input fields.

* I used [this post on AdvancedCustomFields.com](https://support.advancedcustomfields.com/forums/topic/datepicker-disable-selecting-future-dates/#post-60753) to make it so that a user couldn't pick a date in the future in my date picker.

* I used [this post on GeeksForGeeks](https://www.geeksforgeeks.org/how-to-replace-text-with-css/) for help with changing text in elements at different screen sizes.

* I used [this page on Medium](https://medium.com/@zerox/keep-that-damn-footer-at-the-bottom-c7a921cb9551) to help with getting my footer to stay at the bottom.

#### Materialize.com

I used Materialize as the framework for this project using their code and JQuery initialisation. Components used will be listed here. JQuery initialisation is commented as such on the script.js file.

* The Materilize grid system used for page layout [here](https://materializecss.com/grid.html)

* To create the navbar and mobile collapse for the navbar [Materialize navbar (centre logo/mobile collapse)](https://materializecss.com/navbar.html).

* To create the tabs on my entries.html page [Materialize tabs](https://materializecss.com/tabs.html).

* I used [Basic Card](https://materializecss.com/cards.html) for the majority of my div containers, except on the Register.html form where Card Panel is used and entries.html where Horizontal Card is used.

* In my forms, I used [these text inputs (Input Fields)](https://materializecss.com/text-inputs.html), as well as the [Materialize Date Picker](https://materializecss.com/pickers.html).

    * Within the form input fields, I used [Materialize Select](https://materializecss.com/select.html) for options requiring a drop down along with the Disabled attribute.

* For my delete cofirmation feature, I used the [Materialize Modal](https://materializecss.com/modals.html) to show the user a pop up with confirmation when they click on delete.

* On my welcome.html page included the [Materialize Footer](https://materializecss.com/footer.html).
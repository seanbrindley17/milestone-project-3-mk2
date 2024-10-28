# Milestone Project 3

---

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

Wireframes were created on balsamiq for desktop, tablet and mobile displays.

![register page wireframe](/readme-documentation/wireframes/Register.png)

![log in page wireframe](/readme-documentation/wireframes/Log%20In.png)

![main page wireframe](/readme-documentation/wireframes/Main%20page%20when%20logged%20in.png)

![add time page wireframe](/readme-documentation/wireframes/Add%20Time.png)

![log out page wireframe](/readme-documentation/wireframes/Log%20Out.png)

### User Journey Chart

User journey was created using LucidChart

![user journey](/readme-documentation/screenshots/user_journey/lucidchart%20user%20journey%20mp3.png)

### Database Overview

As I used MongoDB, a non relational database, there's no need for a true schema. I have provided a quick overview of what my database looks like.

![database overview](/readme-documentation/screenshots/database_documentation/mongodb_collections/collections.png)

### Colours/Background

As there's a theme of water, I decided to go for blue/green colours for my backgrounds and decided against water-based background images on the grounds that it would make the text more washed out in places. Plus I prefer simple things.

I used [Materialize's colour palette](https://materializecss.com/color.html) and will document the colour classes used from there below:

* Where there is white text on darker backgrounds, I used Materialize's white-text class.

* The main colour used as the background colour is #00acc1, corresponding to Materialize's "cyan darken-1" classes.

* The colour used in the desktop navbar and all cards is #1a237e, corresponding to Materialize's "indigo darken-4" classes.

* The colour used in the mobile navbar is #303f9f, corresponding to Materialize's "indigo darken-2" classes.

* The colour used in my edit entry button on the entries.hmtl page is #1e88e5, corresponding to Materialize's "blue darken-1" classes.

* The colour used in my delete entry button on the entries.html page and cancel button on edit_entry.html is #00838f, corresponding to Materializes's "cyan darken-3" classes.

* The colour used on my submit entry button on new_entry.html, log in button on login.html and login and register buttons on welcome.html is #00acc1, corresponding to Materialize's "cyan darken-1" classes.

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

### Technology Used

#### Coding Languages Used

#### Software and Programs Used

## Features

### Existing Features

### Future Features

## Testing

## Deployment

### Local Deployment

### Cloning

### Forking

## Credits

* [This guide](https://realpython.com/python-comments-guide/) on Real Python for commenting best practices.

* [This guide](https://docs.python.org/3/howto/sorting.html) on Python's own documentation written by Andrew Dalke and Raymond Hettinger for introducing me to the lambda function which enabled my filters to begin working.

* [This guide](https://www.geeksforgeeks.org/python-string-split/) on GeeksForGeeks explaining the split() function in a little more detail allowing me to work out how to prepopulate my race time input fields in the edit_entry() function.

* To try and sort out my dates and times and make them more easily sortable, I used [This guide on DateTime](https://docs.python.org/3/library/datetime.html#datetime.datetime) from Python's own documentation and [This guide on strptime()](https://www.ibm.com/docs/en/i/7.5?topic=functions-strptime-convert-string-datetime) from IBM.
    * HOWEVER, I didn't end up using this. So some of my commits will have this code in but not my finished project.

### Code Used From Outside Sources

* I used [this StackOverflow post](https://stackoverflow.com/questions/69950552/mongodb-update-i-cant-update-my-documents-in-mongodb-with-flask-api) to fix an issue with the update_one() method not working properly.

* I used [this StackOverflow post](https://stackoverflow.com/questions/5655207/footer-not-sticking-to-bottom-of-page?rq=3) to help with my welcome footer not sitting at the bottom of the welcome page.

* I used [this StackOverflow post](https://stackoverflow.com/questions/15591620/how-to-retrieve-session-data-with-flask) to help with retrieving my user session cookie data to use in my add_new_entry() function.

* I used [this StackOverflow post](https://stackoverflow.com/a/54239464) for help with changing the colour of the Materialize selected options in my input fields.

* I used [this post on AdvancedCustomFields.com](https://support.advancedcustomfields.com/forums/topic/datepicker-disable-selecting-future-dates/#post-60753) to make it so that a user couldn't pick a date in the future in my date picker.

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
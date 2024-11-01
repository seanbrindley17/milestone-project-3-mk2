# Testing

Return to [README.md](README.md).

## Code Validation

### HTML

### CSS

| File | Screenshot | Notes |
| :---: | :---: | :---: |
| static/css/style.css | ![screenshot of initial css validation](/readme-documentation/screenshots/validation_screenshots/css/css%20initial%20validation.png) | Some errors resulting from semi colons being in the wrong place. |
| static/css/style.css | ![screenshot of css validation pass](/readme-documentation/screenshots/validation_screenshots/css/css%20validation%20pass.png) | Fixed by moving the semi colons into the correct place. No other errors found. |


### Javascript

I only used Javascript for JQuery code to initialise Materialize components.

| File | Screenshot | Notes |
| :---: | :---: | :---: |
| static/js/script.js | ![screenshot of js validation](/readme-documentation/screenshots/validation_screenshots/js/javascript%20validation.png) | One undefined variable which is the JQuery global selector so this is fine. |

### Python

To validate my Python code, I used [Pylint](https://pypi.org/project/pylint/) to see problems on the fly and [Black](https://pypi.org/project/black/) to format my Python code automatically upon saving, especially helpful for line breaks. This was all done within my IDE itself

| File | Screenshot | Notes |
| :---: | :---: | :---: |
| app.py | ![screenshot of python problems](/readme-documentation/screenshots/validation_screenshots/python/python%20problems.png) | The problems I have got would be what I consider to be totally irrelevant as the functions all work as intended. |
| env.py | Refer to above screenshot | env.py works as intended. |

## Browser Compatibility

## Responsiveness

## Accessibility

## Lighthouse Audit

## User Story Testing

## Defensive Programming

## Bugs/Issues

I didn't run into too many major bugs or issues that took any reasonable time to sort out, part of the joy of building simple. Most of the fixes came from tinkering with my Python code or making sure closing divs were in the right place. I tried not to use google too much for Python because the suggestions were things I had never seen before and would be able to understand which is a prerequisite for me as I want to understand what's going on.

* My major issue is the filter sometimes not working, I have absolutely no idea why as the dates are stored the same way sometimes it works and sometimes it doesn't. Searching for a solution throws me ideas that a. don't make sense to me and b. don't work either.
    * The issue seems to be that it's sorting by the day correctly but ignoring month and year.
        * This was solved by implimenting datetime modules instead of strings, and then re entering the data I had inputted already. The errors appeared to be springing because there were still string inputs so even though I had originally got my code correct I was still getting errors. Once I realised this it was a relatively straightforward fix with a bit of Googling.

* Tried to include Materialize's footer on my Welcome page but couldn't get it to work properly and stick to the bottom.
    * I ended up fixing this by simply attaching the footer content to the card panel underneath the register and log in buttons. 

* When building the filter feature, I noticed that when I edited an entry it would be filtered separately to the other entries for reasons unclear to me.
    * I believe I fixed this by just simplifying the sorting code I had. Google had told me about datetime and how to convert dates into strings and vice versa so I tried that and it made the issue worse so I removed all that.

* In my style.css file at the top I've used the global selector `*` to apply my chosen font to all the text. The issue I had was that it wasn't applying to the Materialize selected options in my add and entry entry pages.
    * Again, a good Google search helped to find the exact css code I needed to target to change the font as well as the colour and that I had to use `!important` as well to get the changes to take effect.

* In my `edit_entry.html` form, the date input field was taking up a full row despite me specifying `col s6 offset-s3` in the classes.
    * Turns out I had a closing `div` on the end of the line with the opening `div` instead of under the block of code I wanted the classes to apply to. This was the only closing div mistake that took me a while to catch.

* The Materialize date picker does not work very well on mobile devices.

* I couldn't work out how to make it so the flash() messages have something for the user to click on to get rid of them.
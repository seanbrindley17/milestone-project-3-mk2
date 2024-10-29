# Testing

Return to [README.md](README.md).

## Code Validation

### HTML

### CSS

### Javascript

### Python

## Browser Compatibility

## Responsiveness

## Accessibility

## Lighthouse Audit

## User Story Testing

## Defensive Programming

## Bugs/Issues

I didn't run into too many major bugs or issues that took any reasonable time to sort out, part of the joy of building simple. Most of the fixes came from tinkering with my Python code or making sure closing divs were in the right place. I tried not to use google too much for Python because the suggestions were things I had never seen before and would be able to understand which is a prerequisite for me as I want to understand what's going on.

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
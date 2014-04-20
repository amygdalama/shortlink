# A Link Shortener

This is a Flask App with a simple form to enter URLs. The app generates a shortened URL (this is really just `/i`, where `i` increases by 1 each time a new link is entered) and stores the original link and the shortened link in a text file. The shortened link then redirects to the original link.

# To-dos

* Make the method of link shortening less dumb
* Store the links in a database rather than a text file
* Deploy the app somewhere other than localhost

More things to do (from HS Jobs Friday):
* Display data on how much a link gets used
* Make that data private to whoever made the original shortened link
* Make shortened links not guessable
* Deploy your site somewhere besides localhost 
* Graphically display the click data
* Load test your server - can you take 100 posts per second? 1000 shortened link GETs per second? How many redirections or shortens can your site do per second? What was the bottleneck?
* Make a bookmarklet that gives the user the shortened version of a link without leaving a page.
* Style your page a bit
* Update your link click stats in realtime (no refresh required)
* Break down link click stats by browser
* Build an api for people to use to access their click data
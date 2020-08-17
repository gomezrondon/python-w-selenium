import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser


br = RoboBrowser(user_agent='a python robot')
#1) go to wikipedia
br.open("https://www.wikipedia.org/" )
# pepe = str(br.parsed())
# print(pepe)

# 2) select the title
# elem = br.select('h1.central-textlogo-wrapper') #works
elem = br.select('span.central-textlogo__image') #works better
# 2.1) print the title
print(elem[0].text) #bingo!
# me trajo en una lista todo el texto del tag h1
# [<h1 class="central-textlogo-wrapper">
# <span class="central-textlogo__image sprite svg-Wikipedia_wordmark">
# Wikipedia
# </span>
# <strong class="jsl10n localized-slogan" data-jsl10n="slogan">The Free Encyclopedia</strong>
# </h1>]
#--------------------- input box
#https://pypi.org/project/robobrowser/
#3) find the search form
form = br.get_form(id='search-form')
#4) insert term to search
form['search'].value = 'canada history' #searh is the name of tag, id did not work
# 5) sumit form
br.submit_form(form )

# <optional>) print web page
pepe = str(br.parsed())
print(pepe)
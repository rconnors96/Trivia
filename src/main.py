import json
import urllib.request
import ssl

OpentdbCategoriesURL = "https://opentdb.com/api_category.php"
Categories = {}

# TODO: allow user to pick category

def main():
    getcategories()

# obtains categories from URL and creates a dictionary from them
def getcategories():
    obtainedcategories = urlrequest(OpentdbCategoriesURL)
    categories = json.loads(obtainedcategories)
    categorieslist = categories["trivia_categories"]
    Categories = createcategorydictionary(categorieslist)


# turns the received list into a dictionary
def createcategorydictionary(templist):
    newdict = {}

    for dictionary in templist:
        for i in dictionary:
            newdict.update({dictionary['id']: dictionary['name']})

    return newdict


# obtains html content from a given url
def urlrequest(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    r = urllib.request.urlopen(url)
    urlbytes = r.read()

    htmlcontent = urlbytes.decode("utf8")
    r.close()

    return htmlcontent


main()

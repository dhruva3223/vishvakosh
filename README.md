#### [Live Demo](https://vishvakosh.herokuapp.com/)

# vishvakosh


#### A Wikipedia-like online encyclopedia (Markdown to HTML)


![vishvakosh-animate](https://user-images.githubusercontent.com/91244148/178155570-40833ab5-adcc-4f19-9ba0-57ccac9b7f25.gif)


## Overview
"vishvakosh" is a Wikipedia-like online encyclopedia using Python, Django, CSS, HTML and Markdown. It is a Django application that allows users to view, create, and edit entries in its encyclopedia. Each entry is stored server side in a lightweight Markdown file. When looking at an entry's page, the Markdown is converted to HTML using the `markdown2` Python library. The raw Markdown can also be viewed/edited when going into the edit mode of a specific page.

Each entries allows an image. There is a random page link that will redirect the user to a random page from the list of existing encyclopedia entries. Also, one can search for entries using the search bar. If the query matches an entry, the user is redirected to that entry's page. If the query is a substring of any entry, a list will be created for navigation.

In conclusion, to add to the encyclopedia one can click the "Create New Page" link. All that's needed to create a new entry is to type in a title and the Markdown contents to be stored.

A particular page can be edited by clicking on "Edit Page" which will redirect you to a textarea which pre-populated with the existing Markdown content of the page. You can also change the image on that page.

## Requirements

- python
- django
- markdown2

## To run the application 
```
python manage.py runserver
```


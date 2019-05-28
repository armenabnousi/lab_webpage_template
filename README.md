## Django-based template for lab/personal webpages
### (Django, CSS, HTML)

To see an example of this template visit the [Heroku deployment of it](https://armenlab.herokuapp.com/).
This is a simple template specially for academic labs and personal webpages. All the data in the webpage are being maintained and updated through tab-separated (tsv) files, without any need for changes in HTML files.</br>

To modify the contents of the webpage simply edit the tab separated files in the labapp/data directory. To change the pictures, add the new pictures in the labapp/static/images directory.

Note that since the data files are being read everytime the webpage is visited, this is not the most efficient implementation but since lab personal webpages generally don't have heavy content or traffic, the ease of uses balances off that disadvantage.

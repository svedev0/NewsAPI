from configparser import ConfigParser
from newsapi import NewsApiClient

# Please read the official documentation
# https://newsapi.org/docs/client-libraries/python

def get_articles():
	config = ConfigParser()
	config.read('config.ini')
	api_key = config['API']['KEY']

	# Initialise NewsAPI client
	newsapi = NewsApiClient(api_key)

	# Get top headlines
	top_headlines = newsapi.get_top_headlines(
		q='AI',                 # Key word
		category='technology',  # News category
		language='sv',          # Publication language
		country='se',           # Publication country
		page_size=5             # Number of articles
	)

	# Extract articles from JSON response
	result = top_headlines['articles']
	return result


if __name__ == '__main__':
	articles = get_articles()

	# Process articles individually
	for article in articles:
		author = article['author']
		publishedAt = article['publishedAt'].replace('T',' ').replace('Z','')
		title = article['title'].replace(f' - {author}','')
		url = article['url']

		# Print result
		print(author, f'({publishedAt})')
		print(title)
		print(url + '\n')

import pyshorteners

# Enter your bit.ly API key here
BITLY_API_KEY = "YOUR_BITLY_API_KEY"

# Create an instance of pyshorteners.Shortener() with the bit.ly service and your API key
s = pyshorteners.Shortener('bit.ly', api_key=BITLY_API_KEY)

# Enter the URL to be shortened
url = input("Enter the URL to be shortened: ")

# Shorten the URL using the bit.ly service
short_url = s.short(url)

# Display the shortened URL
print("Shortened URL: ", short_url)

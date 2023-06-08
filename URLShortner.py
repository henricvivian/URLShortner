import pyshorteners

def shorten_url(url, api_key):
    shortener = pyshorteners.Shortener('bit.ly', api_key=api_key)
    return shortener.short(url)

def main():
    # Enter your Bitly API key here
    bitly_api_key = "YOUR_BITLY_API_KEY"

    # Enter the URL to be shortened
    url = input("Enter the URL to be shortened: ")

    # Shorten the URL using the Bitly service
    short_url = shorten_url(url, bitly_api_key)

    # Display the shortened URL
    print("Shortened URL:", short_url)

if __name__ == "__main__":
    main()

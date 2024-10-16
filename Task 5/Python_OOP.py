# importing necessary libraries
from datetime import datetime
import random


# first class for news
class News:
    # declaring init method with parameters
    def __init__(self, text, city):
        self.text = text
        self.city = city

    # method to generate our feed template
    def news_feed(self):
        return f"""
        News-------
        {self.text}
        {self.city}, {datetime.now().strftime("%m/%d/%Y %H:%M")}
        """

    # method to put our feed into the file
    def put_feed_into_file(self):
        news_feed_text = self.news_feed()
        file_name = "feeds.txt"
        # Using 'with' automatically handles file closing
        with open(file_name, "a+") as file:
            file.write(news_feed_text + "\n")


# second class for private ad
class PrivateAd:
    # declaring init method with parameters
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = expiration_date

    # method to generate our feed template
    def ad_feed(self):
        return f"""
        Private Ad-------
        {self.text}
        Actual until: {self.expiration_date}, {(datetime.strptime(self.expiration_date, "%m/%d/%Y").date() - datetime.now().date()).days} days left
        """

    # method to put our feed into the file
    def put_feed_into_file(self):
        priv_ad_text = self.ad_feed()
        file_name = "feeds.txt"
        # Using 'with' automatically handles file closing
        with open(file_name, "a+") as file:
            file.write(priv_ad_text + "\n")


# third class for joke of the day
class JokeOfTheDay:
    # declaring init method with parameters
    def __init__(self, text):
        self.text = text

    # method to generate our feed template
    def joke_feed(self):
        return f"""
        Joke of the day-------
        {self.text}
        Funny meter - {random.randint(0, 10)} out of 10
        """

    # method to put our feed into the file
    def put_feed_into_file(self):
        joke_feed_text = self.joke_feed()
        file_name = "feeds.txt"
        # Using 'with' automatically handles file closing
        with open(file_name, "a+") as file:
            file.write(joke_feed_text + "\n")


news1 = News(input("Input news text: "), input("Input news city: "))
news1.put_feed_into_file()

ad1 = PrivateAd(input("Input ad text: "), input("Input ad expiration date in the format MM/DD/YYYY: "))
ad1.put_feed_into_file()

joke1 = JokeOfTheDay(input("Input your joke text: "))
joke1.put_feed_into_file()

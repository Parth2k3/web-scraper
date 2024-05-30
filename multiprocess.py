import threading

from web_scraping.scrapeform import scrapeform
from web_scraping.scrapemovies import scrapemovies
from web_scraping.scrapeadvanced import scrapeadvanced
from database.database import delete_database

threads = []


thread1 = threading.Thread(target=scrapeform, args=())
threads.append(thread1)
thread1.start()

thread2 = threading.Thread(target=scrapeadvanced, args=())
threads.append(thread2)
thread2.start()

thread3 = threading.Thread(target=scrapemovies, args=())
threads.append(thread3)
thread3.start()


for thread in threads:
    thread.join()

# delete_database('movies')
# delete_database('teams')
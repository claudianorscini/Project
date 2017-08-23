import take_data.scrape as scrape

app_id = "338018403288147"
app_secret = "fSkFSqFtOVgs-ATkEmQXyI1Cc-0"
access_token = app_id + "|" + app_secret

page_id = 'tods'


scrape.scrapeFacebookPageFeedStatus(page_id, access_token)

import json
import csv
import datetime
import time
import take_data.login as login
import take_data.process as process


def scrapeFacebookPageFeedStatus(page_id, access_token):
    with open('%s_facebook_statuses.csv' % page_id, 'wb') as file:
        w = csv.writer(file)
        w.writerow(["status_id", "status_message", "link_name", "status_type", "status_link",
           "status_published", "num_likes", "num_comments", "num_shares"])

        has_next_page = True
        num_processed = 0   # keep a count on how many we've processed
        scrape_starttime = datetime.datetime.now()

        print "Scraping %s Facebook Page: %s\n" % (page_id, scrape_starttime)

        statuses = login.getFacebookPageFeedData(page_id, access_token, 100)

        while has_next_page:
            for status in statuses['data']:
                w.writerow(process.processFacebookPageFeedStatus(status))

                # output progress occasionally to make sure code is not stalling
                num_processed += 1
                if num_processed % 1000 == 0:
                    print "%s Statuses Processed: %s" % (num_processed, datetime.datetime.now())

            # if there is no next page, we're done.
            if 'paging' in statuses.keys():
                statuses = json.loads(login.request_until_succeed(statuses['paging']['next']))
            else:
                has_next_page = False


        print "\nDone!\n%s Statuses Processed in %s" % (num_processed, datetime.datetime.now() - scrape_starttime)

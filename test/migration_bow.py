#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import yaml
import json

deals_file = open("techno_deals.yml")
campaign_deals_file = open("campaign_deals.yml")

techno_deals = yaml.load(deals_file)
campaign_deals = yaml.load(campaign_deals_file)

campaign_deals_uuid =  set([deal['uuid'] for deal in campaign_deals])
orphans = []

print "-- MIGRATION SCRIPT FOR DEALS BAG OF WORD - RD15 --"
print
print "USE techno;"
print
print "TRUNCATE TABLE deal_bag_of_words;"
print

for deal in techno_deals:
    sql = "INSERT INTO deal_bag_of_words(uuid, bag_of_words) VALUES ('%s', '%s');"
    if deal['uuid'] in campaign_deals_uuid:
        print sql % (deal['uuid'],
                        json.dumps(deal['bag_of_words']).replace("'", r"\'"))
    else:
        orphans.append(deal)

print

if orphans:
    print "-- ORPHAN DEALS TO ADD MANUALLY --"
    for orphan in orphans:
        print "-- ", orphan

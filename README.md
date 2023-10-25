# Speyeder
A web spider/crawler for bug bounties. Find every link with no need to worry about dupes

Works by searching for every href, checking if its already been found, then going to it and checking for more links. Add each link found to a blacklist to avoid dupes.

Contains a blacklist var that blocks from scanning sites such as google, facebook, etc. Add your own as needed.

# Use: Python3

speyeder.py -h
Proxy use: speyeder.py [Server] -p 1.2.3.4
Scan file with proxy: speyeder.py -f filename -p 1.2.3.4
Scan with file: speyeder.py -f filename

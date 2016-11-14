#**HospitalHacks**
##Exposing Medical Conditions through Anonymized Trip Data
by Reade Levinson

![alt tag](http://i.giphy.com/10ub3b5xW3NfDG.gif)

#Introduction

Unlike most European countries, the United States does not have a blanket privacy law under which to regulate privacy concerns in the digital era. Instead, consumer protection agencies like the Federal Trade Commission rely on more specific laws -- HIPPA, Gramm-Leach-Blilley, and others -- to set guidelines for data protection.

Consequently, my goal was to pull enough information from the TLC trip data in a way that might jeopardize privacy under one of these specific laws, in this case, the Health Insurance Portability and Accountability Act of 1996 (HIPAA).

The Taxi and Limousine Commission isn't covered by HIPPA because the Act regulates health care and insurance providers as well as third party "data processors", and TLC fits into none of these categories. However, for the purposes of hackathon, I considered the Commission  a "Business Associate", defined as a "person or organization...that provides certain services to a covered entity that involve the use or disclose or individually identifiable health information." I believe trip data has the potential to disclose identifiable health information, as explained below.

**My goal was to identify trips taken to or from medical facilities and the people taking those trips.**

*\*\*Caveat: Didn't get very far into this project (#election2016 : weary :), so this is more potential than discovery.*

#Plan of Action
###Datasets

I used three (3) datasets for this challenge:

1. [TLC Trip Record Data.](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) Data from every taxi and limousine trip in NYC.

2. [Health and Hospitals Corporation (HHC) Facilities.](https://nycplatform.socrata.com/Health/Health-and-Hospitals-Corporation-HHC-Facilities/f7b6-v6v3) A geo-coded database of HHC facilities in the New York area, available for free download.

3. Voter registration data for New York, easy (enough) to obtain from [NationBuilder](http://nationbuilder.com/).

###Methodology
Using numpy and pandas in Python, first split massive trip dataset into smaller, 200k row text files. Bring the trip datasets and list of medical facilities into Python dataframes. When the pickup or dropoff coordinates from a taxi trip match those of a medical facility, add trip to a new database called "Medical Trips." Do the same for each of the smaller, 200k row files. 

At the end, you have a spreadsheet with all the TLC trips taken to/from known medical facilities. 

Geocode the addresses from the voter registration data base and match the database, as much as possible, to the medical trips spreadsheet. 

###Troubleshooting

This sort of mapping -- using voter registration data to identify individuals -- is faulty at best, especially in New York City which is filled with apartment complexes and multi-family homes. Plus, renters might sublet or taxi miders might simply not be picked up or dropped off at the same address they live at. They might get out of the cap early if they hit traffit...the list goes on. 

Multiple people -- or someone completely different -- could live at the address in the database.

Also, this database is not going to include emergencies, where people are likely calling 9-1-1 and going to hospitals in ambulences. It's also not likely pregnancies, or deaths. 

#Findings

The most interesting -- and potentially compromising -- findings will be when the data show repeated trips to and from a medical facility. Perhaps someone has kidney failure or cancer and goes to the hospital every Wednesday at 3pm for dialysis or chemo. 

There are numerous reasons why someone might elect to keep medical information secret:
*[Why we don't talk about our illnesses](https://www.psychologytoday.com/blog/contemporary-psychoanalysis-in-action/201211/secrets-and-health-keeping-illness-hidden), by Ruth Livingston
*[9 Diseases People Keep Secret](http://www.everydayhealth.com/healthy-living-pictures/diseases-people-keep-secret.aspx), *[Healthy Living]*
*[Keeping Cancer a Secret](http://well.blogs.nytimes.com/2013/07/04/keeping-cancer-a-secret/), by Mikkael A. Sekeres, M.D. *[NYT]*
*[Keeping Death in the Dark](https://www.theguardian.com/lifeandstyle/2016/jan/15/death-in-the-dark-david-bowie-jackie-collins-secret-terminal-illness), by Leo Benedictus *[Guardian]*

As Nicholas Sparks wrote:
>I've learned that we're all entitled to have our secrets.








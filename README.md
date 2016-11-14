#Hospital Hacks: Exposing Medical Conditions through Anonymized Trip Data

##TLC Hackathon Project, November 2016

Caveat: Didn't get very far into this project (#election2016), so this is more potential than discovery.

##Methodology

Unlike most European countries, the United States does not have a blanket privacy law under which to regulate privacy concerns in the digital era. Instead, consumer protection agencies like the Federal Trade Commission rely on more specific laws -- HIPPA, Gramm-Leach-Blilley, and others -- to set guidelines for data protection.

Consequently, my goal was to pull enough information from the TLC trip data in a way that might jeopardize privacy under one of these specific laws, in this case, the Health Insurance Portability and Accountability Act of 1996 (HIPAA).

**My goal was to identify trips taken to or from medical facilities and the people taking those trips.**

The Taxi and Limousine Commission isn't covered by HIPPA because the Act regulates health care and insurance providers as well as third party "data processors", and TLC fits into none of these categories. However, for the purposes of hackathon, I considered the Commission  a "Business Associate", defined as a "person or organization...that provides certain services to a covered entity that involve the use or disclose or individually identifiable health information." I believe trip data has the potential to disclose identifiable health information, as explained below.


##Datasets

I used three (3) datasets for this challenge:

1. Trip data provided by TLC

2. Geo-coded list of medical facilities in the New York area, available for free download here linkl[](dddd.www)

3. Voter registration data for New York, easy (enough) to obtain from NationBuilder[]().

##Plan

Using numpy and pandas in Python, first split massive trip dataset into smaller, 200k row text files. Bring the trip datasets and list of medical facilities into Python dataframes. When the pickup or dropoff coordinates from a taxi trip match those of a medical facility, add trip to a new database called "Medical Trips." Do the same for each of the smaller, 200k row files. 

At the end, you have a spreadsheet with all the TLC trips taken to/from known medical facilities. 

Geocode the addresses from the voter registration data base and match the database, as much as possible, to the medical trips spreadsheet. 

##Known issues (yes, there are many)

This sort of mapping -- using voter registration data to identify individuals -- is faulty at best, especially in New York City which is filled with apartment complexes and multi-family homes. Plus, renters might sublet or taxi miders might simply not be picked up or dropped off at the same address they live at. They might get out of the cap early if they hit traffit...the list goes on. 

Multiple people -- or someone completely different -- could live at the address in the database.

Also, this database is not going to include emergencies, where people are likely calling 9-1-1 and going to hospitals in ambulences. It's also not likely pregnancies, or deaths. 

##Findings

Instead, the most likely findings will come from repeated trips. Perhaps someone has kidney failure or cancer and goes to the hospital every Wednesday at 3pm for dialysis or chemo.  

The most interesting -- and potentially compromising -- aspects will come where the data show repeated trips to a medical facility from the same address.





This branch contains all the generated and exported files from the PIs the to the MISP Server 


To clone this repo onto the VM you can use the below code in the terminal:
git clone https://github.com/Luitsy/Ready-to-Graduate.git --branch MISP ~/Desktop/Ready-to-Graduate


# Ready-to-Graduate
Honeypot - IT Project II

This branch is for all uploaded csv (data) files from the Strawberry Pi's - please export your scripts into this branch. 
The Ubuntu MISP server will pull from this branch every 30 mins to import the data into the MISP server. 

There is a template file that has the headings that MISP requires for a succesful import, not all headings need to have data added. see https://www.misp-standard.org/rfc/misp-standard-core.html#name-format-2 for more details

UUID is recommended to be generated using UUID Ver 4 (see https://www.uuidgenerator.net/) or in Python

import uuid
myuuid = uuid.uuid4()
print('Your UUID is: ' + str(myuuid))

# Transferring Data from the VM to MISP Server
The data that is collected on the Strawberry Pi VM is pushed to the Github every 30 minutes. This is also pulled into the MISP server every 30 minutes, so there is a constant stream of new data. Importing the data into a MISP event is currently not automated and is discussed in the next step.

# Importing files into MISP
A CSV file is pulled from the Github every 30 minutes, and stored in the MISP folder on the Desktop. This file can be imported as is into MISP. 

- Click add event on the left and fill in the basic details about the event (name, date, threat level) and submit. 
- Click populate from... (left column) then freetext import. The data from the CSV file can then be inserted into the text box as is, and MISP will automatically detect the useful information. 
- Click OK then refresh the page to load the new data. 

MISP will show what bits of data have appeared in previous events and you can edit the data/ add comments to assist MISP in analysis. 

# Generating a report from MISP
Once an event has been made and populated, a report can be generated. 

- Click download from the left column
- Choose the CSV option and save

Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 

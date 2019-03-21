# Overview

Google Keep does not have an "import" feature, although this has been a request 
for more than half a decade. This little app will read a directory of HTML files
and import (text only) to Google keep.  It will create one note per file. 

The path supplied on the command line should be a directory of HTML files (or 
tree of directories). The immediate parent directory name is also used as a 
label attached to each of the notes created from the directory.

My specific use case was to migrate from Evernote to Google Keep. So, step 1, in 
this case is to export your notes from Evernote.  This web page has instructions
for that: https://www.guidingtech.com/60155/export-evernote-data-onenote-google-keep/


# Thanks

Thanks to https://github.com/kiwiz/gkeepapi for an "Unofficial" Google Keep API.
Google does not provide an API for third party developers, but this library uses
the internal, undocumented api directly.  

Implications:
1. Could break at any time, due to changes in Google internal API
2. Typical oauth and service management provided by google projects is not supported, so you have to login with email and password.
  

# Usage

I use poetry to manage the dependencies.

    poetry install
    poetry run python gkimport/main.py PATH_TO_DIRECTORY_OF_HTML_FILES
    
You will be prompted for your google email and password.


# Distribution

I considered setting this app up as a service with a trivial UI, so non-developers 
could use it easily. But due to the log in requirements noted above, users would have
to give the service their google password in plaintext. I wouldn't want to encourage
people to do something that is so inherently insecure.
 

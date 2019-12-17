# Importing functions
import sys

from functions import getLatestWordpressDir

# Importing const variables
from props import projectsDirectory

props = sys.argv
# Pop the first item cause its filename
props.pop(0)

print(props)

wordpressVersions = getLatestWordpressDir()

if wordpressVersions == False:
  print('No wordpress files avaible')
  exit()
else:
  print('Avaible files')
  print(wordpressVersions)
  # Do everything correct => copy files with proper new name
  # then create proper file structure inside wp-content themes
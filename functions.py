import os

def getWordpressVersions():
  directories = os.listdir()

  if "wordpress-files" in directories:
    wordpressFiles = os.listdir('./wordpress-files')
    wordpressFolders = []
    for fileName in wordpressFiles:
      # Looping through each file name and cheking if it's not zip
      if not '.zip' in fileName:
        # Here for sure it's folder (subdirectory)
        wordpressFolders.append(fileName)

    if len(wordpressFolders) > 0:
      return wordpressFolders
    else:
      return False

  return False

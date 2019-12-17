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


def convertProps(props):

  # Parametrs: 1=name, 2=version
  correctProps = []

  if len(props) == 0:
    correctProps.append('default-prj-name')
  elif len(props) == 1:
    # I suppose name is correct - later i'll try to create checking funtion
    correctProps.append(props[0])
  elif len(props) == 2:
    # I suppose name is correct - later i'll try to create checking funtion
    correctProps.append(props[0])
    if '@' in props[1]:
      correctProps.append(props[1])
    else:
      print('Not correct wp version. Use "@" at the start.')
      exit()
  else:
    print('Something went wrong with props converting')
    exit()

  return correctProps

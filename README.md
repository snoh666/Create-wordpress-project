# Create wordpress project

## Why created?

  I was very frustrated creating for every new project new wordpress directory so i decided to speed it up and there you go. This command should save you a lot of time in copying files and creating new themes directory, because it does it all for you!

## How to start using it?

  1. Make folder with name "wordpress-files" inside put folders with sample wordpress files structure names as below
      > wp-[version]
  1. Inside props.py input your directory name where all your project will be created
  1. Add this folder to PATH variable. In case of git bash you have to
      > export PATH:'<path-to-this-folder>'
  1. It should now be ready to use! In case of any errors feel free to open one.

  ### REMEMBER!
  Git bash doesnt have default aliases like windows does so you will have to start command by wp-create.bat or create proper alias

## TODOS

  * Create MVP

  ### Also i would like to

  * Look for ways to dynamically look for latest wordpress version and download it
  * Check if there is a way to configurate it with sql
import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'TPTV-Installer'
EXCLUDES       = [ADDON_ID, 'repository.TPTV', 'plugin.program.TPTV-Installer']
# Text File with build info in it.
BUILDFILE      = 'http://wizard.tech-portal.tv/autobuilds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'http://wizard.tech-portal.tv/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Youtube Reviews & Tutorials'
YOUTUBEFILE    = 'http://wizard.tech-portal.tv/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://wizard.tech-portal.tv/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://wizard.tech-portal.tv/advanced.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://wizard.tech-portal.tv/buildsicon.png'
ICONMAINT      = 'http://wizard.tech-portal.tv/mainticon.png'
ICONAPK        = 'http://wizard.tech-portal.tv/apkicon.png'
ICONADDONS     = 'http://wizard.tech-portal.tv/addoninstallericon.png'
ICONYOUTUBE    = 'http://wizard.tech-portal.tv/youtubeicon.png'
ICONSAVE       = 'http://wizard.tech-portal.tv/savedata.png'
ICONTRAKT      = 'http://wizard.tech-portal.tv/trakticon.png'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://wizard.tech-portal.tv/loginicon.png'
ICONCONTACT    = 'http://wizard.tech-portal.tv/contact.png'
ICONSETTINGS   = 'http://wizard.tech-portal.tv/settingsicon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '=='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'BF9D6E48'
COLOR2         = 'ghostwhite'

# Primary menu items   / %s is the menu item and is required
THEME1         = '[B][COLOR '+COLOR1+']TPTV >[/COLOR][/B]  [I][COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[B][COLOR '+COLOR1+']Current Build >[/COLOR][/B]  [I][COLOR '+COLOR2+']%s[/COLOR][/I]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[B][COLOR '+COLOR1+']Current Theme >[/COLOR][/B]  [I][COLOR '+COLOR2+']%s[/COLOR][/I]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Tech-Portal.tv\r\n\r\nContact us on facebook at https://www.facebook.com/groups/Tech.Portal.TV.EN/\nContact us on facebook at https://www.facebook.com/groups/Tech.Portal.TV.NL/'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://wizard.tech-portal.tv/autobuilds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.TPTV'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.github.com/Steindenaer/repository.TechPortal/master/repository.TPTV/addon.xml'
# Url to folder zip is located in
REPOZIPURL     = 'http://wizard.tech-portal.tv/Repo/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = 'http://wizard.tech-portal.tv/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font24'
HEADERMESSAGE  = 'TPTV Wants to notify you about:'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'http://wizard.tech-portal.tv/TPTV-installer.jpg'
#########################################################
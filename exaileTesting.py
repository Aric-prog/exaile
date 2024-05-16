import pyautogui
import os
import time
import subprocess

# Specify the path to the exe file
exe_path = "G:\exaile\exaile.exe"

# Define the positions of buttons
buttonPos = {
    'closeBtn': (2522, 9),  # close Exaile
    'closeCurrentTab': (17, 81),  # closeCurrentTab
    'playOrPause': (432, 1461),  # play and pause
    'stopMusic': (474, 1461),  # stop
    'nextMusic': (501, 1461),  # next
    'lastMusic': (398, 1461),  # last
    'volumeZero': (2433, 168),  # Zero
    'volumeHalf': (2481, 168),  # Half
    'volumeMax': (2529, 168),  # Max
    'mute': (2403, 168),  # Mute
    'refreshCollection': (354, 84),  # refreshCollection
    'searchInputPlayList': (2307, 1421),  # searchInputPlayList
    'searchInputCollection': (104, 120),  # searchInputPlayList
    'musicRepeat': {
        'original': (441, 1418),  # Position of the 'musicRepeat' button
        'off': (494, 1320),  # Position of the 'musicRepeat off' button
        'all': (494, 1350),  # Position of the 'musicRepeat all' button
        'one': (494, 1380),  # Position of the 'musicRepeat one' button

    },
    'shuffleOrder': {
        'original': (405, 1425),  # Position of the 'shuffleOrder' button
        'off': (468, 1290),  # Position of the 'shuffleOrder off' button
        'track': (494, 1320),  # Position of the 'shuffleOrder track' button
        'album': (494, 1350),  # Position of the 'shuffleOrder album' button
        'random': (494, 1380),  # Position of the 'shuffleOrder random' button
    },
    'file': {
        'original': (23, 45),  # Position of the 'File' button
        'new_playlist': (60, 72),  # Position of the 'New Playlist' button
        'open': (60, 107),
        'openUrl': (60, 143),
        'openDirectories': (60, 174),
        'importPlayList': (60, 204),
        'exportCurrentPlayList': (60, 240),
        'closeTab': (60, 270),
        'quit': (60, 300),
    },
    'chooseFileOpenWindow': {
        'open': (2319, 1416),
        'cancel': (2234, 1416),
        'musicFile': (2289, 1368),
        'recent': (240, 227),
        'home': (240, 267),
        'desktop': (240, 307),
        'documents': (240, 347),
        'switchFileType': (2289, 1335),
        'recentFirstDict': (446, 240),
        'recentSecondDict': (446, 267)
    },
    'chooseDirectoryWindow': {  # openDirectories(60, 174)
        'open': (2319, 1416),
        'cancel': (2234, 1416),
        'recent': (240, 227),
        'home': (240, 267),
        'desktop': (240, 307),
        'documents': (240, 347),
        'recentFirstDict': (446, 240),
        'recentSecondDict': (446, 267)
    },
    'editTab': {
        'original': (72, 45),  # Position of the 'edit' button
        'collection': (120, 78),  # Position of the 'edit collection' button
        'queue': (120, 110),  # Position of the 'edit Queue' button
        'cover': (120, 141),  # Position of the 'edit Covers' button
        'preference': (120, 172),  # Position of the 'edit Preference' button

    },
    'collection': (15, 123),
    'radio': (15, 231),
    'playLists': (15, 326),
    'closeLastPlayList': (2529, 209),
    'lyrics': (15, 417),
    'Podcasts': (15, 513),
    'groupTagger': (15, 639),

}

isPlaying = False
isMute = False


def take_screenshot(file_name):
    """
    Takes a screenshot of the entire screen and saves it as a file.

    Args:
        folder_path (str): The path to the folder where the screenshot will be saved.
        file_name (str): The name of the screenshot file.

    Returns:
        str: The full path to the saved screenshot file.
    """
    # Ensure the folder exists, create it if it doesn't
    if not os.path.exists('testResultImg'):
        os.makedirs('testResultImg')

    # Combine folder path and file name to get the full file path
    file_path = os.path.join('testResultImg', file_name)

    # Take screenshot of the entire screen and save it as the specified file
    pyautogui.screenshot(file_path)

    return file_path


def checkWindowSize():
    # Print the screen size
    print('window Size:', pyautogui.size())


# Case 1: Open exaile (Run the exe file using subprocess)
def openExaile():
    subprocess.Popen(exe_path)  # Using Popen() instead of run()
    time.sleep(5)  # Wait for 3 seconds to ensure the program has fully started
    maximizeWindow()
    take_screenshot('openExaile.png')

# case2: Maximize the Exaile window.
def maximizeWindow():
    pyautogui.hotkey('alt', 'space', 'x')
    # Wait for the window to be maximized
    time.sleep(1)
    take_screenshot('maximizeWindow.png')


# case 3: close Exaile
def close_exaile():
    pyautogui.click(buttonPos['closeBtn'])
    take_screenshot('close_exaile.png')


# case 4: switch switchCollectionTab
def switchCollectionTab():
    pyautogui.click(buttonPos['collection'])  # Click the 'File' button
    time.sleep(1)
    take_screenshot('switchCollectionTab.png')


# case 5: switch switchRadioTab
def switchRadioTab():
    pyautogui.click(buttonPos['radio'])  # Click the 'File' button
    time.sleep(1)
    take_screenshot('switchRadioTab.png')


# case 6: switch PlayListsTab
def switchPlayListsTab():
    pyautogui.click(buttonPos['playLists'])  # Click the 'PlayLists' button
    time.sleep(1)
    take_screenshot('switchPlayListsTab.png')


# case 7: switch switchLyricsTab
def switchLyricsTab():
    pyautogui.click(buttonPos['lyrics'])  # Click the 'Lyrics' button
    time.sleep(1)
    take_screenshot('switchLyricsTab.png')


# case 8: switch switchPodcastsTab
def switchPodcastsTab():
    pyautogui.click(buttonPos['podcasts'])  # Click the 'Podcasts' button
    time.sleep(1)
    take_screenshot('switchPodcastsTab.png')


# case 9: switch switchGroupTaggerTab
def switchGroupTaggerTab():
    pyautogui.click(buttonPos['groupTagger'])  # Click the 'GroupTagger' button
    time.sleep(1)
    take_screenshot('switchGroupTaggerTab.png')


# Test case10: Create a new playlist
def newPlayList():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['new_playlist'])  # Click the 'New Playlist' button
    time.sleep(1)
    take_screenshot('new_playlist.png')


# Test case11: close the last playlist
def closeLastPlayList():
    pyautogui.click(buttonPos['closeLastPlayList'])  # Click the 'closeLastPlayList' button
    time.sleep(1)
    take_screenshot('closeLastPlayList.png')


# Test case12: open the file window
def openFileWindow():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['open'])  # Click the 'file' => 'open' button
    time.sleep(1)
    take_screenshot('openDictWindow.png')


# Test case13: open for Url
def openForUrl():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['openUrl'])  # Click the 'file' => 'openUrl' button
    time.sleep(1)
    take_screenshot('openForUrl.png')


# Test case14: open Directories
def openDirectories():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['openDirectories'])  # Click the 'file' => 'open Directories' button
    time.sleep(1)
    take_screenshot('openDirectories.png')


# Test case15: open Import PlayList
def openImportPlayList():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['importPlayList'])  # Click the 'file' => 'Import PlayList' button
    time.sleep(1)
    take_screenshot('openImportPlayList.png')


# Test case16: open Export Current PlayList
def openExportCurrentPlayList():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['exportCurrentPlayList'])  # Click the 'file' => 'Export Current PlayList' button
    time.sleep(1)
    take_screenshot('openExportCurrentPlayList.png')


# Test case17: close Current Playlist
def closeCurrentPlaylist():
    newPlayList()
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['closeTab'])  # Click the 'file' => 'close Tab' button
    time.sleep(1)
    take_screenshot('closeCurrentPlaylist.png')


# Test case18: quit Exaile
def quitExaile():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['quit'])  # Click the 'file' => 'quit Exaile' button
    time.sleep(1)
    take_screenshot('quitExaile.png')


# Test case19: switch OpenFile Recent <= File
def switchOpenFileRecent():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['open'])  # Click the 'file' => 'open' button
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['recent'])  # => Recent
    time.sleep(1)
    take_screenshot('switchOpenFileRecent.png')


# Test case20: switch OpenFile Home <= File
def switchOpenFileHome():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['open'])  # Click the 'file' => 'open' button
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['home'])  # => Home
    time.sleep(1)
    take_screenshot('switchOpenFileHome.png')


# Test case20: switch OpenFile Desktop <= File
def switchOpenFilDesktop():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['open'])  # Click the 'file' => 'open' button
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['desktop'])  # => Desktop
    time.sleep(1)
    take_screenshot('switchOpenFilDesktop.png')


# Test case21: switch OpenFile Documents <= File
def switchOpenFileDocuments():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['open'])  # Click the 'file' => 'open' button =>
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['documents'])  # => Desktop
    time.sleep(1)
    take_screenshot('switchOpenFileDocuments.png')


# Test case22: switch OpenFile Downloads <= File
def switchOpenFileDownloads():
    pyautogui.click(buttonPos['file']['original'])  # Click the 'File' button
    time.sleep(1)
    pyautogui.click(buttonPos['file']['open'])  # Click the 'file' => 'open' button
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['downloads'])  # => Downloads
    time.sleep(1)
    take_screenshot('switchOpenFileDownloads.png')


# Test case23: OpenFile - Try clicking the unclickable open button <= File
def clickOpenFileOpenDisabled():
    switchOpenFileRecent()
    pyautogui.click(buttonPos['chooseFileOpenWindow']['open'])  # => open btn
    time.sleep(1)
    take_screenshot('clickOpenFileOpenDisabled.png')


# Test case24: OpenFile - Try clicking the close openWindow button <= File
def clickOpenFileWindowClose():
    switchOpenFileRecent()
    pyautogui.click(buttonPos['chooseFileOpenWindow']['cancel'])  # => cancel btn
    time.sleep(1)
    take_screenshot('clickOpenFileWindowClose.png')


# Test case25: OpenFile - Try switch FileType <= File
def openFileWindowSwitchFileType():
    switchOpenFileRecent()
    pyautogui.click(buttonPos['chooseFileOpenWindow']['switchFileType'])  # => switchFileType
    pyautogui.click(2274, 1332)  # => Supported Files
    take_screenshot('openFileWindowSwitchFileType-support.png')
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['switchFileType'])  # => switchFileType  ##### bug1: music file cannot be classified
    pyautogui.click(2274, 1368)  # => Music Files
    take_screenshot('openFileWindowSwitchFileType-music.png')
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['switchFileType'])  # => switchFileType
    pyautogui.click(2274, 1374)  # => PlayList Files
    take_screenshot('openFileWindowSwitchFileType-playList.png')
    time.sleep(1)
    pyautogui.click(buttonPos['chooseFileOpenWindow']['switchFileType'])  # => switchFileType
    pyautogui.click(2274, 1374)  # => All Files
    take_screenshot('openFileWindowSwitchFileType-All.png')
    time.sleep(1)


# Test case26: Open - play music <= File
def openFilePlayMusic():
    openFileWindow()
    pyautogui.click(438, 276)  # => first Music
    time.sleep(1)
    pyautogui.click(2328, 1379)  # => play
    isPlaying = True
    time.sleep(1)
    take_screenshot('openFilePlayMusic.png')
    time.sleep(1)


# Test case27: play music
def playMusic():
    if isPlaying:
        pauseMusic()
    else:
        pyautogui.click(buttonPos['playOrPause'])  # => play
        time.sleep(1)
        take_screenshot('playMusic.png')
        time.sleep(1)


# Test case28: pause music
def pauseMusic():
    if not isPlaying:
        playMusic()
    else:
        pyautogui.click(buttonPos['playOrPause'])  # => pause
        time.sleep(1)
        take_screenshot('pauseMusic.png')
        time.sleep(1)


# Test case29: stop music
def stopMusic():
    if not isPlaying:
        playMusic()
    pyautogui.click(buttonPos['stopMusic'])  # => pause
    time.sleep(1)
    take_screenshot('stopMusic.png')
    time.sleep(1)


# Test case30: next music
def nextMusic():
    if not isPlaying:
        playMusic()
    lastMusic()
    pyautogui.click(buttonPos['nextMusic'])  # => pause
    time.sleep(1)
    take_screenshot('nextMusic.png')
    time.sleep(1)


# Test case31: last music
def lastMusic():
    if not isPlaying:
        playMusic()
    nextMusic()
    pyautogui.click(buttonPos['nextMusic'])  # => pause
    time.sleep(1)
    take_screenshot('nextMusic.png')
    time.sleep(1)


# Test case32: close Current tab
def closeCurrentTab():
    pyautogui.click(buttonPos['closeCurrentTab'])  # => close Current Tab
    time.sleep(1)
    take_screenshot('closeCurrentTab.png')
    time.sleep(1)


# Test case33: open edit collection
def openEditCollection():
    pyautogui.click(buttonPos['editTab']['original'])  # => open edit Tab
    time.sleep(1)
    pyautogui.click(buttonPos['editTab']['collection'])  # => open collection Tab
    time.sleep(1)
    take_screenshot('openEditCollection.png')
    time.sleep(1)


# Test case34: open edit queue
def openEditQueue():
    pyautogui.click(buttonPos['editTab']['original'])  # => open edit Tab
    time.sleep(1)
    pyautogui.click(buttonPos['editTab']['queue'])  # => open queue Tab
    time.sleep(1)
    take_screenshot('openEditQueue.png')
    time.sleep(1)


# Test case35: open edit cover
def openEditCover():
    pyautogui.click(buttonPos['closeCoverTab'])  # => open edit Tab
    time.sleep(1)
    pyautogui.click(buttonPos['editTab']['cover'])  # => open cover Tab
    time.sleep(1)
    take_screenshot('openEditCover.png')
    time.sleep(1)


# Test case36: open edit cover
def openEditPreference():
    pyautogui.click(buttonPos['closeCoverTab'])  # => open edit Tab
    time.sleep(1)
    pyautogui.click(buttonPos['editTab']['preference'])  # => open preference Tab
    time.sleep(1)
    take_screenshot('openEditPreference.png')
    time.sleep(1)


# Test case37: setVolumeMax
def setVolumeMax():
    if not isPlaying:
        playMusic()
    pyautogui.click(buttonPos['volumeMax'])  # => max
    time.sleep(1)
    take_screenshot('setVolumeMax.png')
    time.sleep(1)


# Test case38: setVolumeHalf
def setVolumeHalf():
    if not isPlaying:
        playMusic()
    pyautogui.click(buttonPos['volumeHalf'])  # => Half
    time.sleep(1)
    take_screenshot('setVolumeHalf.png')
    time.sleep(1)


# Test case39: setVolumeZero
def setVolumeZero():
    if not isPlaying:
        playMusic()
    pyautogui.click(buttonPos['volumeZero'])  # => Zero
    time.sleep(1)
    take_screenshot('setVolumeZero.png')
    time.sleep(1)


# Test case40: setMute
def setMute():
    if not isPlaying:
        playMusic()
    if isMute:
        releaseMute()
    pyautogui.click(buttonPos['mute'])  # => mute
    take_screenshot('setMute.png')
    time.sleep(1)


# Test case41: releaseMute
def releaseMute():
    if not isPlaying:
        playMusic()
    if not isMute:
        setMute()
    pyautogui.click(buttonPos['mute'])  # => unmute
    take_screenshot('releaseMute.png')
    time.sleep(1)


# Test case42: Search from playList
def musicSearchPlayList():
    pyautogui.click(buttonPos['searchInputPlayList'])  # => searchInputPlayList
    time.sleep(1)
    pyautogui.typewrite("love")
    time.sleep(1)
    take_screenshot('musicSearchPlayList.png')
    time.sleep(1)


# Test case43: Search from playList
def musicSearchCollection():
    pyautogui.click(buttonPos['searchInputCollection'])  # => searchInputPlayList
    time.sleep(1)
    pyautogui.typewrite("1")
    time.sleep(1)
    take_screenshot('musicSearchCollection.png')
    time.sleep(1)


# Test case44: refresh Collection
def refreshCollection():
    pyautogui.click(buttonPos['refreshCollection'])  # => searchInputPlayList
    time.sleep(1)
    take_screenshot('musicSearchCollection.png')
    time.sleep(1)


# Test case45: musicRepeatOff
def musicRepeatOff():
    pyautogui.click(buttonPos['musicRepeat']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['off'])  # => off
    time.sleep(1)
    take_screenshot('musicRepeatOff.png')
    time.sleep(1)


# Test case46: musicRepeatAll
def musicRepeatAll():
    pyautogui.click(buttonPos['musicRepeat']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['all'])  # => all
    time.sleep(1)
    take_screenshot('musicRepeatAll.png')
    time.sleep(1)


# Test case47: musicRepeatOne
def musicRepeatOne():
    pyautogui.click(buttonPos['musicRepeat']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['one'])  # => one
    time.sleep(1)
    take_screenshot('musicRepeatOne.png')
    time.sleep(1)

# Test case48: shuffleOrderTrack
def shuffleOrderTrack():
    pyautogui.click(buttonPos['shuffleOrder']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['track'])  # => track
    time.sleep(1)
    take_screenshot('shuffleOrderTrack.png')
    time.sleep(1)


# Test case49: shuffleOrderAlbum
def shuffleOrderAlbum():
    pyautogui.click(buttonPos['shuffleOrder']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['album'])  # => album
    time.sleep(1)
    take_screenshot('shuffleOrderAlbum.png')
    time.sleep(1)


# Test case50: shuffleOrderRandom
def shuffleOrderRandom():
    pyautogui.click(buttonPos['shuffleOrder']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['random'])  # => random
    time.sleep(1)
    take_screenshot('shuffleOrderRandom.png')
    time.sleep(1)


# Test case51: shuffleOrderOff
def shuffleOrderOff():
    pyautogui.click(buttonPos['shuffleOrder']['original'])  # => original
    time.sleep(1)
    pyautogui.click(buttonPos['musicRepeat']['off'])  # => random
    time.sleep(1)
    take_screenshot('shuffleOrderOff.png')
    time.sleep(1)

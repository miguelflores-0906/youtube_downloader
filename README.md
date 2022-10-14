# YouTube Scraper
### By Miguel Flores
---
There are three scripts in this repository: scraper, frame_extractor, and frame_slicer.

## Scraper
1. Run the script in the CLI
2. Input the channel URL example: https://www.youtube.com/channel/UC0zHSfrOhKz_jRYtVrvU6zA (do not include other extensions such as "/videos" or "/featured")
3. Input how many videos the script would look through
4. Enter keywords to search for in the video titles (it would be good to skim through the channel to see what keywords are used)

## Frame Extractor
1. Make sure that the script is in the same folder as the video you want to extract frames from.
2. Run the script through the CLI and input the name of the video file WITH FILE EXTENSION.
3. A folder with the name of the video file will be created in the same directory as the script.

## Frame Slicer/Cropper
1. Replace the PATH variable with the path to the folder containing the images you want to slice/crop
2. Through the cli, input "python frame_slicer.py [number of cameras in the video]"
3. Folders in the PATH directory will be created with the sliced/cropped images


## Improvements that can be made
1. User interface - This will make the UX better especially if all can be added in one application. No more keyboard inputting, mostly just 
    mouse interactions from the user.
2. Better Web Crawler - currently, the user still has to look for a channel that suits their needs which could end up taking a long time.
    Perhaps implementing a web crawler that uses the keywords and looks for videos tagged as such for scraping instead of just the titles
    of the videos.
3. Larger scope - The scraper only takes from a single website (in this case, YouTube), being able to go through multiple websites could be
    an added feature in the future.

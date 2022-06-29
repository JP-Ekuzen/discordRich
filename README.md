# Discord Rich Desktop App

## Features
- Ability to store multiple profiles
- Fast modification of the current profile by 1-line editing

## Getting Started
Do you want to have your own editable game profiles in status on discord? Here’s what you need:

### Installation
1. Clone this repostory [github.com/JP-Ekuzen/discordRich](https://github.com/JP-Ekuzen/discordRich)
   ```sh
   git clone https://github.com/JP-Ekuzen/discordRich
   ```

2. Install Python package
   ```sh
   pip install pypresence
   ```
   
### Configuration

1. Enter [discord developer panel](https://discord.com/developers/applications)
  
2. Create a new app and name it as you want it to appear (you can change this later) 

![](https://i.imgur.com/h4i6EEV.png)
![](https://i.imgur.com/tZPJGXe.png)


3. Copy the app ID and paste it into the file **[profiles.json](https://github.com/JP-Ekuzen/discordRich/blob/master/profiles.json)** at the appropriate location

![](https://i.imgur.com/wb37zNk.png)

4. All editing options can be found in the file profiles.json and some pre-made profiles to help you understand which element is what. If you want to hide an element, you can find an example in the profile “clear” in the profiles.json file (primarily at the bottom)
- In the field “start_time_count” the expected format is the [timestamp](https://www.epochconverter.com/), but I added the possibility to enter the word “start” which counts from the machine the time from the start of the application
- The field “start_time_count” must be larger than “end_time_count”
- If we leave the field “end_time_count” blank and complete the field “start_time_count” with the value “start”, it shows how much the application is running. But if we add the fields “start_time_count” and “end_time_count”, the counter shows how much is left from the date of “start_time_count” to the date of “end_time_count”

![](https://i.imgur.com/yMgATod.png)

![](https://i.imgur.com/kYpfOeU.png)

5. As you can see, the profiles.json file can store several schemas, which you can easily switch between by renaming the active profile in the config.json file.

![](https://i.imgur.com/ubvGDIY.png)

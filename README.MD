<p align="center">
  <img src="Logo.png" alt="App Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-green"/>
</p>

# ***ImgFormat***

This GUI application allows you to convert **images** to any format which you can imagine. While many websites offer similar services, they often take more time and include ads. With **ImgFormat**, you can convert images fast and easy, saving both time and hassle! I created this app to make my work with photo easier and faster.

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Convert directly without the need for any API keys or extra configuration. Clone and run!
3. **Quick Conversion:** On Intel Core i3 10'th Gen it takes less than 2 seconds to convert image!
4. **User-Friendly GUI**: Easy-to-use graphical interface for a more intuitive experience. Our app has plenty amount of useful GUI features, which make this app very easy to use even for kids. 
5. **Optimised for low resolution monitors:** I know that a lot of people continue to use their ThinkPads etc. from 2004 or even older, so I decided to optimise this app for theirs displays. This app should work fine and not take a lot of space on your monitor even if he has only a 640x320 display resolution. On i3 manager you even can change a size of any window which this app will show to you, but I'm not sure about other window managers.
6. **Regular Updates:** This app is always up to date, so you can never care about her availability. We will notificate you about new available updates every time when you run this app.
7. **Compatible with old computers:** It should work fine even if you have a very old computer. I think that even any laptop from 2004 or even older will be able to work with this app without any issues, but be sure that he has a compatible OS!
8. **Any Formats:** You can enter your own format and app will try to find him.
9. **Offline:** This app is fully offline.

## Screenshots

SOON

> [!WARNING]
> I develop this app only on my Linux laptop, so I can't give to you any warranties that it will work the same on Windows. Maybe it can have some weird things in GUI, so if you will notice any bugs, please - send me an email with screenshot(s).

## Prerequisites

Before running the app, make sure you have the following installed:

- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.
- **PyQt6, pyqtdarktheme:** The most important things here! GUI.

## How to install ***Splash***

1. Clone this repository:

> git clone https://github.com/Vadkon07/ImgFormat

2. Open directory with installed repository and install requirements:

> pip install -r requirements.txt

> [!NOTE]
> Once I was trying to install this app on Windows, but I got some errors which told me to install **Visual C++ 14**, so you will also have to do it if you are a Windows user.

3. Run app:

> python main.py (or python3 main.py)

## PC Requirements

Here's **recommended** PC specifications:

- **OS:** Linux, Windows, MacOS, FreeBSD
- **RAM:** 256MB+
- **CPU:** Intel Pentium 4 or higher
- **GPU:** Probably any GPU will be enough.
- **Storage:** 300MB (app itself and her packages)

## How to use

1. Run the script in your terminal or command prompt. Of course you can just compile this app and run her as an app, but when you run it from terminal it shows to you all her features!
2. Click on 'File' and import you image.
3. Choose a format to which you would like to convert image, click 'Start' and then just wait for notifications.
4. The script will process and save the file(s) in folder in directory where you had an **original file in original format**.

## How to read version of this app

**In version 1.9.0.1 (example):**

    1: Major revision (new UI, lots of new features, conceptual change, etc.)

    9: Minor revision (maybe a change to a search box, 1 feature added, collection of bug fixes)

    0: Bug fix release (fix something what was wrong in code, improve align of image, etc.)

    1: Build number (if used)—that's why you see the .NET framework using something like 2.0.4.2709

## To-Do to release version 1.0

- [ ] **Optimise GUI:** Add some space between buttons, to prevent layering.
- [ ] **Improve README:** Better description, add screenshots.
- [X] **Create Logo:** We have to design a logo for our app.

## FAQ

**Q:** How much time it will take to install this app?
**A:** You just clone repository and then run 'pip install -r requirements.txt', and then everything depends from your internet connection. With a good internet connection it will take less than 5 minutes.

**Q:** Is there any kind of tracking of me when I use this app?
**A:** No, we just don't need it. All what you do will be stored ONLY LOCALY, and ONLY ON YOUR COMPUTER.

**Q:** Is this app is free to use?
**A:** Yes, this app is fully free and you will never need to pay to use her.

**Q:** How can I help developers of this app?
**A:** You have a lot of different ways to do it. At first the best help for us it's just to help us with development (bug fixes, new ideas, etc), but also you can help our developers with donations (open profile of a very active developer of this app and find a donation link.)

**Q:** Can I use this app without internet connection?
**A:** This app is fully offline, so it means that you can use all her **MAIN** functions without internet connection.

> [!WARNING]
> App will convert your images without internet connection, but some features as check updates will not work without internet.

**Q:** What if I got some errors while using the app and can't solve it?
**A:** Open new issue and our community will try to help you. At all at first try just to reinstall this app. Also at first try to use Google or any another search engine and paste in search error which you got. Usually it will help you to solve your problem faster.

> [!NOTE]
> At this moment I create this app fully alone, literally without any help. It will be nice to have a command of 2-3 people, just to work on our app faster. I go to school and have a busy schedule, so I'm not able to code all day long, especially because at home I have some problems with internet connection and don't have a computer. So, I'm always ready to start to work on this app together with you!

### Last Updated
> This README was last updated on **December 8, 2024** for version **v0.3.0**. All new things added in app afer this date + version are **NOT** described/mentioned here.

## License

> This project is licensed under the [MIT License](./LICENSE).

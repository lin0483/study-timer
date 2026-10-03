# Python Study Timer

A simple command-line Pomodoro study timer built with Python.

## Features

* Customizable study duration
* Customizable short break
* Customizable long break
* Long break after every 4 study sessions
* Countdown timer
* Sound notification when a timer finishes
* Stop the timer anytime with `Ctrl+C`
* Displays the total study time after finishing

## Technologies

* Python
* Time module
* User Input
* Functions and Loops

## How to Run

Make sure Python is installed, then run:

```bash
python study_timer.py
```

## How It Works

At the beginning, you can set the duration of:

* Study sessions
* Short breaks
* Long breaks

The timer starts a study session and then gives you a break. After every four completed study sessions, the application starts a longer break.

The default settings are:

```text
Study: 25 minutes
Short Break: 5 minutes
Long Break: 15 minutes
```

## Sound Notification

On Windows, the application uses `winsound` to play a beep when a timer finishes. On other systems, it uses the terminal bell instead.

## Project Structure

```text
python-study-timer/
│
├── study_timer.py
└── README.md
```

## Example

```text
=== Study Timer ===

Study minutes [25]:
Short break minutes [5]:
Long break minutes [15]:

Press Enter to start study session #1...
Studying  24:59 left

Great work! Sessions finished: 1

Time for a short break.
```

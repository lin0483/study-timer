# Study Timer (Pomodoro)
# Work for a while, take a short break, repeat.
# After every 4 study sessions you get a longer break.
# A beginner Python project: loops, functions, time and user input.

import time

try:
    import winsound  # Only on Windows: lets us play a beep sound
except ImportError:
    winsound = None


def beep():
    """Play a sound so you know the timer is finished."""
    if winsound:
        for _ in range(3):
            winsound.Beep(1000, 300)  # 1000 Hz for 0.3 seconds
    else:
        print("\a", end="")  # Terminal bell on other systems


def ask_minutes(question, default):
    """Ask for a number of minutes. Pressing Enter uses the default."""
    while True:
        answer = input(f"{question} [{default}]: ").strip()
        if answer == "":
            return default
        try:
            minutes = float(answer)
            if minutes > 0:
                return minutes
        except ValueError:
            pass
        print("Please type a number bigger than 0.")


def countdown(minutes, label):
    """Count down and show the time left on one line."""
    seconds_left = int(minutes * 60)
    while seconds_left > 0:
        mins, secs = divmod(seconds_left, 60)
        print(f"\r{label}  {mins:02d}:{secs:02d} left   ", end="", flush=True)
        time.sleep(1)
        seconds_left -= 1
    print(f"\r{label}  00:00 - done!      ")
    beep()


def main():
    print("=== Study Timer ===")
    print("Press Ctrl+C at any time to stop.\n")

    study = ask_minutes("Study minutes", 25)
    short_break = ask_minutes("Short break minutes", 5)
    long_break = ask_minutes("Long break minutes", 15)

    sessions_done = 0
    try:
        while True:
            input(f"\nPress Enter to start study session #{sessions_done + 1}...")
            countdown(study, "Studying")
            sessions_done += 1
            print(f"Great work! Sessions finished: {sessions_done}")

            if sessions_done % 4 == 0:
                input("You earned a long break! Press Enter to start it...")
                countdown(long_break, "Long break")
            else:
                input("Time for a short break. Press Enter to start it...")
                countdown(short_break, "Break")

            again = input("Keep going? (y/n): ").strip().lower()
            if again != "y":
                break
    except KeyboardInterrupt:
        print("\n\nTimer stopped.")

    total = sessions_done * study
    print(f"\nYou finished {sessions_done} session(s) - about {total:g} minutes of studying.")
    print("See you next time!")


if __name__ == "__main__":
    main()

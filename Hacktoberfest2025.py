# 🌸 Hacktoberfest 2025 Contribution
# Author: Deepali Agarwal
# A simple yet inspiring open-source program 💻✨

from datetime import datetime
import random

# Current year and time
year = datetime.now().year
time = datetime.now().strftime("%H:%M:%S")

# Fun Hacktoberfest messages
messages = [
    "Keep coding, keep growing 🌱",
    "Every pull request is a step toward mastery 💪",
    "Open source is where ideas come alive 🌍",
    "Celebrate progress, not perfection 🎉",
    "Hacktoberfest 2025 — Let’s build the future together 🚀",
    "The best code is written with passion ❤️"
]

print("\n==============================")
print(f"🌸 Welcome to Hacktoberfest {year}! 🌸")
print("==============================")
print(f"Current Time: {time}\n")
print("💬 Your Hacktoberfest Message of the Day:\n")
print(random.choice(messages))
print("\nMade with ❤️ by Deepali Agarwal for open-source community!\n")

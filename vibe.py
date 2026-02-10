#!/usr/bin/env python3
"""Vibe: tiny fun/useful CLI for focus + mood."""

from __future__ import annotations

import argparse
import random
import time
from datetime import datetime

QUOTES = [
    "Tiny steps count.",
    "Do it messy, then make it pretty.",
    "You don't need motivation to begin.",
    "Ship first, polish second.",
    "Future you says thanks.",
]

MOODS = {
    "calm": "🌊",
    "focus": "🎯",
    "hype": "⚡",
    "cozy": "🕯️",
    "creative": "🎨",
}

RANDOM_TASKS = [
    "clear 10 inbox emails",
    "organize one folder",
    "write a rough draft",
    "fix one annoying bug",
    "review your top 3 priorities",
]


def now() -> str:
    return datetime.now().strftime("%H:%M:%S")


def run_countdown(minutes: int) -> None:
    total = max(0, minutes) * 60
    for left in range(total, -1, -1):
        m, s = divmod(left, 60)
        print(f"\r⏳ {m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
    print("\n✅ Session complete.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Tiny vibe utility")
    parser.add_argument("--mood", choices=sorted(MOODS), default="focus")
    parser.add_argument("--minutes", type=int, default=10)
    parser.add_argument("--random-task", action="store_true", help="Pick a random task")
    parser.add_argument("task", nargs="*", help="What you're about to do")
    args = parser.parse_args()

    manual_task = " ".join(args.task).strip()
    task = random.choice(RANDOM_TASKS) if args.random_task else (manual_task or "something awesome")
    emoji = MOODS[args.mood]
    quote = random.choice(QUOTES)

    print(f"{emoji} [{now()}] Mood: {args.mood}")
    print(f"🛠️ Task: {task}")
    print(f"💬 {quote}")
    print(f"🚀 Starting {args.minutes} minute sprint...")
    run_countdown(args.minutes)


if __name__ == "__main__":
    main()

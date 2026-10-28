"""NM1130 SkillSprint Lab — simple menu to launch an experiment."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPERIMENTS = {
    "1": ("AI Fluency", "01.ai_fluency.py"),
    "2": ("AI Productivity", "02.ai_productivity.py"),
    "3": ("AI Applications", "03.ai_applications.py"),
    "4": ("LinkedIn Profile Analyzer", "04.linkedin_profile_analyzer.py"),
    "5": ("Cybersecurity Toolkit", "05.cybersecurity_toolkit.py"),
    "6": ("Mini Git", "06.mini_git.py"),
    "7": ("Power BI Dashboard", "07.power_bi_dashboard.py"),
    "8": ("Career Essentials", "08.career_essentials.py"),
}


def main():
    print("\n" + "=" * 52)
    print(" NM1130 | AI AND DIGITAL SKILLS LAB")
    print(" SkillSprint Student Edition")
    print("=" * 52)
    for number, (name, _) in EXPERIMENTS.items():
        print(f"{number}. {name}")
    print("Q. Quit")

    choice = input("\nChoose an experiment (1-8) or Q to quit: ").strip().lower()
    if choice in {"q", "quit", "exit"}:
        print("Lab closed. Keep learning!")
        return
    if choice not in EXPERIMENTS:
        print("Invalid choice. Please run the launcher again and select 1-8.")
        return

    name, filename = EXPERIMENTS[choice]
    command = [sys.executable, str(ROOT / filename)]
    if choice == "8" and input("Use your own skill ratings? (y/n): ").strip().lower() == "y":
        command.append("--interactive")
    print(f"\nLaunching: {name}\n")
    subprocess.run(command, cwd=ROOT, check=False)


if __name__ == "__main__":
    main()

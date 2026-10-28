# NM1130 — AI and Digital Skills Lab

**Student Edition | CSE (AI & ML)**  
University College of Engineering (BIT Campus), Anna University, Tiruchirappalli  
Academic Year 2026–2027

This repository contains eight beginner-friendly Python experiments for the NM1130 AI and Digital Skills record. Each program demonstrates the topic with a clear console output. The original experiment features are retained, with a small menu launcher and refreshed project documentation added for easier use.

## Experiments

| No. | Experiment | Main concepts |
|---:|---|---|
| 1 | AI Fluency | AI basics, classification, regression, clustering, optimization, neural networks and text sentiment |
| 2 | AI Productivity | Drafting emails, summarising text, extracting action items and sales insights; optional LLM demonstration |
| 3 | AI Applications | Healthcare prediction, fraud detection, recommendations and agriculture |
| 4 | LinkedIn Profile Analyzer | Profile checklist, score, improvement suggestions and comparison chart |
| 5 | Cybersecurity Toolkit | Password checks, secure password generation, hashing, phishing URL checks, TOTP and integrity checks |
| 6 | Mini Git | Simulated commits, branches, merges, conflicts, cloning, pushing and pull requests |
| 7 | Power BI Dashboard | Data cleaning, KPI calculations, dashboard image and CSV export |
| 8 | Career Essentials | Skill self-assessment, gap analysis, SMART goals and priority matrix |

## Quick start

1. Download or extract all repository files into the same folder.
2. Install Python 3.10 or newer.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the menu launcher:

   ```bash
   python run_lab.py
   ```

   Choose an experiment by entering its number. You can also run any experiment directly using the commands below.

## Run an experiment directly

```bash
python 01.ai_fluency.py
python 02.ai_productivity.py
python 03.ai_applications.py
python 04.linkedin_profile_analyzer.py
python 05.cybersecurity_toolkit.py
python 06.mini_git.py
python 07.power_bi_dashboard.py
python 08.career_essentials.py
```

To enter your own skill ratings in the Career Essentials experiment, run:

```bash
python 08.career_essentials.py --interactive
```

## Files created by experiments

- The LinkedIn Profile Analyzer can create `profile_improvement.png`.
- The Power BI experiment uses `07.sales_raw.csv` and creates a cleaned CSV and dashboard image in the project folder.
- The Career Essentials experiment can create `career_skills_radar.png`.

Generated files may be refreshed when you run the relevant experiment. Keep the CSV files with the Python scripts when running the Power BI experiment.

## Requirements

The project uses Python's standard library plus NumPy, pandas, scikit-learn and Matplotlib for the experiments that need them. The optional real generative-AI call in the productivity experiment requires a separately configured API key and optional provider package; the core examples work without it.

## Learning note

These programs are educational demonstrations. In particular, the cybersecurity and Mini Git examples are simplified learning tools, not replacements for production security systems or the real Git application.

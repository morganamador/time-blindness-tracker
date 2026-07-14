# **Time Blindness Tracker**
a CLI tool to track how long you *think* tasks take vs. how long they actually take. 
see also: [planning fallacy](https://en.wikipedia.org/wiki/Planning_fallacy)

## How to use:
run the tracker, enter your task name, give it a category and a time estimate. when you're done, enter how long it actually took you. the tool computes your error (+ means took longer than expected, - means went faster than expected), gives you feedback, and logs your data to a csv.

```
python tracker.py
```

designed to help productivity in individuals with ADHD or anyone with a desire to see their blind spots.

## Future plans
- analyze.py: category error averages, with directionality included, and ability to see your worst offenders (your blindest spots)
- internal timer with option to override
- category suggestions from existing data
- analysis of correlations of context notes (pending sufficient data)

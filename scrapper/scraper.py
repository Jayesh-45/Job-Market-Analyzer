from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin"],
    search_term="software engineer",
    location="India",
    results_wanted=10,
    country_indeed='India'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")
print(jobs.head()) 
jobs.to_csv("jobs.csv", index=False)
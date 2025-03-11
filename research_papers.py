import argparse
import pandas as pd
import requests

# Dummy API endpoint for example (replace with a real one if available)
API_ENDPOINT = "https://api.example.com/research-papers"

def fetch_research_papers(query, debug=False):
    if debug:
        print(f"Fetching papers for query: {query}")

    # Simulated API response (replace this with an actual API call)
    response = [
        {
            "title": "Advancements in Biotech Research",
            "authors": "Dr. A Smith, Dr. B Jones",
            "abstract": "This paper discusses recent biotech innovations...",
            "published_date": "2025-01-15",
            "affiliation": "XYZ Biotech Solutions"
        },
        {
            "title": "Pharmaceutical Breakthroughs in 2025",
            "authors": "Dr. C White, Dr. D Black",
            "abstract": "A detailed study on pharmaceutical developments...",
            "published_date": "2025-02-10",
            "affiliation": "ABC Pharma Inc."
        },
        {
            "title": "General Science Paper",
            "authors": "Dr. E Green, Dr. F Blue",
            "abstract": "An unrelated paper...",
            "published_date": "2025-02-18",
            "affiliation": "Non-Pharma University"
        }
    ]

    # Filter for pharmaceutical or biotech affiliations
    filtered_papers = [
        paper for paper in response
        if "pharma" in paper["affiliation"].lower() or "biotech" in paper["affiliation"].lower()
    ]

    if debug:
        print(f"Filtered {len(filtered_papers)} papers with pharmaceutical/biotech affiliations.")

    return filtered_papers

def save_to_csv(papers, filename):
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def print_results(papers):
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {paper['authors']}")
        print(f"Published Date: {paper['published_date']}")
        print(f"Affiliation: {paper['affiliation']}")
        print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers with pharma/biotech affiliations.")
    parser.add_argument("query", type=str, help="Search query for research papers")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information during execution")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results as CSV")
    args = parser.parse_args()

    papers = fetch_research_papers(args.query, args.debug)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        print_results(papers)

if __name__ == "__main__":
    main()

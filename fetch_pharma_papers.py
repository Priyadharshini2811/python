import requests
import csv

# Base URL for a research paper API (like arXiv or PubMed - replace with the actual API)
API_URL = "https://api.example.com/search"

def fetch_papers(query):
    params = {
        'q': query,
        'max_results': 50
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()['papers']
    else:
        print(f"Failed to fetch papers: {response.status_code}")
        return []

def filter_pharma_papers(papers):
    pharma_keywords = ["pharmaceutical", "biotech", "biotechnology", "pharma"]
    filtered = []
    for paper in papers:
        for author in paper.get('authors', []):
            affiliation = author.get('affiliation', '').lower()
            if any(keyword in affiliation for keyword in pharma_keywords):
                filtered.append({
                    'title': paper['title'],
                    'authors': ', '.join(a['name'] for a in paper['authors']),
                    'affiliations': ', '.join(a['affiliation'] for a in paper['authors']),
                    'published_date': paper['published_date'],
                    'url': paper['url']
                })
                break
    return filtered

def save_to_csv(papers, filename='pharma_papers.csv'):
    if not papers:
        print("No papers to save.")
        return
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'authors', 'affiliations', 'published_date', 'url'])
        writer.writeheader()
        writer.writerows(papers)
    print(f"Saved {len(papers)} papers to {filename}")

if __name__ == "__main__":
    query = input("Enter your research query: ")
    papers = fetch_papers(query)
    pharma_papers = filter_pharma_papers(papers)
    save_to_csv(pharma_papers)

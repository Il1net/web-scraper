import requests
from bs4 import BeautifulSoup

def main():
    print("🌐 Auto Web Scraper (extracts all readable text)")
    
    url = input("Enter website URL (e.g. https://example.com): ").strip()

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        tags_to_extract = ['h1', 'h2', 'h3', 'p', 'a', 'li', 'span', 'div']

        all_text = []
        for tag in tags_to_extract:
            elements = soup.find_all(tag)
            for el in elements:
                text = el.get_text(strip=True)
                if text and text not in all_text:
                    all_text.append(text)

        if not all_text:
            print("⚠️ No readable text found.")
            return

        print(f"\n✅ Extracted {len(all_text)} pieces of text:\n" + "-"*40)
        for i, text in enumerate(all_text, 1):
            print(f"{i}. {text}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

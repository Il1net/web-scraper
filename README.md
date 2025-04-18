# 🕷️ Simple Auto Web Scraper

This is a minimal Python-based web scraper that automatically extracts **all readable text** from a website without asking the user for any specific tags or selectors.

---

## 🚀 Features

- Asks only for the website URL
- Automatically extracts all visible text:
  - Headings (`h1`, `h2`, `h3`)
  - Paragraphs (`p`)
  - Links (`a`)
  - List items (`li`)
  - Span and div contents
- Outputs the text directly to the console

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install requests beautifulsoup4

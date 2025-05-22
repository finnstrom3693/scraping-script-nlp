import wikipediaapi

# Initialize Wikipedia API for English with a proper user agent
user_agent = "MyWikipediaScraper/1.0 (faizalnf1800@gmail.com)"
wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent=user_agent
)

# Define the page title
page_title = "Light_bomber"
page = wiki.page(page_title)

# Check if the page exists
if not page.exists():
    print("Page not found.")
    exit()

# Collect output in a list
output = []

# Add title and summary
output.append(f"# {page.title}\n")
output.append("## Summary\n")
output.append(page.summary + "\n")

# Function to recursively collect all sections and subsections
def collect_sections(sections, level=2):
    for section in sections:
        header = "#" * level + f" {section.title}\n"
        output.append("\n" + header + "\n")
        output.append(section.text + "\n")
        collect_sections(section.sections, level + 1)

# Collect all sections
collect_sections(page.sections)

# Save to file
file_path = "scrape_full.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(output)

print(f"Scraping completed and saved to '{file_path}'")

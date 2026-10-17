import os
import sys
import urllib.request
import urllib.parse
import re

BASE_DIR = r"c:\Users\Ankush Pandita\Desktop\koshur\library"

SOURCES = [
    {
        "category": "books",
        "filename": "lawrence_1895_valley_of_kashmir.txt",
        "url": "https://archive.org/download/valleyofkashmir00lawruoft/valleyofkashmir00lawruoft_djvu.txt",
        "title": "The Valley of Kashmir",
        "author": "Sir Walter Roper Lawrence"
    },
    {
        "category": "books",
        "filename": "grierson_1899_essays_on_kashmiri_grammar.txt",
        "url": "https://archive.org/download/kashmiriessaysonkashmirigrammargeorgegriersona._202003_670_U/Kashmiri%2C%20Essays%20on%20Kashmiri%20Grammar%20%20George%20Grierson%20A.%20_djvu.txt",
        "title": "Essays on Kashmiri Grammar",
        "author": "Sir George Abraham Grierson"
    },
    {
        "category": "catalogues",
        "filename": "buhler_1877_kashmir_manuscripts_tour.txt",
        "url": "https://archive.org/download/in.ernet.dli.2015.124536/2015.124536.Detailed-Deport-Of-A-Tour-In-Search-Of-Sanskrit-Mss-In-Kasmir-Rajputana-And-Central-India_djvu.txt",
        "title": "Detailed Report of a Tour in Search of Sanskrit MSS. in Kasmir",
        "author": "Dr. Georg Bühler"
    },
    {
        "category": "discourses",
        "filename": "temple_1924_word_of_lalla.txt",
        "url": "https://archive.org/download/TheWordOfLallaTheProphetessSirRichardCarnacTemple/The%20Word%20Of%20Lalla%20The%20Prophetess%20-%20Sir%20Richard%20Carnac%20Temple_djvu.txt",
        "title": "The Word of Lalla the Prophetess",
        "author": "Sir Richard Carnac Temple"
    },
    {
        "category": "discourses",
        "filename": "koul_1924_the_kashmiri_pandit.txt",
        "url": "https://archive.org/download/thekashmiripanditanandkoul/The%20Kashmiri%20Pandit%20-%20Anand%20Koul_djvu.txt",
        "title": "The Kashmiri Pandit: Early History, Social Customs, Language, and Folklore",
        "author": "Pandit Anand Koul"
    },
    {
        "category": "discourses",
        "filename": "vigne_1842_travels_in_kashmir.txt",
        "url": "https://archive.org/download/travelsinkashmir01vign/travelsinkashmir01vign_djvu.txt",
        "title": "Travels in Kashmir, Ladak, Iskardo",
        "author": "Godfrey Thomas Vigne"
    },
    {
        "category": "discourses",
        "filename": "dutt_1879_kings_of_kashmira_vol1.txt",
        "url": "https://archive.org/download/RajataranginiOfKalhana-English-JogeshChunderDuttVolumes12/Rajatarangini-JogeshChunderDuttVol1_djvu.txt",
        "title": "Kings of Kashmira (Vol. 1: Sanskrit Chronicles of Kalhana)",
        "author": "Jogesh Chunder Dutt"
    },
    {
        "category": "discourses",
        "filename": "dutt_1887_kings_of_kashmira_vol2_jonaraja.txt",
        "url": "https://archive.org/download/RajataranginiOfKalhana-English-JogeshChunderDuttVolumes12/Rajatarangini-JogeshChunderDuttVol2_djvu.txt",
        "title": "Kings of Kashmira (Vol. 2: The Rajatarangini of Jonaraja)",
        "author": "Jogesh Chunder Dutt"
    },
    {
        "category": "discourses",
        "filename": "dutt_1898_kings_of_kashmira_vol3_srivara.txt",
        "url": "https://archive.org/download/in.ernet.dli.2015.530049/2015.530049.kings-of_djvu.txt",
        "title": "Kings of Kashmira (Vol. 3: Rajatarangini of Srivara and Prajyabhatta)",
        "author": "Jogesh Chunder Dutt"
    },
    {
        "category": "discourses",
        "filename": "bernier_1665_travels_in_kashmir.txt",
        "url": "https://archive.org/download/travelsinmogulem00bernuoft/travelsinmogulem00bernuoft_djvu.txt",
        "title": "Travels in the Mogul Empire: Journey to the Kingdom of Kachemire",
        "author": "François Bernier"
    }
]

def clean_ocr_text(raw_text: str) -> str:
    """Normalize line endings and clean extraneous control characters."""
    t = raw_text.replace("\r\n", "\n").replace("\r", "\n")
    # Collapse 4+ newlines to double newlines
    t = re.sub(r"\n{4,}", "\n\n", t)
    return t.strip()

def download_all():
    print(f"Starting download of {len(SOURCES)} major historical volumes...")
    downloaded = 0
    total_added_words = 0

    for idx, s in enumerate(SOURCES, 1):
        target_dir = os.path.join(BASE_DIR, s["category"])
        os.makedirs(target_dir, exist_ok=True)
        dest_path = os.path.join(target_dir, s["filename"])

        print(f"\n[{idx}/{len(SOURCES)}] Downloading '{s['title']}' by {s['author']}...")
        print(f"  Source URL: {s['url']}")
        print(f"  Target: {s['category']}/{s['filename']}")

        try:
            req = urllib.request.Request(s["url"], headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                content = resp.read().decode("utf-8", errors="ignore")
                cleaned = clean_ocr_text(content)
                words = len(cleaned.split())
                chars = len(cleaned)

                with open(dest_path, "w", encoding="utf-8") as f_out:
                    f_out.write(cleaned)

                print(f"  -> SUCCESS: Saved {len(cleaned):,d} chars, {words:,d} words ({os.path.getsize(dest_path):,d} bytes)")
                downloaded += 1
                total_added_words += words
        except Exception as e:
            print(f"  -> FAILED: {e}")

    print("\n" + "=" * 60)
    print(f"DOWNLOAD COMPLETE: {downloaded}/{len(SOURCES)} volumes acquired.")
    print(f"Total new words downloaded into library: {total_added_words:,d}")
    print("=" * 60)

if __name__ == "__main__":
    download_all()

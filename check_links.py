import requests

INPUT_FILE = "playlist.m3u"
OUTPUT_FILE = "playlist.m3u"

def is_working(url):
    try:
        r = requests.get(url, timeout=10, stream=True)
        return r.status_code == 200
    except:
        return False

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        if line.startswith("http"):
            url = line.strip()
            if is_working(url):
                new_lines.append(line)
            else:
                print(f"❌ Çalışmıyor: {url}")
        else:
            new_lines.append(line)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("✅ Playlist güncellendi!")

if __name__ == "__main__":
    main()

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Tarih
bugun = datetime.now().strftime("%Y-%m-%d")
saat = datetime.now().strftime("%H-%M")

# Klasör oluştur
os.makedirs("knowledge/outputs", exist_ok=True)

# Dosya adı
output_file = f"knowledge/outputs/{bugun}-youtube-rapor.md"

# Stdin'den gelen içeriği oku (pipe ile kullanılacak)
content = sys.stdin.read()

# Dosyaya yaz
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"# /youtube Raporu — {bugun} {saat}\n\n")
    f.write(content)

print(f"✓ Rapor kaydedildi: {output_file}")
from pathlib import Path
from urllib.request import urlopen

base = Path('c:/Users/RYZEN5/OneDrive/Downloads/flo')
html_path = base / 'flo_unico.html'
html = html_path.read_text(encoding='utf-8')
url = 'https://cdn.jsdelivr.net/npm/three@0.148.0/build/three.min.js'
js = urlopen(url, timeout=30).read().decode('utf-8')
html = html.replace(
    '<script src="https://cdn.jsdelivr.net/npm/three@0.148.0/build/three.min.js"></script>',
    f'<script>{js}</script>'
)
html_path.write_text(html, encoding='utf-8')
print(f'Actualizado: {html_path}')
print(f'Tamaño final: {len(html)} bytes')

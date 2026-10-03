import json
import re
import os

html_path = r"C:\Users\psroh\.gemini\antigravity\brain\4f33ba8d-68e1-4c28-a571-a2f4e06c9a62\.user_uploaded\media_1791002861350.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

if not html_content:
    print("HTML not found!")
    exit(1)

# Remove overflow: hidden from body
html_content = html_content.replace('style="overflow: hidden;"', '')

# Add Lenis CSS and AOS CSS
head_insertion = """
<!-- AOS & Lenis CSS -->
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<style>
html.lenis, html.lenis body { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto !important; }
.lenis.lenis-smooth [data-lenis-prevent] { overscroll-behavior: contain; }
.lenis.lenis-stopped { overflow: hidden; }
.lenis.lenis-scrolling iframe { pointer-events: none; }
</style>
</head>
"""
html_content = html_content.replace("</head>", head_insertion)

# Add AOS and Lenis JS
body_insertion = """
<!-- AOS & Lenis JS -->
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.19/bundled/lenis.min.js"></script>
<script>
  // Initialize Lenis
  const lenis = new Lenis({ duration: 1.2, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // Initialize AOS
  AOS.init({
    duration: 1000,
    once: true,
    easing: 'ease-out-cubic',
    offset: 50
  });
</script>
</body>
"""
html_content = html_content.replace("</body>", body_insertion)

# Add data-aos to elements
# 1. Hero text
html_content = html_content.replace('<h1 class="font-serif', '<h1 data-aos="fade-up" data-aos-delay="200" class="font-serif')
html_content = html_content.replace('<p class="max-w-2xl', '<p data-aos="fade-up" data-aos-delay="400" class="max-w-2xl')
html_content = html_content.replace('<div class="flex flex-col sm:flex-row', '<div data-aos="fade-up" data-aos-delay="600" class="flex flex-col sm:flex-row')
html_content = html_content.replace('<div class="inline-flex items-center gap-2', '<div data-aos="fade-down" class="inline-flex items-center gap-2')

# 2. Section headers
html_content = html_content.replace('<div class="text-center max-w-3xl mx-auto mb-16">', '<div data-aos="fade-up" class="text-center max-w-3xl mx-auto mb-16">')
html_content = html_content.replace('<div class="flex flex-col md:flex-row md:items-end justify-between mb-14">', '<div data-aos="fade-up" class="flex flex-col md:flex-row md:items-end justify-between mb-14">')
html_content = html_content.replace('<div class="text-center max-w-3xl mx-auto mb-12">', '<div data-aos="fade-up" class="text-center max-w-3xl mx-auto mb-12">')
html_content = html_content.replace('<div class="text-center max-w-3xl mx-auto mb-14">', '<div data-aos="fade-up" class="text-center max-w-3xl mx-auto mb-14">')

# 3. About section
html_content = html_content.replace('<div class="lg:col-span-6 relative">', '<div data-aos="fade-right" class="lg:col-span-6 relative">')
html_content = html_content.replace('<div class="lg:col-span-6 space-y-6">', '<div data-aos="fade-left" class="lg:col-span-6 space-y-6">')

# 4. Signature dishes
html_content = html_content.replace('<article class="bg-white rounded-2xl overflow-hidden', '<article data-aos="fade-up" class="bg-white rounded-2xl overflow-hidden')

# 5. Menu items
html_content = html_content.replace('<div class="menu-item bg-white p-5', '<div data-aos="fade-up" class="menu-item bg-white p-5')

# 6. Cinematic quote
html_content = html_content.replace('<blockquote class="font-serif', '<blockquote data-aos="zoom-in" class="font-serif')

# 7. Gallery
html_content = html_content.replace('<div class="group relative rounded-2xl overflow-hidden cursor-pointer shadow-sm aspect-square bg-stone-100 gallery-trigger"', '<div data-aos="zoom-in" class="group relative rounded-2xl overflow-hidden cursor-pointer shadow-sm aspect-square bg-stone-100 gallery-trigger"')

# 8. Reviews
html_content = html_content.replace('<div class="bg-white p-7 rounded-2xl border border-amber-100 shadow-sm flex flex-col justify-between">', '<div data-aos="fade-up" class="bg-white p-7 rounded-2xl border border-amber-100 shadow-sm flex flex-col justify-between">')

# 9. Reservation
html_content = html_content.replace('<div class="bg-white rounded-3xl p-6 sm:p-10 border border-amber-200 shadow-warm-lg">', '<div data-aos="zoom-in-up" class="bg-white rounded-3xl p-6 sm:p-10 border border-amber-200 shadow-warm-lg">')

# 10. Contact
html_content = html_content.replace('<div class="lg:col-span-6 space-y-8">', '<div data-aos="fade-right" class="lg:col-span-6 space-y-8">')
html_content = html_content.replace('<div class="lg:col-span-6">\\n<div class="bg-white', '<div data-aos="fade-left" class="lg:col-span-6">\\n<div class="bg-white')

# Ensure the output directory exists
os.makedirs(r"C:\Users\psroh\.gemini\antigravity\scratch\anna_idli", exist_ok=True)

out_path = r"C:\Users\psroh\.gemini\antigravity\scratch\anna_idli\index.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Saved to {out_path}")

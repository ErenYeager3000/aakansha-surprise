import os

with open('d:/aakansha-surprise/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Fonts
html = html.replace('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,700&family=Cormorant+Garamond:ital,wght@1,300&display=swap" rel="stylesheet">', 
                    '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@1,700&family=Cormorant+Garamond:ital,wght@1,300&display=swap" rel="stylesheet">')

html = html.replace("font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;", 
                    "font-family: 'Outfit', -apple-system, sans-serif;")

# 2. Orb and Background CSS
old_orbs_css = '''  /* ── GLOBAL DARK GLOW THEMES (Immersive) ── */
  .bg-1 { background: #050002; }
  .bg-2 { background: #000408; }
  .bg-3 { background: #020005; }

  /* ── ORBS (Immersive Glow) ── */
  .orbs { position: absolute; inset: 0; pointer-events: none; overflow: hidden; filter: blur(75px); -webkit-filter: blur(75px); }
  .orb { position: absolute; border-radius: 50%; opacity: 0; transition: opacity 1.5s ease; mix-blend-mode: screen; }
  .active .orb { opacity: 0.65; }

  /* Page 1 — warm rose/peach */
  .orb-1 { width: 80vw; height: 80vw; background: #ff2a70; top: -10%; left: -20%; animation: orb-drift1 14s ease-in-out infinite alternate; }
  .orb-2 { width: 90vw; height: 90vw; background: #ffaa00; top: 40%; right: -25%; animation: orb-drift2 18s ease-in-out infinite alternate; }
  .orb-3 { width: 70vw; height: 70vw; background: #d81870; bottom: -15%; left: 5%;  animation: orb-drift3 15s ease-in-out infinite alternate; }

  /* Page 2 — aurora */
  .orb-a1 { width: 80vw; height: 80vw; background: #00ffaa; top: -15%; left: -10%; animation: orb-a1 15s ease-in-out infinite alternate; }
  .orb-a2 { width: 85vw; height: 85vw; background: #9900ff; top: 35%; right: -30%; animation: orb-drift2 17s ease-in-out infinite alternate; }
  .orb-a3 { width: 70vw; height: 70vw; background: #00bbff; bottom: -10%; left: -5%;  animation: orb-drift3 19s ease-in-out infinite alternate; }

  /* Page 3 — deep space */
  .orb-s1 { width: 90vw; height: 90vw; background: #4400cc; top: -10%; left: -30%; animation: orb-drift1 20s ease-in-out infinite alternate; }
  .orb-s2 { width: 80vw; height: 80vw; background: #aa00ff; top: 50%; right: -20%; animation: orb-drift2 16s ease-in-out infinite alternate; }
  .orb-s3 { width: 70vw; height: 70vw; background: #0022ff; bottom: -15%; left: 20%;  animation: orb-drift3 18s ease-in-out infinite alternate; }

  @keyframes orb-drift1 { 0%{transform:translate(0,0)} 100%{transform:translate(10vw,10vh)} }
  @keyframes orb-drift2 { 0%{transform:translate(0,0)} 100%{transform:translate(-8vw,12vh)} }
  @keyframes orb-drift3 { 0%{transform:translate(0,0)} 100%{transform:translate(8vw,-10vh)} }'''

new_orbs_css = '''  /* ── GLOBAL DARK GLOW THEMES (Immersive) ── */
  .bg-1 { background: #0b0205; }
  .bg-2 { background: #000408; }
  .bg-3 { background: #020006; }

  /* ── ORBS (Immersive Glow with Blob Wave) ── */
  .orbs { position: absolute; inset: 0; pointer-events: none; overflow: hidden; filter: blur(85px); -webkit-filter: blur(85px); }
  .orb { position: absolute; opacity: 0; transition: opacity 1.5s ease; mix-blend-mode: screen; animation: blob-float 22s infinite alternate ease-in-out; }
  .active .orb { opacity: 0.85; }

  @keyframes blob-float {
    0% { transform: translate(0, 0) scale(1) rotate(0deg); border-radius: 40% 60% 70% 30% / 40% 40% 60% 50%; }
    33% { transform: translate(8vw, -6vh) scale(1.1) rotate(120deg); border-radius: 60% 40% 30% 70% / 50% 60% 40% 40%; }
    66% { transform: translate(-5vw, 10vh) scale(0.9) rotate(240deg); border-radius: 30% 70% 50% 50% / 60% 30% 70% 40%; }
    100% { transform: translate(4vw, 4vh) scale(1.05) rotate(360deg); border-radius: 50% 50% 40% 60% / 40% 50% 50% 40%; }
  }

  /* Page 1 — vibrant rose/peach sweet colors */
  .orb-1 { width: 90vw; height: 90vw; background: #ff2a85; top: -15%; left: -25%; animation-delay: 0s; }
  .orb-2 { width: 85vw; height: 85vw; background: #ff9a44; bottom: -15%; right: -25%; animation-delay: -5s; }
  .orb-3 { width: 75vw; height: 75vw; background: #fc60a8; top: 25%; left: 15%; animation-delay: -9s; }

  /* Page 2 — aurora vibrant */
  .orb-a1 { width: 85vw; height: 85vw; background: #00f2fe; top: -15%; left: -15%; animation-delay: 0s; }
  .orb-a2 { width: 90vw; height: 90vw; background: #9b23ea; bottom: -15%; right: -25%; animation-delay: -7s; }
  .orb-a3 { width: 80vw; height: 80vw; background: #f093fb; top: 15%; left: 25%; animation-delay: -14s; }

  /* Page 3 — deep space */
  .orb-s1 { width: 80vw; height: 80vw; background: #5f72bd; top: -20%; left: -20%; animation-delay: 0s; }
  .orb-s2 { width: 90vw; height: 90vw; background: #9b23ea; bottom: -20%; right: -15%; animation-delay: -4s; }
  .orb-s3 { width: 75vw; height: 75vw; background: #f97794; top: 35%; left: -5%; animation-delay: -11s; }'''

html = html.replace(old_orbs_css, new_orbs_css)

# 3. Calendar Style HTML
old_cal_css = '''  /* ── CALENDAR WIDGET ── */
  .cal-widget {
    background: rgba(40, 30, 40, 0.45);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 28px;
    padding: 24px;
    width: 320px;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255,255,255,0.25);
    color: #fff;
    transform: scale(0.9) translateY(20px);
    opacity: 0;
    transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.8s ease;
    margin-bottom: 30px;
    position: relative;
    z-index: 10;
  }
  .cal-widget.show { transform: scale(1) translateY(0); opacity: 1; }
  
  .cal-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
  .cal-tabs { display: flex; background: rgba(255,255,255,0.1); border-radius: 20px; padding: 3px; font-size: 13px; font-weight: 500; }
  .cal-tab { padding: 6px 16px; border-radius: 16px; color: rgba(255,255,255,0.6); }
  .cal-tab.active { background: #fff; color: #111; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
  .cal-cog { width: 34px; height: 34px; background: rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; }
  
  .cal-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 24px; padding: 0 4px; }
  .cal-month { font-size: 42px; font-weight: 700; letter-spacing: -1px; text-shadow: 0 2px 10px rgba(0,0,0,0.2); }
  .cal-year { font-size: 36px; font-weight: 400; opacity: 0.9; }

  .cal-slider-wrap { position: relative; height: 80px; margin-bottom: 20px; -webkit-mask-image: linear-gradient(90deg, transparent, #000 20%, #000 80%, transparent); }
  .cal-days { display: flex; font-size: 13px; color: rgba(255,255,255,0.5); margin-bottom: 12px; gap: 6px;}
  .cal-days span { width: 38px; text-align: center; }
  
  .cal-dates-window { width: 100%; overflow: hidden; position: relative; height: 44px; }
  .cal-dates-track { display: flex; position: absolute; left: 0; transition: transform 0.05s linear; gap: 6px;}
  .cal-date-item { width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-size: 17px; font-weight: 400; opacity: 0.5; border-radius: 50%; flex-shrink: 0; transition: all 0.3s cubic-bezier(0.34,1.35,0.64,1); }
  .cal-date-item.active { background: linear-gradient(135deg, #ff1a68, #ff8c00); opacity: 1; font-weight: 700; font-size: 19px; box-shadow: 0 4px 15px rgba(255, 26, 104, 0.4); transform: scale(1.15); color: #fff; }
  .cal-date-item.active-glow { animation: cal-glow 1.5s infinite alternate; }
  @keyframes cal-glow { 0% { box-shadow: 0 0 10px rgba(255, 26, 104, 0.4); } 100% { box-shadow: 0 0 25px rgba(255, 26, 104, 0.9); } }

  .cal-bottom { display: flex; justify-content: space-between; align-items: center; padding: 0 4px; }
  .cal-note { font-size: 13px; color: rgba(255,255,255,0.5); display: flex; align-items: center; gap: 6px; }
  .cal-new-event { background: rgba(255,255,255,0.15); padding: 8px 14px; border-radius: 20px; font-size: 13px; font-weight: 500; color: #fff; }'''

new_cal_css = '''  /* ── CALENDAR WIDGET ── */
  .cal-widget {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(35px);
    -webkit-backdrop-filter: blur(35px);
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-top: 1px solid rgba(255, 255, 255, 0.6);
    border-left: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 32px;
    padding: 28px;
    width: 320px;
    box-shadow: 0 25px 45px rgba(0, 0, 0, 0.2), inset 0 0 20px rgba(255, 255, 255, 0.2);
    color: #fff;
    transform: scale(0.9) translateY(20px);
    opacity: 0;
    transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.8s ease;
    margin-bottom: 30px;
    position: relative;
    z-index: 10;
  }
  .cal-widget.show { transform: scale(1) translateY(0); opacity: 1; }
  
  .cal-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
  .cal-tabs { display: flex; background: rgba(255,255,255,0.25); border-radius: 20px; padding: 4px; font-size: 13px; font-weight: 500; }
  .cal-tab { padding: 8px 32px; border-radius: 16px; color: rgba(255,255,255,0.9); }
  .cal-tab.active { background: rgba(255,255,255,0.95); color: #111; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
  .cal-cog { width: 36px; height: 36px; background: rgba(0,0,0,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; box-shadow: inset 0 0 5px rgba(255,255,255,0.3); }
  
  .cal-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 24px; padding: 0 4px; }
  .cal-month { font-size: 42px; font-weight: 700; letter-spacing: -1.5px; text-shadow: 0 2px 10px rgba(0,0,0,0.2); }
  .cal-year { font-size: 36px; font-weight: 300; opacity: 0.85; }

  .cal-slider-wrap { position: relative; height: 80px; margin-bottom: 22px; -webkit-mask-image: linear-gradient(90deg, transparent, #000 20%, #000 80%, transparent); }
  .cal-days { display: flex; font-size: 13px; font-weight: 500; color: rgba(255,255,255,0.75); margin-bottom: 12px; gap: 6px;}
  .cal-days span { width: 38px; text-align: center; }
  
  .cal-dates-window { width: 100%; overflow: hidden; position: relative; height: 44px; }
  .cal-dates-track { display: flex; position: absolute; left: 0; transition: transform 0.05s linear; gap: 6px;}
  .cal-date-item { width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-size: 17px; font-weight: 500; opacity: 0.7; border-radius: 50%; flex-shrink: 0; transition: all 0.3s cubic-bezier(0.34,1.35,0.64,1); }
  .cal-date-item.active { background: linear-gradient(135deg, #ff3366, #ff7b00); opacity: 1; font-weight: 700; font-size: 19px; box-shadow: 0 4px 15px rgba(255, 51, 102, 0.5); transform: scale(1.15); color: #fff; border: 1px solid rgba(255,255,255,0.4); }
  .cal-date-item.active-glow { animation: cal-glow 1.5s infinite alternate; }
  @keyframes cal-glow { 0% { box-shadow: 0 0 10px rgba(255, 51, 102, 0.4); } 100% { box-shadow: 0 0 25px rgba(255, 51, 102, 0.9); } }

  .cal-bottom { display: flex; justify-content: space-between; align-items: center; padding: 0 4px; }
  .cal-note { font-size: 14px; font-weight: 400; color: rgba(255,255,255,0.8); display: flex; align-items: center; gap: 6px; }
  .cal-new-event { background: rgba(255,255,255,0.25); padding: 10px 16px; border-radius: 20px; font-size: 13px; font-weight: 600; color: #fff; box-shadow: inset 0 1px 0 rgba(255,255,255,0.4); }'''

html = html.replace(old_cal_css, new_cal_css)

# 4. Tab HTML Update
old_tabs_html = '''          <div class="cal-tabs">
            <div class="cal-tab active">Weekly</div>
            <div class="cal-tab">Monthly</div>
          </div>'''
          
new_tabs_html = '''          <div class="cal-tabs">
            <div class="cal-tab active">Month</div>
          </div>'''
          
html = html.replace(old_tabs_html, new_tabs_html)

with open('d:/aakansha-surprise/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")

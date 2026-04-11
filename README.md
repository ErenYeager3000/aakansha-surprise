# 🌸 Aakansha Birthday Surprise — Setup Guide

## Files in this folder
```
index.html     ← The entire app (edit this)
manifest.json  ← PWA config
sw.js          ← Offline support
README.md      ← This file
```

---

## ★ Step 1 — Add your videos

Open `index.html` and find these two lines:

**Page 1 mini motion element** (search for `vid1`):
```html
<video id="vid1" src="" autoplay muted loop playsinline>
```
Change `src=""` to your video file path:
```html
<video id="vid1" src="videos/motion.mp4" autoplay muted loop playsinline>
```

**Page 2 full-screen video** (search for `vid2`):
```html
<video id="vid2" src="" muted loop playsinline>
```
Change to:
```html
<video id="vid2" src="videos/main.mp4" muted loop playsinline>
```

Create a `videos/` folder inside this project folder and put your video files there.
Keep each video **under 10MB** — compress with HandBrake or Clideo if needed.

---

## ★ Step 2 — Edit the surprise details

In `index.html`, search for this line and replace it:
```html
<div class="notif-sub">📍 Location &nbsp;·&nbsp; ⏰ Time &nbsp;·&nbsp; 📅 Date</div>
```
Example:
```html
<div class="notif-sub">📍 Café Paloma, MG Road &nbsp;·&nbsp; ⏰ 7:00 PM &nbsp;·&nbsp; 📅 March 25</div>
```

---

## ★ Step 3 — Optional: Add a photo on Page 3

Find this comment in the scratch card section:
```html
<!-- ★ You can replace this div with an <img> tag -->
```
Replace the placeholder div with:
```html
<img src="images/photo.jpg" style="width:100%;height:160px;object-fit:cover;border-radius:20px;">
```

---

## ★ Step 4 — Deploy to Netlify (free, 2 minutes)

1. Go to **netlify.com** and sign up free
2. Drag and drop this **entire project folder** onto the Netlify dashboard
3. Done — you get a live link instantly like `https://random-name.netlify.app`
4. Optional: go to Site Settings → Change site name → set something like `aakansha-surprise`
   Your link becomes: `https://aakansha-surprise.netlify.app`

---

## ★ Step 5 — Send to Aakansha

Send her the link on WhatsApp. She opens it in her phone browser.

**To add to home screen (feels like a real app):**
- iPhone: Safari → Share button → "Add to Home Screen"
- Android: Chrome → ⋮ menu → "Add to Home Screen"

It opens full-screen with no browser bar, like a native app. 🌸

---

## How the app works

| Page | What happens |
|------|-------------|
| Page 1 | She taps the 💌 envelope → mini video plays → button unlocks → goes to Page 2 |
| Page 2 | Blurred video + eye notification + two teasing buttons → tap twice → video unblurs and plays → "Tap to explore what's next" |
| Page 3 | Scratch the gold foil card to reveal the surprise + notification with location/time/date pops in |

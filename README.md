# Parsons Care Finder

**Live site:** https://naiyajaradat.github.io/Parsons-Care-Finder/

A student-built prototype that helps New School students describe a physical or mental health concern and see matching Student Health Services offices, campus support, and student-insurance benefits (Aetna 2026–27 plan), with what each costs.

Not an official New School site. Details were checked 2026-11-24 against newschool.edu and the Aetna brochure; confirm hours and coverage before relying on them.

## Run locally
Open `index.html` in a browser, or serve the folder: `python3 -m http.server` (needed for `events.json` to load).

## Deploy
Push to `main`. In the repo, go to Settings → Pages → Source: **GitHub Actions**. The workflow in `.github/workflows/pages.yml` publishes the site.

## Update content
- **Resources, hours, costs, keywords:** edit the `RES` and `CATS` arrays in `index.html`. Every resource lists its source link.
- **Events:** edit `events.json`. The deploy workflow copies it into `index.html` (`tools/embed_events.py`) so the page still shows events if the file can't be fetched. To preview locally, run that script first.
  Recurring items use `repeat` instead of `start`: `{"days":[1,2,3,4,5],"short":"M–F","label":"Mon–Fri","time":"2:00–3:00 p.m."}`.
  One-off events use `start`. Each event: `title`, `start` (ISO, e.g. `2026-12-03T17:30:00-05:00`), `format`, `place`, `office`, `url` (https), `note`, `cats` (topic ids such as `stress`, `lonely`). Set `updatedAt` to the refresh time. Past events are hidden automatically.

## Privacy
Matching runs in the browser with keywords. Nothing a student types is sent anywhere or stored.

## Crisis numbers
911 · 988 (call or text) · Campus Security 212.229.7001 · SHS 212.229.1671, option 1.

## Brand
Colors follow The New School visual identity page: black, white, and the web-safe Parsons Red `#E42A1D`. The brand typeface (Neue) is proprietary, so the page uses Archivo, which has similar wide and normal widths. No logos or wordmarks are used.

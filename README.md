# Board.Dev — static site

Plain HTML/CSS, no build step. `build.py` is the source of truth for page content: edit it and run `python3 build.py` to regenerate the site.

- Pages are written to `<slug>/index.html` so URLs match the old WordPress permalinks (`/about-us/`, `/what-we-do/` ...). The slug map is `ROUTES` in `build.py`; old URLs that moved are in `REDIRECTS`.
- `assets/img/` — processed images (logo, team headshots, partner logos, resource cards)
- `assets/pdfs/` — downloadable resources
- `_source/` — original uploaded assets (not committed)
- `404.html` — served by GitHub Pages for unknown URLs
- `CNAME` — custom domain (`board.dev`); do not delete

Forms are HubSpot embeds (contact + newsletter). Video thumbnails load from YouTube.

Deploy: GitHub Pages from `main` (root). GoDaddy DNS: four A records for `@` -> 185.199.108.153 / .109.153 / .110.153 / .111.153, CNAME `www` -> board-dev-org.github.io.

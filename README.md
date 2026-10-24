# Board.Dev — static site

Plain HTML/CSS, no build step. `build.py` is the source of truth for page content: edit it and run `python3 build.py` to regenerate the `.html` files.

- `assets/img/` — processed images (logo, team headshots, partner logos, resource cards)
- `assets/pdfs/` — downloadable resources
- `_source/` — original uploaded assets (not committed)

Forms are HubSpot embeds (contact + newsletter). Video thumbnails load from YouTube.

Deploy: GitHub Pages from `main`. Custom domain `board.dev` is enabled by adding a `CNAME` file containing `board.dev` and pointing GoDaddy DNS at GitHub Pages.

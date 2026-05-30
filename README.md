# miguelofbc.github.io

Personal one-page site / HTML CV for **Miguel Oliveira** — Engineering Manager
working on AI-SDLC and agentic test automation, based in Aveiro, Portugal.

Live at **https://miguelofbc.github.io/**

## Architecture

A single, self-contained `index.html`:

- All CSS is inline in a `<style>` block — no build step, no external CSS/JS/fonts.
- Uses the system font stack, so there are no webfont requests.
- Dark mode via `prefers-color-scheme`, plus a print stylesheet (`Cmd/Ctrl-P` → a clean one-page CV).
- `schema.org/Person` JSON-LD and an inline SVG favicon are embedded directly.
- Total page weight is a few KB; the page makes no third-party requests.

## Hosting & deployment

Served by **GitHub Pages** directly from this repository (a user site, so it
publishes to `https://miguelofbc.github.io/`). Pushing to the default branch
deploys automatically — there is no build pipeline.

## Local preview

It's just static HTML, so any of these work:

```bash
# Open directly
xdg-open index.html        # or: open index.html (macOS)

# Or serve locally (recommended, matches real paths)
python3 -m http.server 8000
# then visit http://localhost:8000/
```

## License

See [`LICENSE`](LICENSE) (MIT) — applies to the site's own source.

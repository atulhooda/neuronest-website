# neuronest-website

Website for NeuroNest Pediatric Rehabilitation Centre, Kharadi, Pune.

Static HTML/CSS/JS, no build step. Run locally:

```
python3 -m http.server 5173
```

Then open http://localhost:5173. Client-supplied content and open questions live in `content.md`.

## Therapy pages

The therapies overview (`services/index.html`) and the 15 therapy pages in `services/` are generated. Edit the content in `build.py`, then run:

```
python3 build.py
```

Don't edit `services/*.html` by hand; the next build overwrites them.

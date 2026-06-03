# On the street / Saving the scene / From the forces of / Evil

Anonymized documentation site built with MkDocs + Material theme. Hosted on GitHub Pages.

## Features

- **Dark aesthetic**: Inspired by [joy_division](https://github.com/ghoulmann/joy_division) project
- **404 page**: Interactive Zork I text adventure (MIT-licensed source code)
- **Material Design**: Modern, responsive documentation theme
- **Automated deployment**: GitHub Actions → GitHub Pages

## Build & Deploy

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Build site
mkdocs build

# Serve locally
mkdocs serve
```

Visit `http://localhost:8000` in your browser.

### Deployment

Automatic deployment to GitHub Pages on every push to `master` branch via `.github/workflows/deploy.yml`.

## Content

- **Digital Imaging**: G'MIC online tutorial
- **Virtualization & Cloud**: PVE/Proxmox guides, virtual disk management
- **Essays**: Tech culture, open standards, intellectual freedom
- **Certifications**: AWS Cloud Practitioner notes

## Zork I License

Zork I source code is © Infocom, Inc. and released under the [MIT License](docs/assets/zork/ZORK_LICENSE). 

Source: [historicalsource/zork1](https://github.com/historicalsource/zork1)

## Site Customization

- **Theme config**: `mkdocs.yml`
- **Dark styling**: `docs/assets/css/custom.css` (custom #080808 aesthetic)
- **Content**: Markdown files in `docs/` directory 


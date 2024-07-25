# www.baialupo.com: Blog

```sh
npm create astro@latest -- --template blog
```

[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=0077b6">](https://github.com/SamKirkland/FTP-Deploy-Action)

> 🧑‍🚀 Have fun!

![www.baialupo.com](https://github.com/user-attachments/assets/1519be39-2587-4c02-9702-3d9f695c47d6)

Features:

- ✅ Markdown & MDX support
- ✅ 100/100 Lighthouse performance
- ✅ SEO-friendly with canonical URLs and OpenGraph data

## 🚀 Project Structure

Inside of this project, you'll see the following folders and files:

```text
├───.github
│   └───workflows
├───etl
│   ├───db
│   └───docker
├───public
│   └───img
│       ├───avio
│       ├───covers
│       ├───market
│       └───stories
└───src
    ├───assets
    │   └───images
    │       ├───banner
    │       │   ├───cloud
    │       │   └───header
    │       ├───categories
    │       ├───meteo
    │       └───posts
    ├───components
    ├───content
    │   ├───avio
    │   ├───gallery
    │   ├───market
    │   ├───meteo
    │   ├───posts
    │   │   ├───baialupo
    │   │   ├───guide
    │   │   ├───news
    │   │   └───sicurezza
    │   └───privacy
    ├───icons
    ├───layouts
    ├───pages
    │   ├───aviosuperficie
    │   ├───gallery
    │   ├───market
    │   ├───meteo
    │   └───privacy
    └───styles
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

The `src/content/` directory contains "collections" of related Markdown and MDX documents. Use `getCollection()` to retrieve posts from `src/content/blog/`, and type-check your frontmatter using an optional schema. See [Astro's Content Collections docs](https://docs.astro.build/en/guides/content-collections/) to learn more.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## Resources

- Icons from https://icon-sets.iconify.design
- Image from [pexel.com](https://www.pexels.com/) and [unsplash.com](https://unsplash.com/)

## Backlog

- Create a meteo radar page using windy
- Get TAF from https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/LIML.TXT
- Get Short TAF from https://tgftp.nws.noaa.gov/data/forecasts/shorttaf/stations/LIML.TXT
- Get Metar from https://tgftp.nws.noaa.gov/data/observations/metar/stations/LIML.TXT
- Get Decoded Metar from https://tgftp.nws.noaa.gov/data/observations/metar/decoded/LIML.TXT

### Issue

If any memory issue arise rebuild the project after issuiing the following command:

```
export NODE_OPTIONS=--max_old_space_size=4096
```

# www.baialupo.com: Blog

[![Built with Astro](https://astro.badg.es/v2/built-with-astro/small.svg)](https://astro.build) [<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=0077b6">](https://github.com/SamKirkland/FTP-Deploy-Action) ![Github actions](https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe) ![Google Analytics](https://img.shields.io/badge/Google%20Analytics-E37400?style=for-the-badge&logo=google%20analytics&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) ![MDX](https://img.shields.io/badge/MDX-1B1F24?style=for-the-badge&logo=mdx&logoColor=white) ![pexels](https://img.shields.io/badge/Pexels-05A081?style=for-the-badge&logo=pexels&logoColor=white) ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Prettier](https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white) ![Typesxript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white) ![unsplash](https://img.shields.io/badge/Unsplash-000000?style=for-the-badge&logo=Unsplash&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E) ![Zod](https://img.shields.io/badge/Zod-000000?style=for-the-badge&logo=zod&logoColor=3068B7)

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

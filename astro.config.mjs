import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  compressHTML: true,
  experimental: {
    contentCollectionCache: true
  },
  integrations: [tailwind()],
  markdown: {
    shikiConfig: {
      theme: "none"
    }
  },
  site: 'https://www.baialupo.com',
  trailingSlash: "never"
});
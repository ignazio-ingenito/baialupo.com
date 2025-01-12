import { defineConfig } from 'astro/config';
import icon from "astro-icon";
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  compressHTML: true,
  integrations: [icon(), tailwind()],
  markdown: {
    shikiConfig: {
      theme: "none"
    }
  },
  site: 'https://www.baialupo.com',
  base: '/web',
  trailingSlash: "ignore",
  prefetch: true,
  experimental: {
    clientPrerender: true,
  }
});

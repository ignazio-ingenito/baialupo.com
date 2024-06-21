/** @type {import('tailwindcss').Config} */
// https://themes.ionevolve.com/
// https://coolors.co/palette/ffbe0b-fb5607-ff006e-8338ec-3a86ff

export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	darkMode: 'class',
	theme: {
		screens: {
			"sm": "640px",
			"md": "768px",
			"lg": "1024px",
			"xl": "1280px",
			"2xl": "1536px",
		},
		extend: {
			fontSize: {
				"xs": ".75rem",
				"sm": ".875rem",
				"tiny": ".875rem",
				"base": "0.975rem",
				"lg": "1.125rem",
				"xl": "1.25rem",
				"2xl": "1.5rem",
				"3xl": "1.875rem",
				"4xl": "2.25rem",
				"5xl": "3rem",
				"6xl": "4rem",
				"7xl": "5rem",
			},
		},
		fontFamily: {
			"sans": ["'Encode Sans'", "system-ui", "ui-sans-serif", "sans-serif"],
			"serif": ["'Encode Sans'", "ui-serif", "serif"],
			"mono": ["Incosolata", "ui-monospace", "monospace"],
		},
	},
	plugins: [],
}
/** @type {import('tailwindcss').Config} */
// https://themes.ionevolve.com/
// https://coolors.co/palette/ffbe0b-fb5607-ff006e-8338ec-3a86ff

export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	darkMode: 'class',
	theme: {
		extend: {
			fontSize: {
				"base": "0.975rem",
			},
			fontFamily: {
				"sans": ["'Encode Sans'", "system-ui", "ui-sans-serif", "sans-serif"],
				"serif": ["'Encode Sans'", "ui-serif", "serif"],
				"mono": ["Incosolata", "ui-monospace", "monospace"],
			},
		},
	},
	plugins: [],
}
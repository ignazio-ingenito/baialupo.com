/** @type {import('tailwindcss').Config} */
// https://themes.ionevolve.com/
// https://coolors.co/palette/ffbe0b-fb5607-ff006e-8338ec-3a86ff

export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	darkMode: 'class',
	theme: {
		screens: {
			"xs": "430px",
			"sm": "640px",
			"md": "768px",
			"lg": "1024px",
			"xl": "1280px",
			"2xl": "1536px",
		},
		fontFamily: {
			"sans": ["Prompt", "system-ui", "ui-sans-serif", "sans-serif"],
			"serif": ["Kanit", "ui-serif", "serif"],
			"mono": ["Incosolata", "ui-monospace", "monospace"],
		},
		extend: {},
	},
	plugins: [
		require("@tailwindcss/typography"),
		require('daisyui'),
	],
	daisyui: {
		themes: [
			{
				'dark': {
					'primary': '#00a3ff', // 1
					'primary-focus': '#4dbfff', // 4
					'primary-content': '#b3e3ff', // 8

					'secondary': '#ff006e',
					'secondary-focus': '#f2cb07',
					'secondary-content': '#ffb3d4',

					'accent': '#ffbe0b',
					'accent-focus': '#ffd254',
					'accent-content': '#ffecb6',

					'neutral': '#2a2e37',
					'neutral-focus': '#6a6d73',
					'neutral-content': '#bfc0c3',

					'base-100': '#121c22',
					'base-200': '#2a2e37',
					'base-300': '#16181d',
					'base-content': '#ebecf0',

					'info': '#66c7ff',
					'success': '#87cf3a',
					'warning': '#e1d460',
					'error': '#ff6b6b',

					'--rounded-box': '0.25',
					'--rounded-btn': '.5rem',
					'--rounded-badge': '1.9rem',

					'--animation-btn': '.25s',
					'--animation-input': '.2s',

					'--btn-text-case': 'uppercase',
					'--navbar-padding': '.5rem',
					'--border-btn': '1px',
				},
				'light': {
					'primary': '#00a3ff', // 1
					'primary-focus': '#4dbfff', // 4
					'primary-content': '#b3e3ff', // 8

					'secondary': '#ff006e',
					'secondary-focus': '#f2cb07',
					'secondary-content': '#ffb3d4',

					'accent': '#ffbe0b',
					'accent-focus': '#ffd254',
					'accent-content': '#ffecb6',

					'neutral': '#3b424e',
					'neutral-focus': '#2a2e37',
					'neutral-content': '#cfcfcf',

					'base-100': '#ffffff',
					'base-200': '#f9fafb',
					'base-300': '#ced3d9',
					'base-content': '#1e2734',

					'info': '#1c92f2',
					'success': '#009440',
					'warning': '#ffc800',
					'error': '#ff4b14',

					'--rounded-box': '0.25',
					'--rounded-btn': '.5rem',
					'--rounded-badge': '1.9rem',

					'--animation-btn': '.25s',
					'--animation-input': '.2s',

					'--btn-text-case': 'uppercase',
					'--navbar-padding': '.5rem',
					'--border-btn': '1px',
				},
			},

		],
	},
}

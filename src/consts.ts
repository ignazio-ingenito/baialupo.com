// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE = 'baialupo.com'
export const SITE_DESCRIPTION = 'Aviosuperficie Baialupo | Milano | Italy'
export const MENU_ITEMS = [
    { label: 'Aviosuperficie', path: '/aviosuperficie' },
    {
        label: 'Blog', path: '/blog', childs: [
            { label: 'Baialupo', path: '/blog/baialupo' },
            { label: 'News', path: '/blog/news' },
            { label: 'Sicurezza', path: '/blog/sicurezza' },
        ]
    },
    { label: 'Guide', path: '/blog/guide' },
    { label: 'Mercatino', path: '/blog/mercatino' },
]
// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE: string = 'baialupo.com'
export const SITE_DESCRIPTION: string = 'Aviosuperficie Baialupo | Milano | Italy'
export const CATEGORIES: string[] = ["baialupo", "guide", "mercatino", "news", "sicurezza"]
export const AIRPORT_AW_CODE: string = "AW-317499"

interface MenuItem {
    label: string
    path: string
}

export const MENU_ITEMS: MenuItem[] = [
    { label: 'Aviosuperficie', path: '/aviosuperficie' },
    { label: 'Novità', path: '/posts' },
    { label: 'Gallery', path: '/gallery' },
    { label: 'Mercatino', path: '/mercatino' },
    { label: 'Meteo', path: '/meteo' },
    { label: 'ScuolaVolo', path: 'http://flying.baialupo.com' },
]
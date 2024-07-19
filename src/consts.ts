// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE: string = 'baialupo.com'
export const SITE_DESCRIPTION: string = 'Aviosuperficie Baialupo | Milano | Italy'
export const CATEGORIES: string[] = ["baialupo", "guide", "mercatino", "news", "sicurezza"]
export const AIRPORT_AW_CODE: string = "AW-317499"

interface MenuItem {
    label: string
    path: string
    icon: string
}

export const MENU_ITEMS: MenuItem[] = [
    { label: 'Aviosuperficie', path: '/aviosuperficie', icon: "airplane" },
    { label: 'Blog', path: '/posts', icon: "blog" },
    { label: 'Galleria', path: '/gallery', icon: "gallery" },
    { label: 'Mercatino', path: '/market', icon: "market" },
    { label: 'Meteo', path: '/meteo', icon: "meteo" },
    { label: 'ScuolaVolo', path: 'http://flying.baialupo.com', icon: "school" },
]
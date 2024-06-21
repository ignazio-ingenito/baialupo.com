
export function formatDate(
    date: Date, locales: Intl.LocalesArgument = "it-IT",
    options: Intl.DateTimeFormatOptions = {
        year: "numeric",
        month: "long",
        day: "numeric",
    }) {
    return date.toLocaleDateString(locales, options)
}

export function randomBetween(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1) + min)
}

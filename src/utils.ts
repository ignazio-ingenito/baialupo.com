export function formatDate(
    date: Date | string, locales: Intl.LocalesArgument = "it-IT",
    options: Intl.DateTimeFormatOptions = {
        year: "numeric",
        month: "long",
        day: "numeric",
    }) {
    return (typeof date == "string" ? new Date(date) : date).toLocaleDateString(locales, options)
}

export function randomBetween(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1) + min)
}

export function handleCover(cover: string | undefined, assets: Record<string, () => Promise<{
    default: ImageMetadata
}>>) {
    return (cover != null)
        ? cover
        : assets["/src/content/posts/no-cover.jpg"]()
}

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

export async function getAlbumImages(id: string) {
    // 1. List all album files from collections path
    let images = import.meta.glob<{ default: ImageMetadata }>(
        "/src/content/gallery/**/*.{jpeg,jpg}"
    )

    // 2. Filter images by albumId
    images = Object.fromEntries(
        Object.entries(images).filter(([key]) => key.includes(id))
    )

    // 3. Images are promises, so we need to resolve the glob promises
    const resolvedImages = await Promise.all(
        Object.values(images).map((image) => image().then((mod) => mod.default))
    )

    // 4. Shuffle images in random order
    resolvedImages.sort((a, b) => Math.random() - 0.5)
    return resolvedImages
}
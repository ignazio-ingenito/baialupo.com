
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
    const files = import.meta.glob<{ default: ImageMetadata }>(
        "/src/content/gallery/**/*.{jpeg,jpg,JPEG,JPG,webp,WEBP,png,PNG}"
    )

    // 2. Filter images by albumId
    const images = Object.fromEntries(
        Object.entries(files)
            .filter(([key]) => key.includes(id))
    )

    // 3. Images are promises, so we need to resolve the glob promises
    return await Promise.all(
        Object.values(images).map((image) => image().then((i) => i.default))
    )
}
const AIRPORT_AW_URL: string = `https://server.airportweather.com/api/airports/${AIRPORT_AW_CODE}/weather`

import { AIRPORT_AW_CODE } from "../consts"
import type {
    MetarCoverageDefinition,
    Weather,
    WeatherApiResponse,
} from "./Meteo.d"


function percentageToMetar(value: number): MetarCoverageDefinition | null {
    // SKC (Sky Clear)
    // 1-25% - FEW (Few)
    // 26-50% - SCT (Scattered)
    // 51-87% - BKN (Broken)
    // 88-100% - OVC (Overcast)
    const MetarDefs: MetarCoverageDefinition[] = [
        { min: 0, max: 0, code: "SKC", description: "Sky Clear" },
        { min: 1, max: 25, code: "FEW", description: "Few" },
        { min: 26, max: 50, code: "SCT", description: "Scattered" },
        { min: 51, max: 87, code: "BKN", description: "Broken" },
        { min: 88, max: 100, code: "OVC", description: "Overcast" },
    ]

    return MetarDefs.find((m) => value >= m.min && value <= m.max) || null
}

async function hydrateMeteo(weather: Weather) {
    const {
        nowcast: {
            air_pressure_qnh,
            air_temperature_2m_agl,
            ceiling_agl,
            cloud_cover,
            dew_point_temperature_2m_agl,
            surface_visibility,
            wind_10m_agl,
        },
        next_sunrise,
        next_sunset
    } = weather

    // temperature
    const temp = air_temperature_2m_agl.time_steps[0].quantity
    document.getElementById("temp")!.textContent = temp.value
        ? `${temp.value.toFixed(1)}°C`
        : `${temp.meaning}`
    // dewpoint
    const dewp = dew_point_temperature_2m_agl.time_steps[0].quantity
    document.getElementById("dewpoint")!.textContent = dewp.value
        ? `${dewp.value.toFixed(1)}°C`
        : `${dewp.meaning}`
    // visibility
    const vis = surface_visibility.time_steps[0].quantity
    document.getElementById("visibility")!.textContent = vis.value
        ? `${Math.round(vis.value / 1000)} km`
        : `${vis.meaning}`
    // ceiling
    const ceil = ceiling_agl.time_steps[0].quantity
    document.getElementById("ceiling")!.textContent = ceil.value
        ? `${Math.round(ceil.value * 3.28084)} ft`
        : `${ceil.meaning}`
    // ceiling type
    const clouds = cloud_cover.time_steps[0].quantity
    const ceilType =
        percentageToMetar(clouds.value)?.description.toLowerCase() || ""
    document.getElementById("ceiling-type")!.textContent = ceilType
    // wind
    const { from_direction, speed } = wind_10m_agl.time_steps[0]
    const windDir = from_direction.value
        ? `${Math.round(from_direction.value)}°`
        : from_direction.meaning
    const windSpeed = Math.round(speed.value * 1.94384)
    document.getElementById("wind")!.textContent = `${windDir} ${windSpeed}kt`

    // QNH
    const qnh = air_pressure_qnh.time_steps[0].quantity
    document.getElementById("qnh")!.textContent = vis.value
        ? `${Math.round(qnh.value / 100)} hPa`
        : `${vis.meaning}`

    const sunrise: Date = new Date(next_sunrise.replaceAll(/\[.*/g, ""))
    document.getElementById("sunrise")!.textContent =
        sunrise.toLocaleTimeString("it-IT")

    const sunset: Date = new Date(next_sunset.replaceAll(/\[.*/g, ""))
    document.getElementById("sunset")!.textContent =
        sunset.toLocaleTimeString("it-IT")
}

async function getMeteo(): Promise<WeatherApiResponse> {
    const response = await fetch(AIRPORT_AW_URL)
    return await response.json()
}

async function renderMeteo() {
    const res: WeatherApiResponse = await getMeteo()
    hydrateMeteo(res.weather)
}

document.addEventListener("DOMContentLoaded", async function() {
    await renderMeteo()
})
export interface IMeteo {
    icao: string
    weather: Weather
    isOverAccessLimit: boolean
    canShowKiosk: boolean
}

export interface Offset {
    unit?: string
    value: number
    meaning?: string
}

export interface Timezone {
    name: string
    offset: Offset
}

export interface Weather {
    elevation: Elevation
    icao_id: string
    latitude: Latitude
    longitude: Longitude
    magnetic_declination: MagneticDeclination
    next_sunrise: string
    next_sunset: string
    nowcast: Nowcast
    timezone: Timezone
}

export interface Elevation {
    unit?: string
    value: number
    meaning?: string
}

export interface Latitude {
    unit?: string
    value: number
    meaning?: string
}

export interface Longitude {
    unit?: string
    value: number
    meaning?: string
}

export interface MagneticDeclination {
    unit?: string
    value: number
    meaning?: string
}

export interface Nowcast {
    air_pressure_qnh: AirPressureQnh
    air_temperature_2m_agl: AirTemperature2mAgl
    ceiling_agl: CeilingAgl
    cloud_cover: CloudCover
    dew_point_temperature_2m_agl: DewPointTemperature2mAgl
    flight_rules: FlightRules
    publish_time: string
    surface_visibility: SurfaceVisibility
    synthetic_metar_report: string
    synthetic_taf_report: string
    wind_10m_agl: Wind10mAgl
}

// AirPressureQnh
export interface AirPressureQnhTimeStepQuantity {
    unit?: string
    value: number
    meaning?: string
}

export interface AirPressureQnhTimeStep {
    quantity: AirPressureQnhTimeStepQuantity
    valid_time: string
}

export interface AirPressureQnh {
    time_steps: AirPressureQnhTimeStep[]
}

// AirTemperature2mAgl
export interface AirTemperature2mAglTimeStepQuantity {
    unit?: string
    value: number
    meaning?: string
}

export interface AirTemperature2mAglTimeStep {
    quantity: AirTemperature2mAglTimeStepQuantity
    valid_time: string
}

export interface AirTemperature2mAgl {
    time_steps: AirTemperature2mAglTimeStep[]
}


// CeilingAgl
export interface CeilingAglTimeStepQuantity {
    unit?: string
    value: number
    meaning?: string
}

export interface CeilingAglTimeStep {
    quantity: CeilingAglTimeStepQuantity
    valid_time: string
}

export interface CeilingAgl {
    time_steps: CeilingAglTimeStep[]
}

// CloudCover

export interface CloudCoverTimeStepQuantity {
    unit?: string
    value: number
    meaning?: string
}

export interface CloudCoverTimeStep {
    quantity: CloudCoverTimeStepQuantity
    valid_time: string
}

export interface CloudCover {
    time_steps: CloudCoverTimeStep[]
}

// DewPointTemperature2mAgl

export interface DewPointTemperature2mAglTimeStepQuantity {
    unit?: string
    value: number
    meaning?: string
}

export interface DewPointTemperature2mAglTimeStep {
    quantity: DewPointTemperature2mAglTimeStepQuantity
    valid_time: string
}

export interface DewPointTemperature2mAgl {
    time_steps: DewPointTemperature2mAglTimeStep[]
}

// FlightRules
export interface FlightRulesTimeStepQuantity {
    meaning: string
}

export interface FlightRulesTimeStep {
    quantity: FlightRulesTimeStepQuantity
    valid_time: string
}

export interface FlightRules {
    time_steps: FlightRulesTimeStep[]
}

// SurfaceVisibility
export interface SurfaceVisibilityTimeStepQuantity {
    unit?: string
    value: number
    meaning?: string
}

export interface SurfaceVisibilityTimeStep {
    quantity: SurfaceVisibilityTimeStepQuantity
    valid_time: string
}

export interface SurfaceVisibility {
    time_steps: SurfaceVisibilityTimeStep[]
}

// Wind10mAgl
export interface FromDirection {
    unit?: string
    value: number
    meaning?: string
}

export interface GustSpeed {
    unit?: string
    value: number
    meaning?: string

}

export interface Speed {
    unit?: string
    value: number
    meaning?: string
}

export interface Wind10mAglTimeStep {
    from_direction: FromDirection
    gust_speed: GustSpeed
    speed: Speed
    valid_time: string
}

export interface Wind10mAgl {
    time_steps: Wind10mAglTimeStep[]
}

export type MetarCoverageDefinition = {
    min: number
    max: number
    code: string
    description: string
} 

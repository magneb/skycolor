import asyncio
import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pvlib import atmosphere, irradiance, solarposition, spectrum


def one_day_spectra(date, lat, lon, periods: int = 24):
    """Retrive the sky spectrum for all periods in a day"""
    # Much of the following is pulled from the pvlib irradiance example,
    # and i have little idea what it really means...

    # assumptions
    tilt = 0
    azimuth = 180
    pressure = 101300  # sea level, roughly
    water_vapor_content = 0.5  # cm
    tau500 = 0.1
    ozone = 0.31  # atm-cm
    albedo = 0.2

    next_day = date + datetime.timedelta(days=1)

    times = pd.date_range(start=date, end=next_day, periods=periods, tz="UTC")
    solpos = solarposition.get_solarposition(times, lat, lon)
    aoi = irradiance.aoi(tilt, azimuth, solpos.apparent_zenith, solpos.azimuth)
    relative_airmass = atmosphere.get_relative_airmass(
        solpos.apparent_zenith, model="kastenyoung1989"
    )

    spectra = spectrum.spectrl2(
        apparent_zenith=solpos.apparent_zenith,
        aoi=aoi,
        surface_tilt=tilt,
        ground_albedo=albedo,
        surface_pressure=pressure,
        relative_airmass=relative_airmass,
        precipitable_water=water_vapor_content,
        ozone=ozone,
        aerosol_turbidity_500nm=tau500,
    )
    return spectra


def dates_in_year(year: int):
    """datetime date generator object"""
    y_len = pd.Timestamp(year, 12, 31).dayofyear
    for doy in range(1, y_len + 1):
        yield datetime.datetime.strptime(f"{year}-{doy}", "%Y-%j")


def rgb_wavelengths_in_model(spectra):
    """spectral response definition
    This is where i set wavelength limits (arbitrarially)"""
    cr = np.where(
        (spectra["wavelength"] > 550) & (650 > spectra["wavelength"])
    )[0]
    cg = np.where(
        (spectra["wavelength"] > 500) & (590 > spectra["wavelength"])
    )[0]
    cb = np.where(
        (spectra["wavelength"] > 430) & (480 > spectra["wavelength"])
    )[0]
    return cr, cg, cb


def colors_from_spectra(spectra, periods=24):
    """Assemble rgb colors from a given spectra"""

    model = "poa_sky_diffuse"
    # model = 'poa_global'

    cr, cg, cb = rgb_wavelengths_in_model(spectra)

    r = np.sum(spectra[model][cr[0]: cr[-1], :], axis=0)
    g = np.sum(spectra[model][cg[0]: cg[-1], :], axis=0)
    b = np.sum(spectra[model][cb[0]: cb[-1], :], axis=0)

    red = np.reshape(1.0 * r, (periods,))
    green = np.reshape(1.2 * g, (periods,))
    blue = np.reshape(1.0 * b, (periods,))

    im = np.stack([red.T, green.T, blue.T], axis=1)
    rgb = np.where(np.isnan(im), 0, im)

    return rgb


async def create_stack(year, lat, lon, periods: int = 24):
    """Assemble the red green blue time datacube"""

    async def one_itter(date):
        spectra = one_day_spectra(date, lat, lon, periods=periods)
        rgb = colors_from_spectra(spectra, periods=periods)
        return rgb

    stack = []
    for date in dates_in_year(year):
        stack.append(one_itter(date))
    stack = await asyncio.gather(*stack)
    stack = np.stack(stack, axis=1)
    return stack


if __name__ == "__main__":
    import time

    tic = time.perf_counter()

    YEAR = 2022
    LAT = 60
    LON = 10
    PERIODS = 24 * 4

    data = asyncio.run(create_stack(YEAR, LAT, LON, periods=PERIODS))

    toc = time.perf_counter()

    print(f"Took: {(toc-tic):.02f} Seconds")

    plt.figure()
    plt.imshow(data, origin="lower")
    # plt.yticks([0, 3, 6, 9, 12, 15, 18, 21, 24])
    plt.show()

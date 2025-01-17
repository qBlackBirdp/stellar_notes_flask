# astronomy_utils.py

from datetime import datetime
from skyfield.api import Star
from utils.global_resources import get_timescale, get_ephemeris


def get_constellation_details(constellation_name, date_str):
    ts = get_timescale()
    eph = get_ephemeris()
    t = ts.utc(datetime.strptime(date_str, '%Y-%m-%d'))

    observer = eph['earth']

    # Betelgeuse 별의 예시 위치 사용
    star = Star(ra_hours=22, dec_degrees=-13)
    astrometric = observer.at(t).observe(star)
    ra, dec, distance = astrometric.radec()

    return {
        "name": constellation_name,
        "position": {
            "right_ascension": f"{ra.hours:.2f}h",
            "declination": f"{dec.degrees:.2f}°"
        },
        "distance_from_earth": f"{distance.au:.2f} AU",
    }

# astronomy_utils.py

from skyfield.api import load


def get_star_data(constellation, date):
    ts = load.timescale()
    t = ts.utc(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]))
    eph = load('de421.bsp')
    observer = eph['earth']

    # 별자리 데이터 예시
    star_data = [
        {"name": "Betelgeuse", "pitch": 60, "duration": 480},
        {"name": "Rigel", "pitch": 64, "duration": 240},
        {"name": "Bellatrix", "pitch": 67, "duration": 360},
    ]
    return star_data

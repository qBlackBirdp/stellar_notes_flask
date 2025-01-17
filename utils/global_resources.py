# global_resources.py

from skyfield.api import load

# Skyfield 기본 리소스 로드
EPOCHS = load.timescale()
EPHEMERIS = load('de421.bsp')  # 태양계 기본 데이터


def get_timescale():
    """Skyfield의 TimeScale 객체 반환"""
    return EPOCHS


def get_ephemeris():
    """Skyfield의 Ephemeris 데이터 반환"""
    return EPHEMERIS

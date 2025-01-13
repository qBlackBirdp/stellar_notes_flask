# music.py

from flask import Blueprint, request, jsonify, send_file
from utils.midi_utils import generate_midi
from utils.astronomy_utils import get_star_data

music_bp = Blueprint('music', __name__)


@music_bp.route('/generate', methods=['POST'])
def generate_music():
    data = request.json
    constellation = data.get('constellation', 'Orion')
    date = data.get('date', '2025-01-01')

    try:
        # 별자리 데이터 가져오기
        star_data = get_star_data(constellation, date)

        # MIDI 파일 생성
        midi_path = generate_midi(star_data, constellation)
        return send_file(midi_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

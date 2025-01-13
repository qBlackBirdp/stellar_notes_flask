# app.py

from flask import Flask
from routes.main import main_bp
from routes.music import music_bp


def create_app():
    app = Flask(__name__)

    # Blueprint 등록
    app.register_blueprint(main_bp)
    app.register_blueprint(music_bp, url_prefix='/api/music')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
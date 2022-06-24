from quart import Quart
from hypercorn.config import Config as HyperConfig
from hypercorn.asyncio import serve

from ..settings import Config, DevConfig

from .blueprints.ui import ui_blueprint
from .blueprints.webgui import webgui_blueprint

def build_app():
    app = Quart(__name__)

    app.register_blueprint(webgui_blueprint)
    app.register_blueprint(ui_blueprint, url_prefix='/api/int/')

    if DevConfig().is_dev:
        from quart_cors import cors
        app = cors(app, allow_origin='*')

    return app

async def run_server(app):
    hyper_cfg = HyperConfig()
    hyper_cfg.bind = f'0.0.0.0:{Config().port}'
    return await serve(app, hyper_cfg)

"""Run ChillTyper in a desktop window and bundle it as a standalone EXE."""

from __future__ import annotations

import argparse
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread


APP_NAME = "ChillTyper"
HOST = "127.0.0.1"
PORT = 8765
HTML_NAME = "chilltyper.html"
ICON_NAME = "chilltyper_icon.ico"
SOURCE_DIR = Path(__file__).resolve().parent


def bundled_html_path() -> Path:
    """Return the HTML resource path in source and PyInstaller one-file modes."""
    bundle_dir = getattr(sys, "_MEIPASS", None)
    if getattr(sys, "frozen", False) and bundle_dir:
        return Path(bundle_dir) / HTML_NAME
    return SOURCE_DIR / HTML_NAME


def make_handler(page: bytes) -> type[BaseHTTPRequestHandler]:
    class ChillTyperHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path.partition("?")[0] not in ("/", f"/{HTML_NAME}"):
                self.send_error(404)
                return

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(page)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(page)

        def log_message(self, format: str, *args: object) -> None:
            return

    return ChillTyperHandler


def run_app() -> None:
    html_path = bundled_html_path()
    if not html_path.is_file():
        raise SystemExit(
            f"Nem található a beágyazott alkalmazásfelület: {html_path}\n"
            "Forrásból indítva tedd a chilltyper.html fájlt a Python-fájl mellé, "
            "vagy az alkalmazást a --build-exe kapcsolóval csomagold újra."
        )

    try:
        import webview
    except ModuleNotFoundError as error:
        if error.name == "webview":
            raise SystemExit(
                "A ChillTyper indításához telepítsd a pywebview csomagot:\n"
                "python -m pip install pywebview"
            ) from error
        raise

    page = html_path.read_bytes()
    try:
        server = ThreadingHTTPServer((HOST, PORT), make_handler(page))
    except OSError as error:
        if getattr(error, "winerror", None) == 10048:
            raise SystemExit(
                f"A ChillTyper helyi portja ({PORT}) már használatban van. "
                "Zárd be a másik ChillTyper-példányt, majd próbáld újra."
            ) from error
        raise
    server_thread = Thread(
        target=server.serve_forever,
        kwargs={"poll_interval": 0.2},
        daemon=True,
    )
    url = f"http://{HOST}:{server.server_port}/"

    try:
        server_thread.start()
        webview.create_window(
            "ChillTyper – Magyar QWERTZ vakírás",
            url,
            width=1280,
            height=900,
            min_size=(920, 680),
            background_color="#323437",
        )
        webview.start()
    finally:
        server.shutdown()
        server.server_close()
        server_thread.join()


def build_exe() -> None:
    html_path = SOURCE_DIR / HTML_NAME
    if not html_path.is_file():
        raise SystemExit(f"Az EXE készítéséhez hiányzik a HTML-fájl: {html_path}")

    icon_path = SOURCE_DIR / ICON_NAME
    if not icon_path.is_file():
        raise SystemExit(f"Az EXE ikonjához hiányzik az ikonfájl: {icon_path}")

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--windowed",
        "--name",
        APP_NAME,
        "--icon",
        str(icon_path),
        "--specpath",
        str(SOURCE_DIR / "build"),
        "--workpath",
        str(SOURCE_DIR / "build" / "work"),
        "--distpath",
        str(SOURCE_DIR / "dist"),
        "--add-data",
        f"{html_path};.",
        "--collect-all",
        "webview",
        str(Path(__file__).resolve()),
    ]
    subprocess.run(command, cwd=SOURCE_DIR, check=True)
    print(f"Elkészült: {SOURCE_DIR / 'dist' / f'{APP_NAME}.exe'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="ChillTyper asztali alkalmazás")
    parser.add_argument(
        "--build-exe",
        action="store_true",
        help="Önálló EXE készítése; a HTML-felületet belecsomagolja a fájlba.",
    )
    args = parser.parse_args()
    if args.build_exe:
        build_exe()
    else:
        run_app()


if __name__ == "__main__":
    main()

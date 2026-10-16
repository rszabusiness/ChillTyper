"""Run ChillTyper in a desktop window and bundle it as a standalone EXE."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread


APP_NAME = "ChillTyper"
APP_VERSION = "5.4.7"
HOST = "127.0.0.1"
PORT = 8765
HTML_NAME = "chilltyper.html"
ALT_HTML_NAME = "verseny.html"
ICON_NAME = "chilltyper_icon.ico"
SOURCE_DIR = Path(__file__).resolve().parent
BUNDLED_HTML_NAMES = (HTML_NAME, ALT_HTML_NAME)


def bundled_html_path(html_name: str = HTML_NAME) -> Path:
    """Return the HTML resource path in source and PyInstaller one-file modes."""
    bundle_dir = getattr(sys, "_MEIPASS", None)
    if getattr(sys, "frozen", False) and bundle_dir:
        return Path(bundle_dir) / html_name
    return SOURCE_DIR / html_name


def user_data_path() -> Path:
    """Return a stable per-user directory for WebView cookies and local storage."""
    if sys.platform == "win32":
        base_dir = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
    elif sys.platform == "darwin":
        base_dir = Path.home() / "Library" / "Application Support"
    else:
        base_dir = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share")
    return base_dir / APP_NAME / "webview"


def make_handler(pages: dict[str, bytes]) -> type[BaseHTTPRequestHandler]:
    class ChillTyperHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            requested_path = self.path.partition("?")[0]
            page_name = requested_path.lstrip("/") or HTML_NAME
            page = pages.get(page_name)
            if page is None and requested_path == "/":
                page = pages.get(HTML_NAME)
            if page is None:
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


def run_app(page_name: str = HTML_NAME) -> None:
    page_map: dict[str, bytes] = {}
    for html_name in BUNDLED_HTML_NAMES:
        html_path = bundled_html_path(html_name)
        if not html_path.is_file():
            missing_names = ", ".join(
                f"{name} ({bundled_html_path(name)})" for name in BUNDLED_HTML_NAMES if not bundled_html_path(name).is_file()
            )
            raise SystemExit(
                "Nem található a beágyazott alkalmazásfelület:\n"
                f"{missing_names}\n"
                "Forrásból indítva tedd a chilltyper.html és verseny.html fájlokat a Python-fájl mellé, "
                "vagy az alkalmazást a --build-exe kapcsolóval csomagold újra."
            )
        page_map[html_name] = html_path.read_bytes()

    try:
        import webview
    except ModuleNotFoundError as error:
        if error.name == "webview":
            raise SystemExit(
                "A ChillTyper indításához telepítésd a pywebview csomagot:\n"
                "python -m pip install pywebview"
            ) from error
        raise

    try:
        server = ThreadingHTTPServer((HOST, PORT), make_handler(page_map))
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
    root_path = page_name if page_name in BUNDLED_HTML_NAMES else HTML_NAME
    url = f"http://{HOST}:{server.server_port}/{root_path}"

    try:
        server_thread.start()
        webview.create_window(
            f"{APP_NAME} v{APP_VERSION} – Magyar QWERTZ vakírás",
            url,
            width=1280,
            height=900,
            min_size=(920, 680),
            background_color="#323437",
        )
        webview.start(private_mode=False, storage_path=str(user_data_path()))
    finally:
        server.shutdown()
        server.server_close()
        server_thread.join()


def build_exe() -> None:
    missing_html = [name for name in BUNDLED_HTML_NAMES if not (SOURCE_DIR / name).is_file()]
    if missing_html:
        raise SystemExit(f"Az EXE készítéséhez hiányzik a HTML-fájl(ok): {', '.join(str(SOURCE_DIR / name) for name in missing_html)}")

    icon_path = SOURCE_DIR / ICON_NAME
    if not icon_path.is_file():
        raise SystemExit(f"Az EXE ikonjához hiányzik az ikonfájl: {icon_path}")

    exe_name = f"{APP_NAME}-v{APP_VERSION}"
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--windowed",
        "--name",
        exe_name,
        "--icon",
        str(icon_path),
        "--specpath",
        str(SOURCE_DIR / "build"),
        "--workpath",
        str(SOURCE_DIR / "build" / "work"),
        "--distpath",
        str(SOURCE_DIR / "dist"),
    ]
    for html_name in BUNDLED_HTML_NAMES:
        command.extend(["--add-data", f"{SOURCE_DIR / html_name};."])
    command.extend([
        "--collect-all",
        "webview",
        str(Path(__file__).resolve()),
    ])
    subprocess.run(command, cwd=SOURCE_DIR, check=True)
    print(f"Elkészült: {SOURCE_DIR / 'dist' / f'{exe_name}.exe'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="ChillTyper asztali alkalmazás")
    parser.add_argument(
        "--build-exe",
        action="store_true",
        help="Önálló EXE készítése; a ChillTyper és a Verseny HTML-felületeket belecsomagolja a fájlba.",
    )
    parser.add_argument(
        "--page",
        choices=[HTML_NAME, ALT_HTML_NAME],
        default=HTML_NAME,
        help="Melyik HTML-felület nyíljon meg az appben. A versenyhez használd a verseny.html értéket.",
    )
    args = parser.parse_args()
    if args.build_exe:
        build_exe()
    else:
        run_app(page_name=args.page)


if __name__ == "__main__":
    main()

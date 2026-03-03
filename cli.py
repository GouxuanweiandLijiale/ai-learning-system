import argparse
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
NOTES_DIR = PROJECT_ROOT / "notes"
LOGS_DIR = PROJECT_ROOT / "logs"

def cmd_init_day(date_str: str | None) -> None:
    NOTES_DIR.mkdir(exist_ok=True)
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    day_file = NOTES_DIR / f"{date_str}.md"
    if day_file.exists():
        print(f"[OK] Day file already exists: {day_file}")
        return
    day_file.write_text(
        f"# Day Log: {date_str}\n\n"
        "## 今日目标\n- \n\n"
        "## 今日记录\n- \n\n"
        "## 卡点\n- \n\n",
        encoding="utf-8"
    )
    print(f"[OK] Created: {day_file}")

def cmd_log(message: str) -> None:
    LOGS_DIR.mkdir(exist_ok=True)
    log_file = LOGS_DIR / "study.log"
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write_text("", encoding="utf-8") if not log_file.exists() else None
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"{ts} | {message}\n")
    print(f"[OK] Logged to {log_file}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-learning-system",
        description="StudyOps CLI (Day2 minimal version)"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init-day", help="Create a daily note file in notes/YYYY-MM-DD.md")
    p_init.add_argument("--date", default=None, help="Date in YYYY-MM-DD (default: today)")

    p_log = sub.add_parser("log", help="Append a line to logs/study.log")
    p_log.add_argument("message", help="Message to log")

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init-day":
        cmd_init_day(args.date)
    elif args.command == "log":
        cmd_log(args.message)
    else:
        parser.error("Unknown command")

if __name__ == "__main__":
    main()
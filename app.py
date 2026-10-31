from pathlib import Path
import sqlite3
import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_PATH = Path(__file__).resolve().parent / "cloudtask.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


with get_db() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            day TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            room TEXT NOT NULL
        )
    """)


@app.route("/")
def home():
    with get_db() as conn:
        schedules = conn.execute(
            "SELECT * FROM schedules ORDER BY id DESC"
        ).fetchall()

    return render_template("index.html", schedules=schedules)


@app.route("/schedules/add", methods=["POST"])
def add_schedule():
    subject = request.form.get("subject", "").strip()
    day = request.form.get("day", "").strip()
    start_time = request.form.get("start_time", "").strip()
    end_time = request.form.get("end_time", "").strip()
    room = request.form.get("room", "").strip()

    valid_days = [
        "Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5",
        "Thứ 6", "Thứ 7", "Chủ nhật"
    ]

    if not all([subject, day, start_time, end_time, room]):
        return "Vui lòng nhập đầy đủ thông tin.", 400

    if day not in valid_days:
        return "Thứ học không hợp lệ.", 400

    try:
        from datetime import time
        start = time.fromisoformat(start_time)
        end = time.fromisoformat(end_time)
    except ValueError:
        return "Giờ học không hợp lệ.", 400

    if start >= end:
        return "Giờ kết thúc phải sau giờ bắt đầu.", 400

    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO schedules
                (subject, day, start_time, end_time, room)
            VALUES (?, ?, ?, ?, ?)
            """,
            (subject, day, start_time, end_time, room)
        )

    return redirect(url_for("home"))

@app.route("/schedules/<int:schedule_id>/edit", methods=["GET", "POST"])
def edit_schedule(schedule_id):
    with get_db() as conn:
        schedule = conn.execute(
            "SELECT * FROM schedules WHERE id = ?",
            (schedule_id,)
        ).fetchone()

    if schedule is None:
        return "Không tìm thấy lịch học.", 404

    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        day = request.form.get("day", "").strip()
        start_time = request.form.get("start_time", "").strip()
        end_time = request.form.get("end_time", "").strip()
        room = request.form.get("room", "").strip()

        valid_days = [
            "Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5",
            "Thứ 6", "Thứ 7", "Chủ nhật"
        ]

        if not all([subject, day, start_time, end_time, room]):
            return "Vui lòng nhập đầy đủ thông tin.", 400

        if day not in valid_days:
            return "Thứ học không hợp lệ.", 400

        try:
            from datetime import time
            start = time.fromisoformat(start_time)
            end = time.fromisoformat(end_time)
        except ValueError:
            return "Giờ học không hợp lệ.", 400

        if start >= end:
            return "Giờ kết thúc phải sau giờ bắt đầu.", 400

        with get_db() as conn:
            conn.execute(
                """
                UPDATE schedules
                SET subject = ?, day = ?, start_time = ?,
                    end_time = ?, room = ?
                WHERE id = ?
                """,
                (subject, day, start_time, end_time, room, schedule_id)
            )

        return redirect(url_for("home"))

    return render_template("edit.html", schedule=schedule)


@app.route("/schedules/<int:schedule_id>/delete", methods=["POST"])
def delete_schedule(schedule_id):
    with get_db() as conn:
        result = conn.execute(
            "DELETE FROM schedules WHERE id = ?",
            (schedule_id,)
        )

        if result.rowcount == 0:
            return "Không tìm thấy lịch học.", 404

    return redirect(url_for("home"))
@app.route("/health")
def health():
    return {"status": "ok", "app": "CloudTask"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
    {"app":"CloudTask","status":"ok"}
    
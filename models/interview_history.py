from database.db import mysql


class InterviewHistory:

    @staticmethod
    def save(user_id, score, report):

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            INSERT INTO interview_history
            (user_id, score, report)
            VALUES (%s, %s, %s)
            """,
            (
                user_id,
                score,
                report
            )
        )

        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_history(user_id):

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                score,
                created_at
            FROM interview_history
            WHERE user_id=%s
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        rows = cursor.fetchall()

        cursor.close()

        return rows

    @staticmethod
    def get_report(report_id):

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT report
            FROM interview_history
            WHERE id=%s
            """,
            (report_id,)
        )

        row = cursor.fetchone()

        cursor.close()

        if row:
            return row["report"]

        return None

    @staticmethod
    def delete(report_id):

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            DELETE FROM interview_history
            WHERE id=%s
            """,
            (report_id,)
        )

        mysql.connection.commit()

        cursor.close()
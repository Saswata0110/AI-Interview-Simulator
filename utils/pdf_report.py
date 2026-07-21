from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

import os

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def create_pdf(report_text, filename):

    path = os.path.join(

        REPORT_FOLDER,

        filename

    )

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    story = []

    story.append(

        Paragraph(

            "<b>AI Interview Report</b>",

            styles["Heading1"]

        )

    )

    story.append(

        Paragraph("<br/><br/>", styles["Normal"])

    )

    for line in report_text.split("\n"):

        story.append(

            Paragraph(

                line,

                styles["Normal"]

            )

        )

    doc.build(story)

    return path
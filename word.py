
import win32com.client as win32
from docx import Document
from docx.shared import Pt


doc = Document("template.docx")
#docw=win32.gencache.EnsureDispatch("Word.Application")
#docw.Visible=True


def DOX_GEN(sets,subjects,s_no,q1,q2,q3,q4,q5,q6,q7,q8,q9):
    para=doc.paragraphs
    header = doc.sections[0].header
    for p in header.paragraphs:
        if p.text.strip() in["A","B","C","D","E"]:
            for run in p.runs:
                run.text = sets
                run.font.size=Pt(36)
                run.bold=True
    table = doc.tables[3]

    p = para[1]
    p.text=""
    if p.runs:
        p.runs[0].text = "QUIZ TEST-III"
        p.runs[0].bold = True
    else:
        run = p.add_run("QUIZ TEST-III")
        run.bold = True


    p = para[3]
    p.text=""
    if p.runs:
        p.runs[0].text = "BCA VI Sem. (BCA 61,42,63,64,65)"
        p.runs[0].bold = True
    else:
        run = p.add_run("BCA VI Sem. (BCA 61,42,63,64,65)")
        run.bold = True

    
    p = para[4]
    p.text=""
    if p.runs:
        p.runs[0].text = f"NBCA-{s_no}: {subjects}"
        p.runs[0].bold = True
    else:
        run = p.add_run(f"NBCA-{s_no}: {subjects}")
        run.bold = True

    # Q1
    table.cell(2, 2).text = q1

    # Q2
    table.cell(3, 2).text = q2

    # Q3 main instruction
    table.cell(5, 1).text = "Briefly answer the following parts (a)–(e)."

    # Q3 subparts
    table.cell(6, 3).text = q3
    table.cell(7, 3).text = q4
    table.cell(8, 3).text = q5
    table.cell(9, 3).text = q6
    table.cell(10, 3).text = q7

    # Q4
    table.cell(11, 2).text = q8

    # Q5
    table.cell(12, 2).text = q9

    doc.save(f"{'Quiz_paper'}/question_paper{sets}.docx")

    return "Question paper saved successfully." 
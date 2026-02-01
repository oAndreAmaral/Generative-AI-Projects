import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import os
from langchain_community.document_loaders import PyPDFLoader
from rag_system import ingestion_pdf_to_vectordatabase, retrieval_vectordatabase_to_response

# ------------------------------
# Function to add PDFs to the vector database for context purpose
# ------------------------------
def add_context_files():
    files = filedialog.askopenfilenames(
        title="Select the context files",
        filetypes=[("PDF files", "*.pdf")]
    )
    if files:
        for file_path in files:
            ingestion_pdf_to_vectordatabase(os.path.basename(file_path))
        messagebox.showinfo("OK", f"{len(files)} arquivos adicionados ao vector DB")

# ------------------------------
# Function to generate the report based on the LLM + Context + Query output
# ------------------------------
def generate_report_pdf():

    # Get the file to be analyzed
    target_file = filedialog.askopenfilename(
        title="Select the file to be analyzed",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not target_file:
        return
    
    # Load the file in the LLM understandable format
    loader = PyPDFLoader(target_file)
    target_documents = loader.load()

    # Extract the complete text
    target_text = "\n\n".join([doc.page_content for doc in target_documents])
    
    # Query to provide to the LLM (can be personalised)
    user_question = f"Analyze the following document and provide a detailed report of errors, failing points, and issues:\n\nDocument to Analyze: {target_text}"
    
    # Call the RAG retrieval part to obtain the answer and source
    answer, source_name = retrieval_vectordatabase_to_response(user_question)
    
    # Generates the PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "RAG Auto-Report", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    pdf.multi_cell(0, 6, f"File analised: {os.path.basename(target_file)}")
    pdf.ln(5)
    pdf.multi_cell(0, 6, answer)
    
    # Saves the PDF in the defined folder with te defined name
    out_path = filedialog.asksaveasfilename(
        title="Save the report as PDF",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if out_path:
        pdf.output(out_path)
        messagebox.showinfo("Done", f"PDF Report generated in {out_path}")

# ------------------------------
# Tkinter Interface
# ------------------------------
root = tk.Tk()
root.title("RAG Auto-Report PDF")
root.geometry("450x300")
root.resizable(False, False)
root.configure(bg="#f0f4f8")
root.geometry("450x300")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Frame principal
frame = tk.Frame(root, bg="#f0f4f8", padx=20, pady=20)
frame.pack(expand=True, fill="both")

# Título
title = tk.Label(frame, text="RAG Auto-Report Generator", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#333")
title.pack(pady=(0, 20))

# Botões estilizados
btn_style = {"font": ("Helvetica", 12), "width": 35, "bd": 2, "relief": "ridge", "bg": "#4a90e2", "fg": "white", "activebackground": "#357ABD"}

tk.Button(root, text="Add PDFs for context", command=add_context_files).pack(pady=10)
tk.Button(root, text="Select the PDF to be analyzed and the final report name", command=generate_report_pdf).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()

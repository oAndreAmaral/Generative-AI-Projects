import sys
import os

# Adiciona a pasta superior ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_system import ingestion_pdf_to_vectordatabase, retrieval_vectordatabase_to_response

#ingestion_pdf_to_vectordatabase("Indian_financial_system.pdf")

# Teste 1: Pergunta dentro do domínio (com contexto)
question_with_context = "Explique os principais fundamentos do sistema indiano financeiro"
answer, sources = retrieval_vectordatabase_to_response(question_with_context)
print("=== Teste com contexto ===")
print("Answer:", answer)
print("Sources:", sources)
print()

# Teste 2: Pergunta fora do domínio (sem contexto)
question_no_context = "Qual é a capital da Mongólia?"
answer, sources = retrieval_vectordatabase_to_response(question_no_context)
print("=== Teste sem contexto ===")
print("Answer:", answer)
print("Sources:", sources)

# Teste 1: Pergunta dentro do domínio (com contexto)
question_with_context = "Sistema financeiro indiano vs portugues"
answer, sources = retrieval_vectordatabase_to_response(question_with_context)
print("=== Teste com contexto ===")
print("Answer:", answer)
print("Sources:", sources)
print()

import openai

# Pega aquí tu llave API de OpenAI
openai.api_key = "TU_API_KEY"

# Función para resolver problemas
def resolver_problema(pregunta):
    contexto = """
    Soy un asistente que resuelve problemas. Por ejemplo:
    - "He recibido una multa por exceso de velocidad, ¿cómo puedo recurrirla?" -> "Para recurrir una multa por exceso de velocidad, debes presentar un recurso administrativo..."
    - "Compré un producto defectuoso, ¿cómo puedo reclamar?" -> "Tienes derecho a reclamar la reparación, sustitución, rebaja del precio o resolución del contrato..."
    - "¿Cuántos días de vacaciones me corresponden por ley?" -> "Te corresponden 30 días naturales de vacaciones al año..."
    """
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=contexto + "\nPregunta del usuario: " + pregunta,
        max_tokens=150
    )
    return respuesta["choices"][0]["text"]

# Prueba del sistema
pregunta_usuario = input("Escribe tu pregunta: ")
respuesta = resolver_problema(pregunta_usuario)
print("\nRespuesta del GPT: " + respuesta)


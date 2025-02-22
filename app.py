from flask import Flask, request, redirect
import secrets

app = Flask(__name__)

# Paso 1: Configuración inicial
CLIENT_ID = "YOUR_CLIENT_ID"  # Reemplaza con tu client_id real
REDIRECT_URI = "https://your-ngrok-url.ngrok-free.app/callback"  # URL de ngrok

@app.route("/")
def home():
    """
    Página principal que redirige al vendedor a Amazon para autorización.
    """
    # Generar un valor único para 'state' en cada solicitud
    state = secrets.token_urlsafe(16)
    
    # Construir la URL de autorización dinámicamente
    auth_url = (
        f"https://sellercentral.amazon.com/apps/authorize/consent?"
        f"application_id={CLIENT_ID}&"
        f"state={state}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"version=beta"
    )
    
    # Redirigir al usuario a la URL de autorización
    return redirect(auth_url)

@app.route("/callback")
def callback():
    """
    Endpoint de callback que recibe el authorization_code y lo muestra en pantalla.
    """
    authorization_code = request.args.get("code")
    if not authorization_code:
        return "Error: No se recibió el código de autorización.", 400
    
    return f"""
    <h1>Código de Autorización</h1>
    <p>Copia el siguiente código y úsalo en tu aplicación:</p>
    <pre>{authorization_code}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
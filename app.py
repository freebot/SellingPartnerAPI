from flask import Flask, request, redirect

app = Flask(__name__)

# Paso 1: Configuración inicial
CLIENT_ID = "YOUR_CLIENT_ID"  # Reemplaza con tu client_id real
REDIRECT_URI = "https://your-ngrok-url.ngrok-free.app/callback"  # URL de ngrok
AUTH_URL = (
    f"https://sellercentral.amazon.com/apps/authorize/consent?"
    f"application_id={CLIENT_ID}&"
    f"state=UNIQUE_STATE_VALUE&"
    f"version=beta"
)

@app.route("/")
def home():
    """
    Página principal que redirige al vendedor a Amazon para autorización.
    """
    return redirect(AUTH_URL)

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
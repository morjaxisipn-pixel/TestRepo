import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import base64

print("\n" + "=" * 60)
print("🛞 GENERADOR DE QR - VULCANIZADORA CHAVALO")
print("=" * 60 + "\n")

# PASO 1: Crear imagen
print("PASO 1/3: Creando imagen del logo...")
try:
    ancho, alto = 1200, 800
    img = Image.new('RGB', (ancho, alto), 'white')
    draw = ImageDraw.Draw(img)
    
    naranja = '#ff6b35'
    
    # Fondo naranja
    draw.rectangle([(0, 0), (ancho, 200)], fill=naranja)
    
    # Texto
    try:
        font_grande = ImageFont.truetype("arialbd.ttf", 80)
        font_mediana = ImageFont.truetype("arial.ttf", 50)
        font_pequena = ImageFont.truetype("arial.ttf", 40)
    except:
        font_grande = ImageFont.load_default()
        font_mediana = ImageFont.load_default()
        font_pequena = ImageFont.load_default()
    
    draw.text((300, 60), "VULCANIZADORA CHAVALO", fill='white', font=font_grande)
    draw.text((450, 150), "Tuxpan, Veracruz", fill='white', font=font_mediana)
    
    y = 280
    draw.text((100, y), "▶ Mercado Pago", fill=naranja, font=font_mediana)
    y += 70
    draw.text((150, y), "722 969 010 862 117 414", fill='#333', font=font_mediana)
    y += 60
    draw.text((150, y), "Marco Antonio Morales S.", fill='#666', font=font_pequena)
    
    y += 100
    draw.text((100, y), "▶ Banco Azteca", fill=naranja, font=font_mediana)
    y += 70
    draw.text((150, y), "5263 5401 3321 6628", fill='#333', font=font_mediana)
    y += 60
    draw.text((150, y), "CLABE: 1279 0301 3098 3090 52", fill='#666', font=font_pequena)
    
    img.save("logo_chavalo.png")
    print("   ✅ logo_chavalo.png creado\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")
    exit()

# PASO 2: Crear HTML
print("PASO 2/3: Creando página HTML...")
try:
    with open("logo_chavalo.png", "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode('utf-8')
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CHAVALO - Pago</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: Arial;
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height: 100vh;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .container {{
            background: white;
            border-radius: 20px;
            max-width: 800px;
            width: 100%;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b35, #f7931e);
            padding: 40px;
            text-align: center;
            color: white;
        }}
        .logo-container {{
            text-align: center;
            padding: 30px;
            background: #f5f5f5;
        }}
        .logo-container img {{
            max-width: 100%;
            border-radius: 15px;
        }}
        .payment {{ padding: 30px; }}
        .section {{
            background: #f9f9f9;
            padding: 25px;
            margin: 20px 0;
            border-radius: 15px;
            border-left: 5px solid #ff6b35;
        }}
        .section h2 {{ color: #ff6b35; margin-bottom: 15px; }}
        .row {{
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            cursor: pointer;
        }}
        .row:hover {{ transform: translateX(5px); }}
        .label {{ font-weight: bold; color: #555; }}
        .value {{ font-family: 'Courier New'; font-size: 1.1em; }}
        .btn {{
            background: #ff6b35;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 8px;
            cursor: pointer;
        }}
        .notif {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #4CAF50;
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            display: none;
        }}
        .footer {{ background: #333; color: white; text-align: center; padding: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛞 VULCANIZADORA CHAVALO</h1>
            <p>Tuxpan, Veracruz</p>
        </div>
        <div class="logo-container">
            <img src="data:image/png;base64,{img_base64}">
        </div>
        <div class="payment">
            <div class="section">
                <h2>Mercado Pago</h2>
                <div class="row" onclick="cp('722969010862117414',this)">
                    <span class="label">Número:</span>
                    <span class="value">722 969 010 862 117 414</span>
                    <button class="btn">📋</button>
                </div>
                <div class="row" onclick="cp('Marco Antonio Morales S.',this)">
                    <span class="label">Titular:</span>
                    <span class="value">Marco Antonio Morales S.</span>
                    <button class="btn">📋</button>
                </div>
            </div>
            <div class="section">
                <h2>Banco Azteca</h2>
                <div class="row" onclick="cp('5263540133216628',this)">
                    <span class="label">Cuenta:</span>
                    <span class="value">5263 5401 3321 6628</span>
                    <button class="btn">📋</button>
                </div>
                <div class="row" onclick="cp('127903013098309052',this)">
                    <span class="label">CLABE:</span>
                    <span class="value">1279 0301 3098 3090 52</span>
                    <button class="btn">📋</button>
                </div>
                <div class="row" onclick="cp('Marco Antonio Morales S.',this)">
                    <span class="label">Titular:</span>
                    <span class="value">Marco Antonio Morales S.</span>
                    <button class="btn">📋</button>
                </div>
            </div>
        </div>
        <div class="footer">✅ Toca para copiar</div>
    </div>
    <div class="notif" id="n">Copiado ✅</div>
    <script>
        function cp(t,e){{
            navigator.clipboard.writeText(t);
            document.getElementById('n').style.display='block';
            e.style.background='#d4edda';
            setTimeout(()=>{{
                document.getElementById('n').style.display='none';
                e.style.background='white';
            }},2000);
        }}
    </script>
</body>
</html>"""
    
    with open("info_pago_chavalo.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print("   ✅ info_pago_chavalo.html creado\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")
    exit()

# PASO 3: Crear QR
print("PASO 3/3: Creando código QR...")
try:
    ruta = os.path.abspath("info_pago_chavalo.html").replace(os.sep, '/')
    url = f"file:///{ruta}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#ff6b35", back_color="white")
    img.save("qr_chavalo.png")
    print("   ✅ qr_chavalo.png creado\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")
    exit()

# RESUMEN
print("=" * 60)
print("✅ ¡COMPLETADO CON ÉXITO!")
print("=" * 60 + "\n")
print("📁 Archivos creados en:")
print(f"   {os.getcwd()}\n")
print("📄 Archivos:")
print("   1. info_pago_chavalo.html (página web)")
print("   2. qr_chavalo.png (código QR)")
print("   3. logo_chavalo.png (imagen con datos)\n")
print("🎯 SIGUIENTE PASO:")
print("   Abre 'info_pago_chavalo.html' en tu navegador\n")
print("=" * 60 + "\n")

input("Presiona Enter para abrir el HTML en el navegador...")
os.system("start info_pago_chavalo.html")
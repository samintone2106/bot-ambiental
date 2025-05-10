import discord
from discord.ext import commands
import random

# Token del bot (asegúrate de mantenerlo seguro)
TOKEN = 'token aqui'

# Intents necesarios para el bot
intents = discord.Intents.default()
intents.message_content = True

# Configuración del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Consejos ecológicos
tips = [
    "Usa transporte público, bicicleta o camina en lugar de usar el coche.",
    "Recicla y reutiliza siempre que sea posible.",
    "Reduce el uso de plásticos de un solo uso.",
    "Apaga las luces y desconecta los aparatos electrónicos cuando no los uses.",
    "Planta árboles o apoya iniciativas de reforestación.",
    "Evita desperdiciar agua y energía.",
    "Compra productos locales para reducir la huella de carbono.",
    "Participa en limpiezas comunitarias de tu entorno.",
    "Usa bolsas reutilizables en lugar de bolsas de plástico.",
    "Educa a otros sobre la importancia de cuidar el medio ambiente."
]

# Retos ecológicos
retos = [
    "♻️ Hoy, intenta no usar ningún plástico de un solo uso.",
    "🚶‍♂️ Camina o usa bici en lugar del auto al menos una vez.",
    "🌱 Planta algo: una planta, una semilla o cuida de una que ya tengas.",
    "🔌 Desconecta todos los aparatos electrónicos que no uses al final del día.",
    "🛒 Compra local: elige productos de tu zona para reducir transporte."
]

# Recursos recomendados
recursos = [
    "🎬 *Nuestro Planeta* (Netflix) – Documental sobre biodiversidad y cambio climático.",
    "📘 *Zero Waste Home* de Bea Johnson – Guía para vivir con menos residuos.",
    "🌐 https://www.wwf.org – Sitio con consejos y noticias sobre el medio ambiente.",
]

# Preguntas tipo trivia
preguntas = [
    ("¿Cuál de estos materiales tarda más en degradarse?\nA) Plástico\nB) Papel\nC) Cáscara de banana", "A"),
    ("¿Qué gas emiten en exceso los autos que contribuye al calentamiento global?\nA) Oxígeno\nB) Dióxido de carbono\nC) Hidrógeno", "B"),
]

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def consejo(ctx):
    """Envía un consejo aleatorio contra la contaminación."""
    await ctx.send(f'🌱 {random.choice(tips)}')

@bot.command()
async def info(ctx):
    """Proporciona información sobre el propósito del bot."""
    await ctx.send(
        "🌍 Hola, soy un bot que comparte consejos para combatir la contaminación. "
        "Usa `!consejo`, `!reto`, `!ecoquiz` o `!recurso` para aprender más."
    )

@bot.command()
async def reto(ctx):
    """Envía un reto ecológico para hoy."""
    await ctx.send(f'💪 {random.choice(retos)}')

@bot.command()
async def recurso(ctx):
    """Recomienda un recurso ecológico (libro, web o documental)."""
    await ctx.send(f'📚 {random.choice(recursos)}')

@bot.command()
async def ecoquiz(ctx):
    """Pregunta ecológica al azar."""
    pregunta, respuesta = random.choice(preguntas)
    await ctx.send(f"🌍 Quiz ecológico:\n{pregunta}\n(Responde con A, B o C)")

    def check(m):
        return m.author == ctx.author and m.content.upper() in ["A", "B", "C"]

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        if msg.content.upper() == respuesta:
            await ctx.send("✅ ¡Correcto!")
        else:
            await ctx.send(f"❌ Incorrecto. La respuesta correcta era {respuesta}.")
    except:
        await ctx.send("⏰ ¡Tiempo agotado!")

@bot.command()
async def ecoidea(ctx):
    """Envía una idea ecológica."""
    ideas = [
        "🌿 Cambia a shampoo y jabón en barra para evitar botellas plásticas.",
        "🚰 Instala un filtro y evita comprar agua embotellada.",
        "🛍️ Lleva tu propia bolsa de tela cada vez que vayas de compras.",
        "🧼 Usa productos de limpieza ecológicos o caseros.",
        "📦 Reutiliza cajas y frascos en lugar de desecharlos."
    ]
    await ctx.send(random.choice(ideas))

@bot.command()
async def reutiliza(ctx):
    """Envía un consejo para reutilizar objetos."""
    consejos = [
        "🧴 Un frasco de vidrio puede ser un florero, lapicero o recipiente de cocina.",
        "👕 Camisetas viejas pueden transformarse en bolsas o trapos.",
        "📦 Cajas de cartón sirven para organizar cosas en casa.",
        "📰 Usa papel viejo para envolver regalos o hacer manualidades.",
        "☕ Latas vacías pueden decorarse como macetas pequeñas."
    ]
    await ctx.send(random.choice(consejos))

@bot.command()
async def estadisticas(ctx):
    """Envía datos impactantes sobre el medio ambiente."""
    datos = [
        "📉 Solo el 9% del plástico producido en el mundo se recicla.",
        "🌊 Cada año, se vierten más de 8 millones de toneladas de plástico en los océanos.",
        "🚿 Una ducha de 10 minutos puede gastar hasta 200 litros de agua.",
        "🌳 Se pierden 10 millones de hectáreas de bosque cada año.",
        "🐢 Más de 1 millón de animales marinos mueren cada año por plástico."
    ]
    await ctx.send(random.choice(datos))

@bot.command()
async def botellasalvadas(ctx, dias: int = 1):
    """Calcula cuántas botellas plásticas se han salvado usando una reutilizable."""
    botellas = dias  # 1 botella por día como ejemplo
    await ctx.send(f"👏 ¡Has salvado aproximadamente {botellas} botellas plásticas en {dias} día(s) usando una reutilizable!")

@bot.command()
async def ecoemoji(ctx, accion: str):
    """Envía un emoji relacionado con una acción ecológica."""
    acciones = {
        "bicicleta": "🚴",
        "reutilizar": "🔁",
        "plantar": "🌱",
        "ahorraragua": "🚿",
        "energiasolar": "🌞",
        "reciclar": "♻️"
    }
    emoji = acciones.get(accion.lower(), "❓ Acción no reconocida. Prueba: bicicleta, reutilizar, plantar, ahorraragua, energiasolar, reciclar.")
    await ctx.send(emoji)

# Ejecuta el bot
bot.run(TOKEN)

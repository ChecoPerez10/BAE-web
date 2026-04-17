from django.shortcuts import render


def inicio(request):
    """Vista de la pagina de inicio."""
    contexto = {
        'titulo': 'JumpRush - Endless Runner Game',
        'descripcion': 'Un emocionante endless runner 2D con estetica pixel art',
        'juego': {
            'nombre': 'JumpRush',
            'descripcion': '',
            'genero': 'Sepa la bola',
            'estado': 'En desarrollo',
        },
        'escenarios': [
            {
                'id': 'bosque',
                'nombre': 'Bosque Encantado',
                'imagen': 'images/escenario1.jpeg',
                'descripcion': 'Un frondoso bosque lleno de arboles gigantes, flores coloridas y criaturas magicas. Corre entre la naturaleza mientras esquivas raices y saltas sobre troncos caidos.',
                'dificultad': 'Facil',
                'monedas_bonus': '+10%',
            },
            {
                'id': 'desierto',
                'nombre': 'Desierto Ancestral',
                'imagen': 'images/escenario2.jpeg',
                'descripcion': 'Arenas doradas bajo un sol abrasador. Piramides antiguas guardan secretos mientras esquivas cactus y tormentas de arena en este desafiante escenario.',
                'dificultad': 'Media',
                'monedas_bonus': '+25%',
            },
            {
                'id': 'ciudad',
                'nombre': 'Ciudad Neon',
                'imagen': 'images/escenario3.jpeg',
                'descripcion': 'Una metropolis futurista iluminada con luces de neon. Salta entre edificios, esquiva vehiculos voladores y recorre las calles de esta ciudad cyberpunk.',
                'dificultad': 'Dificil',
                'monedas_bonus': '+50%',
            },
        ],
        'personajes': [
            {
                'id': 'aventurero',
                'nombre': 'Max el Aventurero',
                'imagen': 'images/player1.gif',
                'descripcion': 'Un valiente explorador con sed de aventuras. Su agilidad y determinacion lo hacen perfecto para cualquier desafio.',
                'velocidad': 3,
                'salto': 4,
                'resistencia': 3,
                'habilidad': 'Doble Salto',
            },
            {
                'id': 'ninja',
                'nombre': 'Kira la Ninja',
                'imagen': 'images/player2.gif',
                'descripcion': 'Una guerrera sigilosa entrenada en las artes ninja. Su velocidad es incomparable y puede deslizarse bajo obstaculos.',
                'velocidad': 5,
                'salto': 3,
                'resistencia': 2,
                'habilidad': 'Dash Veloz',
            },
            {
                'id': 'robot',
                'nombre': 'R0-B0 el Robot',
                'imagen': 'images/player3.gif',
                'descripcion': 'Un robot amigable con tecnologia avanzada. Su resistencia superior le permite absorber golpes y seguir adelante.',
                'velocidad': 2,
                'salto': 3,
                'resistencia': 5,
                'habilidad': 'Escudo Energia',
            },
        ],
        'armas': [
            {
                'id': 'espada',
                'nombre': 'Espada de Luz',
                'imagen': 'images/arma1.png',
                'descripcion': 'Una espada legendaria forjada con energia pura. Capaz de cortar cualquier obstaculo en tu camino.',
                'dano': 4,
                'alcance': 2,
                'velocidad': 3,
                'habilidad': 'Corte Luminoso',
            },
            {
                'id': 'arco',
                'nombre': 'Arco Elemental',
                'imagen': 'images/arma2.png',
                'descripcion': 'Un arco magico que dispara flechas de diferentes elementos. Perfecto para ataques a distancia.',
                'dano': 3,
                'alcance': 5,
                'velocidad': 4,
                'habilidad': 'Flecha Multiple',
            },
            {
                'id': 'baston',
                'nombre': 'Baston Arcano',
                'imagen': 'images/arma3.png',
                'descripcion': 'Un baston canalizado con magia antigua. Lanza hechizos devastadores contra los enemigos.',
                'dano': 5,
                'alcance': 4,
                'velocidad': 2,
                'habilidad': 'Explosion Magica',
            },
        ],
        'enemigos': [
            {
                'id': 'slime',
                'nombre': 'Slime Venenoso',
                'imagen': 'images/drone1.gif',
                'descripcion': 'Una criatura gelatinosa que deja rastros de veneno. Facil de vencer pero aparece en grandes cantidades.',
                'vida': 2,
                'dano': 1,
                'velocidad': 2,
                'tipo': 'Comun',
            },
            {
                'id': 'esqueleto',
                'nombre': 'Esqueleto Guardian',
                'imagen': 'images/drone2.gif',
                'descripcion': 'Un guerrero no-muerto que protege tesoros antiguos. Ataca con precision y es dificil de esquivar.',
                'vida': 4,
                'dano': 3,
                'velocidad': 3,
                'tipo': 'Elite',
            },
            {
                'id': 'dragon',
                'nombre': 'Dragon de Sombra',
                'imagen': 'images/drone3.gif',
                'descripcion': 'El jefe final de cada mundo. Un dragon colosal que escupe fuego oscuro y tiene ataques devastadores.',
                'vida': 5,
                'dano': 5,
                'velocidad': 4,
                'tipo': 'Jefe',
            },
        ],
        'equipo': [
            {
                'nombre': 'Rodrigo Alcaraz Alvarez',
                'rol': 'Full Stack Developer',
                'descripcion': 'Desarrollo web y backend',
            },
            {
                'nombre': 'Erik Eduardo Vital Corona',
                'rol': 'Game Developer',
                'descripcion': 'Mecanicas y logica del juego',
            },
            {
                'nombre': 'Berenice Jazmin Antonio Leiva',
                'rol': 'Backend Developer',
                'descripcion': 'APIs y base de datos',
            },
            {
                'nombre': 'Adela Olivos Cuesta ',
                'rol': 'Frontend Developer',
                'descripcion': 'Interfaces y experiencia de usuario',
            },
        ],
    }
    return render(request, 'inicio.html', contexto)


def nosotros(request):
    """Vista de la pagina Nosotros."""
    return render(request, 'nosotros.html')


def escenarios(request):
    """Vista de la pagina de Escenarios."""
    return render(request, 'escenarios.html')


def personajes(request):
    """Vista de la pagina de Personajes."""
    return render(request, 'personajes.html')


def contacto(request):
    """Vista de la pagina de Contacto."""
    return render(request, 'contacto.html')

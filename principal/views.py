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
                'nombre': 'Sector Perdido',
                'imagen': 'images/escenario1.jpeg',
                'descripcion': 'Una antigua zona industrial donde todo comenzó a fallar. Las máquinas quedaron fuera de control y los drones patrullan sin descanso, atacando a cualquiera que entre. Entre estructuras abandonadas y sistemas inestables, este lugar guarda las primeras pistas de lo que salió mal.',
                'dificultad': 'Facil',
                'monedas_bonus': '+10%',
            },
            {
                'id': 'desierto',
                'nombre': 'Ciudad Silenciosa',
                'imagen': 'images/escenario2.jpeg',
                'descripcion': 'Lo que antes fue una ciudad activa ahora permanece en completo silencio. No hay señales de vida… solo drones vigilando cada rincón y reaccionando ante cualquier movimiento. Las calles ocultan secretos, y cada paso te acerca a una verdad que alguien —o algo— intenta mantener oculta.',
                'dificultad': 'Media',
                'monedas_bonus': '+25%',
            },
            {
                'id': 'ciudad',
                'nombre': 'El Núcleo',
                'imagen': 'images/escenario3.jpeg',
                'descripcion': 'En lo más profundo del sistema se encuentra el origen de todo. Aquí, las máquinas operan con un propósito desconocido, protegiendo el corazón que las controla. Cada enfrentamiento es más intenso, y solo avanzando podrás descubrir qué está realmente detrás de esta amenaza.',
                'dificultad': 'Dificil',
                'monedas_bonus': '+50%',
            },
        ],
        'personajes': [
            {
                'id': 'aventurero',
                'nombre': 'Max el Aventurero',
                'imagen': 'images/player1.png',
                'descripcion': 'Un valiente explorador con sed de aventuras. Su agilidad y determinacion lo hacen perfecto para cualquier desafio.',
                'velocidad': 3,
                'salto': 4,
                'resistencia': 3,
                'habilidad': 'Doble Salto',
            },
            {
                'id': 'ninja',
                'nombre': 'Kira la Ninja',
                'imagen': 'images/player2.png',
                'descripcion': 'Una guerrera sigilosa entrenada en las artes ninja. Su velocidad es incomparable y puede deslizarse bajo obstaculos.',
                'velocidad': 5,
                'salto': 3,
                'resistencia': 2,
                'habilidad': 'Dash Veloz',
            },
            {
                'id': 'robot',
                'nombre': 'R0-B0 el Robot',
                'imagen': 'images/player3.png',
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
                'imagen': 'images/Drone1_hover.gif',
                'descripcion': 'Una criatura gelatinosa que deja rastros de veneno. Facil de vencer pero aparece en grandes cantidades.',
                'vida': 2,
                'dano': 1,
                'velocidad': 2,
                'tipo': 'Comun',
            },
            {
                'id': 'esqueleto',
                'nombre': 'Esqueleto Guardian',
                'imagen': 'images/Drone2_hover.gif',
                'descripcion': 'Un guerrero no-muerto que protege tesoros antiguos. Ataca con precision y es dificil de esquivar.',
                'vida': 4,
                'dano': 3,
                'velocidad': 3,
                'tipo': 'Elite',
            },
            {
                'id': 'dragon',
                'nombre': 'Dragon de Sombra',
                'imagen': 'images/Drone3_hover.gif',
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

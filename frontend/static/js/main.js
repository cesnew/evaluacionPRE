// Obtener el elemento del navbar
const navbar = document.querySelector('.university-header');

// Función para manejar el scroll
function handleScroll() {
    // Obtener la posición vertical actual de la página
    const scrollY = window.scrollY;

    // Determinar si el usuario ha desplazado la página hacia abajo
    if (scrollY > 0) {
        navbar.style.position = 'fixed';
        navbar.style.top = '0';
    } else {
        // Si el usuario está en la parte superior de la página, restaurar el estilo original
        navbar.style.position = 'static';
    }
}

// Escuchar el evento scroll para activar la función handleScroll
window.addEventListener('scroll', handleScroll);

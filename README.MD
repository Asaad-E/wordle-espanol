# Wordle en Español

<video width="320" height="320" controls style='margin-top:' src="https://github.com/Asaad-E/wordle-espanol/blob/main/media/test.mp4">
</video>

**Descripción:**

Una implementación del popular juego Wordle en español, desarrollado con HTML, CSS y JavaScript. El objetivo es adivinar una palabra de cinco letras en seis intentos o menos.

## Características

- 🎨 Sistema intuitivo de pistas por colores:
  - 🟩 Verde: Letra correcta en posición correcta
  - 🟨 Amarillo: Letra correcta en posición incorrecta
  - ⬜ Gris: Letra no está en la palabra
- 🎲 Palabras aleatorias del español más común
- 🌓 Modo oscuro/claro automático y manual
- ⌨️ Soporte completo para teclado físico
- 📊 Estadísticas detalladas de tu progreso
- 📱 Diseño responsivo para todos los dispositivos

## Cómo jugar

Puedes probar rapidamente la [versión online](link-to-game).

### Instalación local

Puedes tambien crear una copia local del proyecto para poder modicarlo.

```bash
git clone https://github.com/Asaad-E/wordle-espanol.git
```

## Origen de los datos

Las palabras más usadas del español se obtuvieron de la pagina de la [Real Academia Española](link).

El proceso de filtrado se realizó con el script de Python ubicado en la carpeta `data`.

Este script genera el archivo `words_data.js` que contiene todas las palabras de 5 letras listas para ser utilizadas por la aplicación.

Para ejecutar el script de Python es necesario tener instalado:

- Python 3.x
- NumPy
- Pandas

Se recomienda usar Anaconda, o alternativamente instalar las dependencias mediante pip:

```bash
cd ./data
pip install -r requirements.txt
```

## Fuentes

- Inspirado en el [Wordle original](https://www.nytimes.com/games/wordle) de Josh Wardle

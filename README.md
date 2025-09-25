# Desarticulator - Generador MIDI para Superior Drummer 3

Un generador avanzado de patrones de batería MIDI diseñado específicamente para Superior Drummer 3. Crea grooves musicales realistas con variaciones automáticas, fills dinámicos y estructura profesional.

## 🎯 Características Principales

- **Patrones de 150 compases** con estructura musical completa
- **Fills automáticos** cada 8 compases con variaciones
- **Velocidades humanizadas** para sonido natural
- **Mapeo GM estándar** compatible con Superior Drummer 3
- **Generación determinística** con seeds fijos
- **Múltiples estilos** de batería (expandible)

## 🚀 Instalación Rápida

### Requisitos
- Python 3.7+
- midiutil

### Instalación
```bash
pip install midiutil
```

## 📖 Uso Básico

### Generar un Patrón de Punk Rock Drum
```bash
python3 examples/generate_punk_rock_drum_file.py
```

Esto genera `PunkRock150bars.mid` listo para importar en Superior Drummer 3.

## 🎵 Estilos Disponibles

### ✅ Punk Rock
- **Tempo**: 150 BPM
- **Características**: Kick constante, snare en 2 y 4, hi-hats agresivos
- **Fills**: Tom rolls rápidos y energéticos
- **Archivo**: `PunkRock150bars.mid`

### 🔄 Próximos Estilos (En desarrollo)
- **Rock Clásico**: 4/4 tradicional con groove dinámico
- **Jazz**: Swing patterns con ride prominente
- **Latin**: Patrones de salsa y bossa nova
- **Metal**: Double bass y blast beats
- **Funk**: Ghost notes y groove sincopado
- **Blues**: Shuffle patterns y fills tradicionales

## 🏗️ Arquitectura del Código

### Estructura Base
```python
def create_[style]_groove():
    # Configuración MIDI
    midi = MIDIFile(1)
    track, channel, tempo, ppq = 0, 9, [BPM], 480
    
    # Mapeo de tambores (GM Standard)
    kick=36, snare=38, closed_hh=42, open_hh=46, 
    ride=51, crash=49, toms=[43,45,48]
    
    # Funciones de patrones
    def add_basic_pattern(start_bar): ...
    def add_variation_1(start_bar): ...
    def add_fill_simple(bar): ...
    def add_fill_complex(bar): ...
    def add_final_fill(bar): ...
    
    # Lógica de construcción
    # 150 compases con fills cada 8 compases
```

### Componentes Clave

#### 1. Sistema de Timing
- **PPQ**: 480 (Pulses Per Quarter note)
- **Ticks por compás**: 1920 (4/4 time)
- **Resolución**: Hasta semicorcheas (120 ticks)

#### 2. Mapeo de Velocidades
```python
# Velocidades realistas
kick_main = 90-100      # Kicks principales
snare_main = 95-100     # Snares acentuados
snare_ghost = 40-50     # Ghost notes
hihats = 65-85          # Hi-hats con variación
toms = 80-95            # Fills y solos
```

#### 3. Estructura Musical
- **Compases 1-7**: Patrón básico
- **Compás 8**: Fill simple/complejo (70/30%)
- **Compases 9-15**: Variación 1
- **Compás 16**: Fill
- **Compás 149**: Fill final épico
- **Compás 150**: Crash + kick de cierre

## 📁 Estructura del Proyecto

```
desarticulator/
├── README.md                          # Este archivo
├── docs/                              # Documentación completa
│   ├── TECHNICAL_DOCS.md              # Especificaciones técnicas
│   ├── CHANGELOG.md                   # Historial de versiones
│   ├── API_REFERENCE.md               # Referencia de API
│   └── CONTRIBUTING.md                # Guía de contribución
├── examples/                          # Ejemplos de uso
│   └── generate_punk_rock_drum_file.py  # Generador Punk Rock Drum
├── styles/                            # Módulos de estilos musicales
│   ├── __init__.py                    # Registro de estilos
│   ├── punk_rock.py                   # Módulo Punk Rock
│   ├── classic_rock.py                # Módulo Rock Clásico
│   └── jazz.py                        # Módulo Jazz
├── output/                            # Archivos MIDI generados
│   └── *.mid                          # Patrones exportados
└── samples/                           # Recursos de audio
    └── drum_packs/                    # Paquetes de batería
        ├── complete_drum_pack_81bpm/
        ├── complete_drum_pack_85bpm/
        └── complete_drum_pack_94bpm/
```

## 🎛️ Configuración Avanzada

### Parámetros Modificables
```python
# En cada generador de estilo
tempo = 150              # BPM del patrón
total_bars = 150         # Número total de compases
fill_frequency = 8       # Fills cada X compases
random_seed = 42         # Seed para reproducibilidad
```

### Mapeo de Tambores (GM Standard)
```python
# Mapeo estándar para Superior Drummer 3
kick = 36        # Bass Drum
snare = 38       # Acoustic Snare
closed_hh = 42   # Closed Hi-Hat
open_hh = 46     # Open Hi-Hat
ride = 51        # Ride Cymbal
crash = 49       # Crash Cymbal
tom_high = 43    # High Tom
tom_mid = 45     # Mid Tom
tom_low = 48     # Low Tom
```

## 🔧 Desarrollo de Nuevos Estilos

### Template Base
```python
def create_[style]_groove():
    # 1. Configuración MIDI base
    # 2. Definir patrones básicos
    # 3. Crear variaciones
    # 4. Diseñar fills característicos
    # 5. Implementar lógica de construcción
    # 6. Añadir final épico
    return midi
```

### Guías de Estilo
- **Punk**: Agresivo, directo, fills de toms rápidos
- **Jazz**: Swing, ride prominente, fills sutiles
- **Latin**: Patrones sincopados, percusión adicional
- **Metal**: Double bass, blast beats, crashes frecuentes
- **Funk**: Ghost notes, groove sincopado, hi-hat abierto

## 🎵 Importar en Superior Drummer 3

1. **Abrir Superior Drummer 3**
2. **Ir a la pestaña MIDI**
3. **Drag & Drop** el archivo `.mid` generado
4. **Ajustar tempo** si es necesario
5. **Seleccionar kit** apropiado para el estilo

## 🤝 Contribuir

### Añadir Nuevo Estilo
1. Crear archivo `styles/[nuevo_estilo].py`
2. Implementar función `create_[estilo]_groove()`
3. Seguir las convenciones de naming y estructura
4. Añadir documentación del estilo
5. Crear script principal `generate_[estilo]_file.py`

### Mejoras Sugeridas
- [ ] Interfaz gráfica para parámetros
- [ ] Exportación a múltiples formatos
- [ ] Análisis de patrones existentes
- [ ] Generación basada en IA
- [ ] Presets de kits específicos

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo LICENSE para detalles.

## 🏆 Estado del Proyecto

**Versión Actual**: 1.0.0 - Punk Rock Generator
**Estado**: ✅ Funcional y estable
**Próximo Release**: Generadores multi-estilo

---

*Desarrollado para músicos y productores que buscan patrones de batería MIDI profesionales y realistas.*

# Documentación Técnica - Desarticulator

## 🏗️ Arquitectura del Sistema

### Visión General
El sistema está diseñado como un generador modular de patrones MIDI, donde cada estilo musical es un módulo independiente que sigue una arquitectura común.

### Componentes Principales

#### 1. Core Engine (Motor Principal)
```python
# Configuración MIDI base
midi = MIDIFile(1)
track = 0
channel = 9          # Canal 10 (índice 9)
ppq = 480           # Pulses Per Quarter note
```

#### 2. Sistema de Timing
```python
# Resolución temporal
ticks_per_bar = 1920        # 4/4 time signature
ticks_per_beat = 480        # Quarter note
ticks_per_eighth = 240      # Eighth note
ticks_per_sixteenth = 120   # Sixteenth note
```

#### 3. Mapeo de Instrumentos (GM Standard)
```python
# Drum mapping para Superior Drummer 3
drum_map = {
    'kick': 36,         # Bass Drum 1
    'snare': 38,        # Acoustic Snare
    'closed_hh': 42,    # Closed Hi-Hat
    'open_hh': 46,      # Open Hi-Hat
    'ride': 51,         # Ride Cymbal 1
    'crash': 49,        # Crash Cymbal 1
    'tom_high': 43,     # High Floor Tom
    'tom_mid': 45,      # Low Tom
    'tom_low': 48       # Hi Mid Tom
}
```

## 🎵 Sistema de Patrones

### Jerarquía de Patrones
1. **Basic Pattern**: Patrón fundamental del estilo
2. **Variations**: Variaciones del patrón básico
3. **Fills**: Transiciones y ornamentaciones
4. **Final Fill**: Cierre épico del groove

### Estructura de Función de Patrón
```python
def add_pattern_function(start_bar, bars=8):
    """
    Añade un patrón específico al MIDI
    
    Args:
        start_bar (int): Compás de inicio
        bars (int): Número de compases del patrón
    """
    for bar in range(start_bar, start_bar + bars):
        # Lógica específica del patrón
        add_note(instrument, bar, position, velocity)
```

## 🎛️ Sistema de Velocidades

### Rangos por Instrumento
```python
velocity_ranges = {
    'kick_main': (90, 100),      # Kicks principales
    'kick_ghost': (60, 75),      # Kicks secundarios
    'snare_main': (95, 100),     # Snares acentuados
    'snare_ghost': (40, 50),     # Ghost notes
    'snare_fill': (85, 95),      # Snares en fills
    'hh_closed_accent': (75, 85), # Hi-hat cerrado acentuado
    'hh_closed_normal': (65, 75), # Hi-hat cerrado normal
    'hh_closed_ghost': (40, 55),  # Hi-hat cerrado suave
    'hh_open': (70, 80),         # Hi-hat abierto
    'ride_normal': (70, 80),     # Ride normal
    'ride_accent': (85, 95),     # Ride acentuado
    'crash': (95, 100),          # Crashes
    'tom_fill': (80, 95)         # Toms en fills
}
```

### Humanización de Velocidades
```python
def humanize_velocity(base_velocity, variation=5):
    """Añade variación humana a las velocidades"""
    return random.randint(
        max(1, base_velocity - variation),
        min(127, base_velocity + variation)
    )
```

## 🔄 Lógica de Construcción

### Algoritmo Principal
```python
def build_groove_structure():
    current_bar = 0
    pattern_type = 0
    
    while current_bar < 149:
        if current_bar == 148:
            # Fill final épico
            add_final_fill(current_bar)
            current_bar += 1
        elif (current_bar + 1) % 8 == 0:
            # Fill cada 8 compases
            add_fill(current_bar)
            current_bar += 1
        else:
            # Alternar entre patrones básicos y variaciones
            if pattern_type == 0:
                add_basic_pattern(current_bar)
                pattern_type = 1
            else:
                add_variation(current_bar)
                pattern_type = 0
            current_bar += 7
    
    # Cierre final
    add_note(crash, 149, 0, 100, 2.0)
    add_note(kick, 149, 0, 100)
```

## 🎯 Especificaciones por Estilo

### Punk Rock (Implementado)
```python
# Características del estilo
tempo = 150
time_signature = (4, 4)
fill_frequency = 8
fill_complexity = 0.7  # 70% fills simples, 30% complejos

# Patrones característicos
kick_pattern = "1 + 2e+ 3 + 4+"     # Kick constante con sincopas
snare_pattern = "+ 2 + 4"            # Snare en 2 y 4
hh_pattern = "16th notes with accents" # Hi-hats en semicorcheas
```

### Template para Nuevos Estilos
```python
def create_[style]_groove():
    # 1. Configuración específica del estilo
    tempo = [BPM]
    style_config = {
        'fill_frequency': [compases],
        'complexity': [0.0-1.0],
        'swing_factor': [0.0-1.0],
        'ghost_note_probability': [0.0-1.0]
    }
    
    # 2. Patrones básicos del estilo
    def add_basic_pattern(start_bar):
        # Implementar patrón fundamental
        pass
    
    # 3. Variaciones del estilo
    def add_variation_1(start_bar):
        # Primera variación
        pass
    
    def add_variation_2(start_bar):
        # Segunda variación (opcional)
        pass
    
    # 4. Fills característicos
    def add_fill_simple(bar):
        # Fill simple del estilo
        pass
    
    def add_fill_complex(bar):
        # Fill complejo del estilo
        pass
    
    # 5. Fill final épico
    def add_final_fill(bar):
        # Cierre característico del estilo
        pass
    
    # 6. Construcción del groove
    return build_groove_with_style_logic()
```

## 🔧 Herramientas de Desarrollo

### Función de Utilidad para Notas
```python
def add_note(drum, bar, beat_pos, velocity=85, duration=0.1):
    """
    Añade una nota MIDI al track
    
    Args:
        drum (int): Número MIDI del instrumento
        bar (int): Número de compás (0-149)
        beat_pos (int): Posición en ticks dentro del compás
        velocity (int): Velocidad MIDI (1-127)
        duration (float): Duración en beats
    """
    time_ticks = (bar * ticks_per_bar) + beat_pos
    midi.addNote(track, channel, drum, time_ticks / ppq, duration, velocity)
```

### Validación de Patrones
```python
def validate_pattern(pattern_function):
    """Valida que un patrón no exceda los límites temporales"""
    # Verificar que todas las notas estén dentro del rango válido
    # Comprobar que no haya overlaps problemáticos
    # Validar velocidades dentro del rango MIDI
    pass
```

### Debug y Análisis
```python
def analyze_groove(midi_file):
    """
    Analiza un groove generado para métricas de calidad
    
    Returns:
        dict: Estadísticas del groove (densidad, variación, etc.)
    """
    metrics = {
        'total_notes': 0,
        'notes_per_bar': [],
        'velocity_distribution': {},
        'instrument_usage': {},
        'fill_positions': []
    }
    return metrics
```

## 📊 Métricas de Calidad

### KPIs del Groove
- **Densidad promedio**: Notas por compás
- **Variación de velocidades**: Distribución de intensidades
- **Balance instrumental**: Uso equilibrado de instrumentos
- **Consistencia temporal**: Regularidad del patrón
- **Complejidad de fills**: Variedad en transiciones

### Testing Automático
```python
def test_groove_quality(midi_file):
    """Tests automáticos de calidad"""
    tests = [
        test_exact_bar_count(150),
        test_velocity_ranges(),
        test_no_overlapping_notes(),
        test_final_crash_present(),
        test_fill_frequency(8)
    ]
    return all(tests)
```

## 🚀 Optimizaciones

### Performance
- **Generación en memoria**: Todo el MIDI se construye en RAM
- **Batch note adding**: Añadir múltiples notas por llamada
- **Lazy evaluation**: Calcular patrones solo cuando se necesiten

### Memoria
- **Reutilización de patrones**: Cachear patrones comunes
- **Compresión de datos**: Almacenar solo diferencias entre variaciones

## 🔮 Roadmap Técnico

### Fase 1 (Actual)
- ✅ Generador base funcional
- ✅ Estilo Punk Rock completo
- ✅ Documentación técnica

### Fase 2 (Próximo)
- [ ] Sistema modular de estilos
- [ ] Configuración externa (JSON/YAML)
- [ ] Validación automática de patrones

### Fase 3 (Futuro)
- [ ] Generación basada en templates
- [ ] Análisis de grooves existentes
- [ ] Machine learning para nuevos patrones
- [ ] API REST para generación remota

---

*Esta documentación técnica debe actualizarse con cada nuevo estilo implementado.*

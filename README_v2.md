# Desarticulator v2.0 - Modular Multi-Genre MIDI Drum Pattern Generator

🥁 **Sistema modular avanzado de generación de patrones de batería MIDI con variaciones auténticas**

## ✨ **Nuevas Características v2.0**

### 🔄 **Sistema de Variaciones**
- **5 tipos de patrones**: `basic`, `variation_1`, `variation_2`, `fill_simple`, `fill_complex`
- **Randomización inteligente**: Cada generación produce patrones únicos
- **Fills automáticos**: Transiciones musicales cada 8 compases
- **Humanización**: Velocidades randomizadas para sonido natural

### 🏗️ **Arquitectura Modular**
- **Géneros separados**: Cada género en su propio módulo
- **Fácil extensión**: Agregar nuevos géneros es simple
- **Código limpio**: Separación clara de responsabilidades
- **Mantenible**: Estructura escalable y organizada

### 🎵 **Géneros Implementados**
- **Rock Nacional**: Sumo, Los Redonditos - agresivo, punk-influenced
- **Blues Argentino**: Pappo's Blues - shuffle feel, blues rock attitude

## 📁 **Estructura del Proyecto**

```
desarticulator/
├── desarticulator_v2.py          # Script principal modular
├── core/                          # Funcionalidades centrales
│   ├── base_pattern.py           # Clase base para patrones
│   └── pattern_generator.py      # Generador principal
├── genres/                        # Módulos de géneros
│   └── argentinian/              # Géneros argentinos
│       ├── rock_nacional.py     # Rock Nacional con variaciones
│       └── blues_argentino.py   # Blues Argentino con variaciones
├── output/                        # Archivos MIDI generados
├── docs/                         # Documentación
└── examples/                     # Scripts de ejemplo
```

## 🚀 **Uso Rápido**

### **Listar géneros disponibles:**
```bash
python3 desarticulator_v2.py --list
```

### **Información de un género:**
```bash
python3 desarticulator_v2.py --info rock_nacional
```

### **Generar patrón con variaciones:**
```bash
# Patrón completamente aleatorio (máximas variaciones)
python3 desarticulator_v2.py --genre rock_nacional --tempo 160

# Patrón reproducible con seed
python3 desarticulator_v2.py --genre blues_argentino --tempo 120 --seed 42

# Personalizar número de compases
python3 desarticulator_v2.py --genre rock_nacional --tempo 140 --bars 100
```

## 🎯 **Sistema de Variaciones**

### **Tipos de Patrones:**
- **`basic`**: Patrón base del género
- **`variation_1`**: Primera variación (más agresiva)
- **`variation_2`**: Segunda variación (diferentes elementos)
- **`fill_simple`**: Fill simple para transiciones
- **`fill_complex`**: Fill complejo para secciones importantes

### **Selección Inteligente:**
- **Fills automáticos**: Cada 8 compases
- **Variaciones aleatorias**: 25% probabilidad en otros compases
- **Humanización**: Velocidades randomizadas ±10 MIDI units
- **Crash final**: Siempre en el compás 150

## 🔧 **Desarrollo**

### **Agregar Nuevo Género:**

1. **Crear el módulo:**
```python
# genres/categoria/mi_genero.py
from core.base_pattern import BasePattern

class MiGeneroPattern(BasePattern):
    @property
    def genre_name(self) -> str:
        return "Mi Género"
    
    @property
    def description(self) -> str:
        return "Descripción del género"
    
    def create_basic_pattern(self, midi, start_bar, bars=8):
        # Implementar patrón básico
        pass
    
    # Implementar variation_1, variation_2, fill_simple, fill_complex
```

2. **Registrar en el generador:**
```python
# core/pattern_generator.py
from genres.categoria.mi_genero import MiGeneroPattern
self.patterns['mi_genero'] = MiGeneroPattern
```

### **Características de Cada Género:**

#### **Rock Nacional (Sumo/Los Redonditos):**
- **Basic**: Kicks agresivos, ghost notes, hi-hats punk
- **Variation 1**: Double kicks, más intensidad
- **Variation 2**: Ride pattern con crashes
- **Fills**: Snare rolls y tom cascades

#### **Blues Argentino (Pappo's Blues):**
- **Basic**: Shuffle feel, kicks sincopados
- **Variation 1**: Ride cymbal, bell patterns
- **Variation 2**: Open hi-hats, ghost notes
- **Fills**: Blues-style tom fills

## 📊 **Comparación de Versiones**

| Característica | v1.0 | v2.0 |
|---------------|------|------|
| Variaciones | ❌ Siempre iguales | ✅ 5 tipos diferentes |
| Estructura | ❌ Un archivo gigante | ✅ Modular y organizada |
| Extensibilidad | ❌ Difícil agregar géneros | ✅ Fácil agregar módulos |
| Humanización | ❌ Velocidades fijas | ✅ Randomización inteligente |
| Documentación | ❌ Básica | ✅ Completa y detallada |

## 🎵 **Ejemplos de Uso**

### **Generar múltiples variaciones:**
```bash
# Tres versiones diferentes del mismo género
python3 desarticulator_v2.py --genre rock_nacional --tempo 160 --seed 1
python3 desarticulator_v2.py --genre rock_nacional --tempo 160 --seed 2
python3 desarticulator_v2.py --genre rock_nacional --tempo 160  # Sin seed (máxima variación)
```

### **Comparar géneros:**
```bash
python3 desarticulator_v2.py --genre rock_nacional --tempo 140 --seed 42
python3 desarticulator_v2.py --genre blues_argentino --tempo 140 --seed 42
```

## 🔮 **Próximas Características**

- [ ] **Más géneros**: Madchester, Krautrock, Jazz Fusion
- [ ] **Exportación avanzada**: Diferentes formatos
- [ ] **GUI**: Interfaz gráfica para facilitar uso
- [ ] **Plugins**: Sistema de plugins para extensiones
- [ ] **Análisis**: Estadísticas de patrones generados

## 🎤 **Géneros Planeados**

### **Experimentales/Progresivos:**
- Prog Rock (Frank Zappa style)
- Math Rock (polyrhythms)
- Krautrock (motorik beats)
- Art Rock (sophisticated)

### **Internacionales:**
- Madchester (Happy Mondays)
- Dub (King Tubby style)
- Reggae (Bob Marley style)
- Ska (The Skatalites style)

## 📈 **Resultados de Pruebas**

### **Variaciones Confirmadas:**
- **Rock Nacional seed 1**: 19,553 bytes
- **Rock Nacional seed 2**: 19,714 bytes
- **Rock Nacional sin seed**: 20,434 bytes
- **Blues Argentino seed 1**: 14,056 bytes
- **Blues Argentino seed 2**: 15,532 bytes

✅ **Cada generación produce archivos MIDI únicos con diferentes tamaños y contenido**

---

**Desarticulator v2.0** - Llevando la generación de patrones de batería MIDI al siguiente nivel con variaciones auténticas y arquitectura modular. 🥁🎵

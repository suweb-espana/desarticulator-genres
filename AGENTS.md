# Desarticulator — agent context

Modular MIDI drum pattern generator for Superior Drummer 3.

## graphify

Usar regla de proyecto `.cursor/rules/graphify.mdc` (+ global), mismo modelo que Tervia.

- Orientación: regla **global** `graphify.mdc` (`query` / `path` / `explain` antes de explorar).
- Rebuild: `graphify update .` (repo único; no hay `graphify-rebuild.sh` de productos anidados).
- Review formal: `.cursor/rules/36-code-review-graphify.mdc` (sin prompt-corrector Jira de Tervia).

## Convenios

- Código y commits: inglés.
- Docs de usuario: castellano.
- Prefijo MIDI: `fracaso_inminente_`.
- Nuevos géneros: actualizar `GENRE_IMPLEMENTATION_STATUS.md`.
- No auto-commit / no auto-push.

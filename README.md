
## Structure

- `src/vulnerable.py` - insecure patterns
- `src/safe.py` - safe patterns
- `src/main.py` - simple runner

## Suggested SAST tools

### Bandit

```bash
pip install bandit
bandit -r src
```

### Semgrep

```bash
pip install semgrep
semgrep --config auto src
```

## Notes

This project is intentionally insecure in parts and should not be used in production.

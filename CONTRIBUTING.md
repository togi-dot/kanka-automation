# Contributing to KANKA Automation

## Code of Conduct

Be respectful and constructive.

## How to Contribute

### Reporting Bugs

1. Check if issue already exists
2. Provide detailed description
3. Include steps to reproduce
4. Attach logs if possible

### Suggesting Enhancements

1. Describe the enhancement
2. Explain the use case
3. Provide examples

### Pull Requests

1. Fork the repository
2. Create feature branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature/my-feature`
5. Open Pull Request

## Development Setup

```bash
git clone https://github.com/togi-dot/kanka-automation.git
cd kanka-automation
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Running Tests

```bash
pytest tests/
```

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings
- Comment complex logic

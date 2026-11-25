# Checkout QA | Playwright Test Suite

Six automated Chromium regression tests against a self-contained fictional checkout fixture. No payment processing, no external website and no network dependency during browser interaction.

```bash
pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -q
```
Open checkout.html to inspect the fixture. Failed tests save screenshots under artifacts/. Independent AI-assisted demonstration. See TEST_PLAN.md for coverage and limitations.

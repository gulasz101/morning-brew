"""Gate: the project fit counts are reported, never enforced."""

from __future__ import annotations

from gate import fit_counts


BODY = """## 1. A, by b
**For my projects:**
- homelab-2nd: Run it next to pihole as a second resolver on k3s

## 2. C, by d
**For my projects:**
- ideogram4-local: Swap the sampler inside ComfyUI. Would fit if it needs 24 GB of memory.

## 3. E, by f
**For my projects:** Nothing for my projects, no Kubernetes path and no metrics.

## 4. G, by h
**For my projects:** Nothing for my projects.

## 5. I, by j
**For my projects:** Nothing for my projects, no Kubernetes path.

**Spark (homelab-2nd):** Point the status page at the departure board for the hallway tablet.
"""


def test_fit_counts():
    assert fit_counts(BODY) == {"direct": 1, "conditional": 1, "none": 3, "reasoned_none": 2, "spark": 1}

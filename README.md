# Hey, I'm Brian

I build and operate AI infrastructure on bare metal — and I run a production business on top of it.

---

## Gridline Productions

A fully automated commercial AI render operation, built from scratch in roughly a month with no prior rendering or pipeline experience.

The system handles the entire lifecycle: prompt generation, rendering across multiple models, multi-tier quality enrichment, automated scoring and selection, metadata processing, and commercial listing — all with a single click to start.

**By the numbers:**
- 30,000+ renders produced
- Fully automated end-to-end: one-click startup, no manual intervention required
- Self-correcting and self-restarting — if something fails, the system recovers on its own
- Self-improving — the platform learns from its own operations, surfacing what works and deprioritizing what doesn't
- Dual control plane with machine-specific fallback agents across a multi-machine estate
- Custom render engine replacing off-the-shelf tooling entirely

Everything runs on hardware I own. No cloud dependencies for production workloads.

---

## Infrastructure

I design and operate a self-hosted multi-machine estate for AI workloads, enrichment pipelines, observability, and automation.

- **Multi-host GPU compute:** AMD RX 7800 XT, NVIDIA GTX 1080 Ti, Apple Silicon
- **Networking:** Unbound recursive DNS, AdGuard filtering, VLAN-segmented UniFi
- **Virtualization & storage:** Proxmox VE, automated backup
- **Observability:** Real-time dashboards, system-wide queryability, automated anomaly detection with alerting
- **Operations:** Structured ticketing system with 200+ closed tickets, startup/shutdown verification routines, full audit trail from day one

---

## Philosophy

I own the stack. Compute, networking, DNS, storage, monitoring, and deployment all run on hardware I control.

If something breaks, I fix it at the root cause. The [PyTorch memory fix](https://github.com/brjen/pytorch-memory-fix) came from weeks of instrumented profiling across a real production workload — tracing the issue to glibc allocator behavior rather than treating it as an application-level bug.

I build systems that are observable, rebuildable, and free of vendor lock-in. Every decision, every fix, and every lesson learned is documented and searchable. The system's institutional memory goes back to day one.

---

## Stack

Python, Node.js, Svelte, FastAPI, SQLite, Linux, Proxmox VE, systemd, Git, SSH, Fish shell

---

## Open Source

* **[pytorch-memory-fix](https://github.com/brjen/pytorch-memory-fix)** — Two environment variables that eliminate PyTorch RSS creep during repeated model load/unload cycles on Linux. Zero code changes. Zero performance cost.

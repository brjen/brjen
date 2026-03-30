# Hey, I'm Brian

I build and operate AI infrastructure on bare metal.

---

## What I Do

I design and run a self-hosted multi-machine estate for AI workloads, enrichment pipelines, observability, and custom tooling.

### AI Systems
Custom render and processing pipelines spanning diffusion models (SDXL, Flux, PixArt), model switching across AMD and NVIDIA GPUs, and multi-tier enrichment using vision models for automated asset analysis and metadata tagging.

### Observability & Intelligence
SQLite-native multi-database architecture: FTS5 knowledge indexing, federated metrics aggregation, real-time change tracking with SHA verification, and agent session instrumentation. No Postgres, no Redis — by design.

### Infrastructure & Network
Unbound recursive DNS + AdGuard filtering, VLAN-segmented UniFi networking, Proxmox virtualization, and host operations across Linux systems with systemd.

---

## Stack

- Multi-host GPU estate: AMD RX 7800 XT, NVIDIA GTX 1080 Ti, Apple Silicon
- Python, Node.js, Svelte, FastAPI, SQLite
- Unbound DNS, AdGuard, UniFi, VLAN segmentation
- Linux, Proxmox VE, systemd
- Git, SSH, rsync, Fish shell

---

## Philosophy

I own the stack. Compute, networking, DNS, storage, monitoring, and deployment all run on hardware I control.

If something breaks, I fix it at the root cause. The [PyTorch memory fix](https://github.com/brjen/pytorch-memory-fix) came from weeks of instrumented profiling across a real production workload, tracing the issue to glibc allocator behavior rather than treating it as an application-level bug.

---

## Open Source

- **[pytorch-memory-fix](https://github.com/brjen/pytorch-memory-fix)** — Two environment variables that eliminate PyTorch RSS creep during repeated model load/unload cycles on Linux.

---
name: taste-skill
description: "Anti-slop frontend skill: read the brief, infer design direction, tune three dials (VARIANCE/MOTION/DENSITY), ship premium landing pages/portfolios/redesigns that don't look templated. Real design systems, audit-first on redesigns, strict pre-flight check."
---

# tasteskill: Anti-Slop Frontend Skill

> Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI.
> Every rule below is **contextual**. None of it fires automatically. First read the brief, then pull only what fits.

---

## 0. BRIEF INFERENCE (Read the Room Before Anything Else)

### 0.A Read these signals first
1. **Page kind** — landing (SaaS / consumer / agency / event), portfolio (dev / designer / creative studio), redesign (preserve vs overhaul), editorial / blog.
2. **Vibe words** the user used — "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "glassy", "dark tech".
3. **Reference signals** — URLs they linked, screenshots they pasted, products they named, brands they're competing with.
4. **Audience** — B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a portfolio.
5. **Brand assets that already exist** — logo, color, type, photography.
6. **Quiet constraints** — accessibility-first audiences, public-sector, regulated industries, kids' products.

### 0.B Output a one-line "Design Read" before generating
Before any code, state: **"Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."**

---

## 1. THE THREE DIALS (Core Configuration)

After the design read, set three dials. Every layout, motion, and density decision below is gated by these.

- **`DESIGN_VARIANCE: 8`** — 1 = Perfect Symmetry, 10 = Artsy Chaos
- **`MOTION_INTENSITY: 6`** — 1 = Static, 10 = Cinematic / Physics
- **`VISUAL_DENSITY: 4`** — 1 = Art Gallery / Airy, 10 = Cockpit / Packed Data

### 1.A Dial Inference

| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| "minimalist / clean / calm / editorial / Linear-style" | 5-6 | 3-4 | 2-3 |
| "premium consumer / Apple-y / luxury / brand" | 7-8 | 5-7 | 3-4 |
| "playful / wild / Dribbble / Awwwards / experimental / agency" | 9-10 | 8-10 | 3-4 |
| "landing page / portfolio / marketing site (default)" | 7-9 | 6-8 | 3-5 |
| "trust-first / public-sector / regulated / accessibility-critical" | 3-4 | 2-3 | 4-5 |
| "redesign - preserve" | match existing | +1 | match existing |
| "redesign - overhaul" | +2 | +2 | match existing |

### 1.B Use-Case Presets

| Use case | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Landing (SaaS, mainstream) | 7 | 6 | 4 |
| Landing (Agency / creative) | 9 | 8 | 3 |
| Landing (Premium consumer) | 7 | 6 | 3 |
| Portfolio (Designer / studio) | 8 | 7 | 3 |
| Portfolio (Developer) | 6 | 5 | 4 |
| Editorial / Blog | 6 | 4 | 3 |
| Public-sector service | 3 | 2 | 5 |
| Redesign - preserve | match | match+1 | match |
| Redesign - overhaul | +2 | +2 | match |

---

## 2. BRIEF → DESIGN SYSTEM MAP

### 2.A When to reach for a real design system

| Brief reads as… | Reach for |
|---|---|
| Microsoft / enterprise SaaS / dashboards | `@fluentui/react-components` |
| Google-ish UI, Material-flavored product | `@material/web` + Material 3 tokens |
| IBM-style B2B / enterprise analytics | `@carbon/react` + `@carbon/styles` |
| Shopify app surfaces | `polaris.js` web components / Polaris React |
| Atlassian / Jira-style product | `@atlaskit/*` + `@atlaskit/tokens` |

### 2.B When the brief is an aesthetic, not a system

| Aesthetic | Honest implementation |
|---|---|
| Glassmorphism / "frosted glass" | `backdrop-filter`, layered borders, highlight overlays. Solid-fill fallback for `prefers-reduced-transparency`. |
| Bento (Apple-style tile grids) | CSS Grid with mixed cell sizes. |
| Brutalism | Native CSS, monospace, raw borders. |
| Editorial / magazine | Serif type, asymmetric grid, generous whitespace. |
| Dark tech / hacker | Mono + accent neon, terminal motifs. |
| Aurora / mesh gradients | SVG or layered radial gradients. |

---

## 3. DEFAULT ARCHITECTURE & CONVENTIONS

### 3.A Stack
- Framework detected from user context (React, Vue, Svelte, or plain HTML/CSS/JS)
- Tailwind CSS v4 preferred for utility styling unless a real design system applies
- GSAP / Motion for scroll-driven animation (never `window.addEventListener('scroll')`)

### 3.B Responsiveness
- Mobile-first CSS. Desktop layout builds on mobile base.
- `min-h-[100dvh]` never `h-screen`.
- Navigation on ONE line at desktop, height ≤ 80px.

### 3.C Icons
- Phosphor / HugeIcons / Radix / Tabler ONLY.
- Lucide on explicit request only.
- NO hand-rolled SVG icons.

---

## 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)

### 4.A Hero Architecture
- Headline ≤ 2 lines at desktop. Subtext ≤ 20 words AND ≤ 4 lines.
- Max 4 text elements in hero (eyebrow OR brand strip, headline, subtext, CTAs).
- NO tiny tagline below CTAs, no trust micro-strip in hero.
- Hero content does not float halfway down the viewport (max `pt-24`).

### 4.B Layout Variance
- No two adjacent sections share the same layout family.
- At least 4 different layout families across 8+ sections.
- Bento grids: N items → N cells. NO empty cells.

### 4.C Section-Layout-Repetition Check
If two consecutive sections look the same (Left/Right split, full-width text, etc.), change one. Defaulting to Left/Right split for every section is a laziness tell.

### 4.D Theme Lock
ONE theme (light, dark, or auto) for the whole page. No section flips to inverted mode mid-page.

---

## 5. PERFORMANCE & ACCESSIBILITY GUARDRAILS

- Animate only `transform` and `opacity`. Never `top`, `left`, `width`, `height`.
- `prefers-reduced-motion` respected for everything `MOTION_INTENSITY > 3`.
- Core Web Vitals targets: LCP < 2.5s, INP < 200ms, CLS < 0.1.
- `useEffect` animations must have strict cleanup functions.

---

## 6. AI TELLS (Forbidden Patterns)

### Banned by default
- **ZERO em-dashes (`—`)** anywhere. Not in headlines, body, quotes, CTAs, alt text, captions.
- **Inter as default font.** Pick the right typeface for the brief.
- **AI-purple** (#7C3AED, #8B5CF6) as the primary accent.
- **Three-equal-card rows** for feature sections (reach for bento / mixed-span layout).
- **Jane Doe / John Doe / Acme Corp / "Quietly in use at"** placeholder text.
- **Section-number eyebrows** (`00 / INDEX`, `001 · Capabilities`, `06 · how it works`).
- **Fake screenshots built from `<div>` rectangles.**
- **Broken Unsplash links.** Use `https://picsum.photos/seed/{string}/{w}/{h}`.

### Typography
- The middle-dot (`·`) is rationed: max 1 per line in metadata strips. Prefer line breaks, hairlines, or columns.
- NO decorative dots before every nav link, task row, or badge.
- NO photo-credit captions as decoration (`Field study no. 12 · Ines Caetano`).

---

## 7. REDESIGN PROTOCOL

### 7.A Detect the Mode
Is this a greenfield build or an existing project? Check user input for existing code, URL references, or "fix my site" framing.

### 7.B Audit Before Touching
1. Run a visual audit: spacing, hierarchy, color, type, motion.
2. Identify what works (preserve it) and what doesn't (replace it).
3. Establish the delta: targeted evolution vs full redesign.

### 7.C What Never Changes Silently
- Brand colors, logo, and name stay unless explicitly requested.
- Core content hierarchy and page structure are preserved by default.

---

## 8. FINAL PRE-FLIGHT CHECK

Run this matrix before outputting code. **THIS IS NOT OPTIONAL.**

- [ ] Brief inference declared?
- [ ] Dial values explicit and reasoned from the brief?
- [ ] Design system chosen from Section 2 if applicable?
- [ ] ZERO em-dashes (`—`) anywhere?
- [ ] Hero fits the viewport (headline ≤ 2 lines, CTA visible)?
- [ ] Premium-consumer palette is NOT the AI-default beige+brass+oxblood family?
- [ ] No two sections share the same layout family?
- [ ] Bento has rhythm AND exact cell count?
- [ ] Real images used — NO div-based fake screenshots?
- [ ] Motion motivated — every animation justified?
- [ ] Dark mode tokens defined (for consumer-facing pages)?
- [ ] Reduced motion respected?
- [ ] Icons from allowed library only — NO hand-rolled SVG?
- [ ] One design system per project?
- [ ] No AI Tells from Section 6?

If a single checkbox cannot be honestly ticked, the page is not done.

---

## 9. OUT OF SCOPE

This skill is NOT for:
- Dashboards / dense product UI / admin panels
- Data tables
- Multi-step forms / wizards
- Code editors
- Native mobile apps
- Realtime collab UIs

If the brief is one of the above, say so explicitly and point to the right tool.

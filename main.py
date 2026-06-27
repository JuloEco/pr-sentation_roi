from flask import Flask, render_template_string

app = Flask(__name__)
HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Intrigues & Couronne — Règles Officielles</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet" />
  <style>/* ============================================================
   INTRIGUES & COURONNE — Stylesheet
   Palette : deep parchment night, gold, crimson, ash
   ============================================================ */

:root {
  --noir:      #0e0b07;
  --encre:     #1a1409;
  --parchemin: #f5ead6;
  --or:        #c9922a;
  --or-clair:  #e8b84b;
  --cramoisi:  #8b1a1a;
  --cramoisi-clair: #b52b2b;
  --cendre:    #6b6255;
  --cendre-clair: #9e917e;
  --blanc-os:  #f0e6d0;
  --vert-jade: #2a5c45;
  --vert-clair: #3d7a5e;

  --font-display: 'Cinzel', serif;
  --font-body:    'Crimson Text', serif;
  --font-accent:  'EB Garamond', serif;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: var(--font-body);
  background: var(--noir);
  color: var(--parchemin);
  font-size: 1.1rem;
  line-height: 1.7;
}

/* ---- HERO ---- */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
}

.hero-bg {
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse at 50% 30%, #3a1e0a55 0%, transparent 60%),
    radial-gradient(ellipse at 20% 80%, #8b1a1a22 0%, transparent 50%),
    linear-gradient(160deg, #1a0f05 0%, #0e0b07 50%, #12080a 100%);
}

.hero-bg::after {
  content: '';
  position: absolute; inset: 0;
  background-image:
    repeating-linear-gradient(0deg, transparent, transparent 80px, #c9922a08 80px, #c9922a08 81px),
    repeating-linear-gradient(90deg, transparent, transparent 80px, #c9922a06 80px, #c9922a06 81px);
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 820px;
  padding: 2rem;
}

.eyebrow {
  font-family: var(--font-display);
  font-size: 0.75rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--cendre-clair);
  margin-bottom: 1.5rem;
}

.hero-content h1 {
  font-family: var(--font-display);
  font-size: clamp(3.5rem, 9vw, 7rem);
  font-weight: 700;
  line-height: 1.05;
  color: var(--blanc-os);
  letter-spacing: 0.02em;
  text-shadow: 0 0 60px #c9922a40;
}

.hero-content h1 span {
  color: var(--or);
  font-size: 0.7em;
  display: block;
  margin: -0.1em 0 0.1em;
}

.hero-sub {
  font-family: var(--font-accent);
  font-style: italic;
  font-size: 1.25rem;
  color: var(--cendre-clair);
  margin: 1.5rem auto;
  max-width: 500px;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2.5rem;
}

.btn-primary {
  font-family: var(--font-display);
  font-size: 0.8rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.85rem 2rem;
  background: var(--or);
  color: var(--noir);
  border: 2px solid var(--or);
  transition: all 0.25s;
}

.btn-primary:hover {
  background: var(--or-clair);
  border-color: var(--or-clair);
  box-shadow: 0 0 24px #c9922a66;
}

.btn-ghost {
  font-family: var(--font-display);
  font-size: 0.8rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.85rem 2rem;
  background: transparent;
  color: var(--parchemin);
  border: 2px solid #6b625566;
  transition: all 0.25s;
}

.btn-ghost:hover {
  border-color: var(--cendre-clair);
  color: var(--blanc-os);
}

.scroll-hint {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  color: var(--cendre);
  font-size: 1.4rem;
  animation: bob 2s ease-in-out infinite;
}

@keyframes bob {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(8px); }
}

/* ---- LAYOUT ---- */
.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section {
  padding: 6rem 0;
  border-top: 1px solid #c9922a18;
}

.section-dark {
  background: #120d06;
}

.section-label {
  font-family: var(--font-display);
  font-size: 0.7rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--or);
  margin-bottom: 1rem;
}

.section-label.light { color: var(--or-clair); }

.section h2 {
  font-family: var(--font-display);
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  color: var(--blanc-os);
  font-weight: 600;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.section-intro {
  font-family: var(--font-accent);
  font-size: 1.2rem;
  color: var(--cendre-clair);
  max-width: 600px;
  margin-bottom: 3rem;
}

.section-intro.light-text { color: #a8997e; }

/* ---- GAUGES ---- */
.gauges-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

@media (max-width: 600px) { .gauges-grid { grid-template-columns: 1fr; } }

.gauge-card {
  background: #1a1409;
  border: 1px solid #c9922a22;
  padding: 2rem;
}

.gauge-icon { font-size: 2rem; margin-bottom: 0.75rem; }

.gauge-card h3 {
  font-family: var(--font-display);
  font-size: 1rem;
  color: var(--blanc-os);
  margin-bottom: 1rem;
}

.gauge-bar {
  height: 6px;
  background: #2a2018;
  margin-bottom: 1rem;
  border-radius: 0;
}

.gauge-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--vert-jade), var(--vert-clair));
  transition: width 1s ease;
}

.gauge-fill.gold {
  background: linear-gradient(90deg, var(--or), var(--or-clair));
}

.gauge-card p { font-size: 1rem; color: var(--cendre-clair); }

/* ---- RUIN / INFO BLOCKS ---- */
.ruin-block {
  display: flex;
  gap: 1.25rem;
  align-items: flex-start;
  background: #2a100a;
  border: 1px solid #8b1a1a55;
  border-left: 4px solid var(--cramoisi);
  padding: 1.5rem;
  margin-bottom: 2.5rem;
}

.ruin-icon { font-size: 1.5rem; flex-shrink: 0; margin-top: 0.1rem; }
.ruin-block strong { font-family: var(--font-display); color: #d45050; font-size: 1rem; display: block; margin-bottom: 0.4rem; }
.ruin-block p { color: var(--cendre-clair); font-size: 1rem; }

/* ---- FORMULA ---- */
.victory-block {
  background: #1a1409;
  border: 1px solid #c9922a33;
  border-top: 3px solid var(--or);
  padding: 2rem 2.5rem;
}

.victory-block h3 {
  font-family: var(--font-display);
  color: var(--or);
  font-size: 1.1rem;
  margin-bottom: 0.75rem;
}

.victory-block > p { color: var(--cendre-clair); margin-bottom: 1.25rem; font-size: 1rem; }

.formula {
  font-family: var(--font-display);
  font-size: clamp(0.8rem, 2.2vw, 1.05rem);
  color: var(--or-clair);
  background: #0e0b07;
  border: 1px solid #c9922a33;
  padding: 1.25rem 1.5rem;
  text-align: center;
  letter-spacing: 0.03em;
  margin: 1.5rem 0;
  word-break: break-word;
}

.formula-note { font-size: 1rem; color: var(--cendre-clair); }

/* ---- PILLARS ---- */
.pillars-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

@media (max-width: 700px) { .pillars-grid { grid-template-columns: 1fr; } }

.pillar {
  border-top: 2px solid var(--or);
  padding: 1.75rem 1.5rem;
  background: #1a14091a;
}

.pillar-num {
  font-family: var(--font-display);
  font-size: 2rem;
  color: var(--or);
  opacity: 0.5;
  margin-bottom: 0.75rem;
}

.pillar h4 {
  font-family: var(--font-display);
  color: var(--blanc-os);
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.pillar p { font-size: 1rem; color: #9e917e; }

/* ---- CONFIG TABS ---- */
.config-tabs {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.config-tab {
  font-family: var(--font-display);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.6rem 1.25rem;
  background: transparent;
  color: var(--cendre-clair);
  border: 1px solid #6b625533;
  cursor: pointer;
  transition: all 0.2s;
}

.config-tab:hover,
.config-tab.active {
  background: var(--or);
  color: var(--noir);
  border-color: var(--or);
}

.config-panel { display: none; }
.config-panel.active { display: block; }

.config-note {
  font-family: var(--font-accent);
  font-style: italic;
  font-size: 1.15rem;
  color: var(--cendre-clair);
  margin-bottom: 1.5rem;
  border-left: 3px solid var(--or);
  padding-left: 1rem;
}

.config-roles {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.config-role-chip {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #1a1409;
  border: 1px solid #c9922a33;
  padding: 0.6rem 1rem;
  font-family: var(--font-display);
  font-size: 0.8rem;
  color: var(--blanc-os);
  letter-spacing: 0.05em;
}

.chip-icon { font-size: 1.2rem; }

/* ---- ROLES ---- */
.roles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 2rem;
}

@media (max-width: 500px) { .roles-grid { grid-template-columns: 1fr; } }

.role-card {
  background: #1a1409;
  border: 1px solid #c9922a22;
  transition: border-color 0.25s, box-shadow 0.25s;
}

.role-card:hover {
  border-color: #c9922a66;
  box-shadow: 0 8px 40px #c9922a14;
}

.role-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem 1.5rem 1rem;
  border-bottom: 1px solid #c9922a1a;
}

.role-icon { font-size: 2.2rem; }

.role-header h3 {
  font-family: var(--font-display);
  font-size: 1rem;
  color: var(--blanc-os);
  margin-bottom: 0.25rem;
}

.role-badge {
  font-family: var(--font-display);
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--or);
  background: #c9922a18;
  padding: 0.15rem 0.5rem;
}

.role-flux {
  padding: 1rem 1.5rem;
  font-size: 0.95rem;
  color: var(--cendre-clair);
  border-bottom: 1px solid #c9922a0f;
  font-style: italic;
}

.role-flux strong { font-style: normal; color: var(--blanc-os); }

.role-voies {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-bottom: 1px solid #c9922a0f;
}

.voie {
  padding: 1rem 1.2rem;
  font-size: 0.9rem;
}

.voie:first-child { border-right: 1px solid #c9922a0f; }

.voie-label {
  font-family: var(--font-display);
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}

.voie.serviteur .voie-label { color: var(--vert-clair); }
.voie.fourbe .voie-label { color: var(--cramoisi-clair); }
.voie p { color: var(--cendre-clair); line-height: 1.5; font-size: 0.88rem; }

.robinets {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.robinet {
  padding: 1rem 1.2rem;
  font-size: 0.88rem;
}

.robinet:first-child { border-right: 1px solid #c9922a0f; }

.robinet-label {
  font-family: var(--font-display);
  font-size: 0.6rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}

.robinet.ouvrir { background: #0a1a0f; }
.robinet.ouvrir .robinet-label { color: var(--vert-clair); }
.robinet.fermer { background: #1a0a0a; }
.robinet.fermer .robinet-label { color: var(--cramoisi-clair); }
.robinet p { color: var(--cendre-clair); line-height: 1.5; }

/* ---- POUVOIR ROYAL ---- */
.pouvoir-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 650px) { .pouvoir-grid { grid-template-columns: 1fr; } }

.pouvoir-card {
  background: #1a1409;
  border: 1px solid #c9922a22;
  border-top: 3px solid var(--or);
  padding: 2rem;
}

.pouvoir-card.danger { border-top-color: var(--cramoisi); }

.pouvoir-icon { font-size: 2.5rem; margin-bottom: 1rem; }

.pouvoir-card h3 {
  font-family: var(--font-display);
  color: var(--blanc-os);
  font-size: 1.05rem;
  margin-bottom: 1rem;
}

.pouvoir-card p { color: var(--cendre-clair); font-size: 1rem; line-height: 1.65; }
.pouvoir-card strong { color: var(--blanc-os); }

/* ---- FOOTER ---- */
.footer {
  text-align: center;
  padding: 3rem 1.5rem;
  border-top: 1px solid #c9922a18;
  font-family: var(--font-display);
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--cendre);
}</style>
</head>
<body>

  <!-- HERO -->
  <header class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <p class="eyebrow">Livre des Règles Officielles · Version Alpha-0.1</p>
      <h1>Intrigues<br/><span>&amp;</span> Couronne</h1>
      <p class="hero-sub">La frontière entre le dévouement et la haute trahison<br/>n'est dictée que par votre ambition.</p>
      <div class="hero-cta">
        <a href="#victoire" class="btn-primary">Lire les règles</a>
        <a href="#roles" class="btn-ghost">Les rôles</a>
      </div>
    </div>
    <div class="scroll-hint">↓</div>
  </header>

  <main>

    <!-- SECTION VICTOIRE -->
    <section id="victoire" class="section">
      <div class="container">
        <div class="section-label">01 — Objectif</div>
        <h2>Conditions de Victoire &amp; de Défaite</h2>
        <p class="section-intro">Le Royaume possède deux jauges globales suivies publiquement sur le plateau.</p>

        <div class="gauges-grid">
          <div class="gauge-card">
            <div class="gauge-icon">⚖️</div>
            <h3>Stabilité du Royaume</h3>
            <div class="gauge-bar"><div class="gauge-fill" style="width:72%"></div></div>
            <p>Jauge de 0 à 100. Si elle atteint <strong>0</strong>, c'est la révolte populaire : le Royaume s'effondre.</p>
          </div>
          <div class="gauge-card">
            <div class="gauge-icon">💰</div>
            <h3>Caisses de l'État</h3>
            <div class="gauge-bar"><div class="gauge-fill gold" style="width:55%"></div></div>
            <p>Or public. Si les caisses tombent <strong>en dessous de zéro</strong>, c'est la banqueroute collective.</p>
          </div>
        </div>

        <div class="ruin-block">
          <span class="ruin-icon">⚠️</span>
          <div>
            <strong>La Ruine Collective</strong>
            <p>Si l'une de ces deux jauges bascule à la fin d'un tour, <em>tous les joueurs perdent immédiatement la partie</em>. Le Royaume ne peut survivre sans ses gardiens.</p>
          </div>
        </div>

        <div class="victory-block">
          <h3>Si le Royaume survit aux 5 cycles…</h3>
          <p>Le décompte des points a lieu. La formule est universelle et équilibrée pour chaque rôle :</p>
          <div class="formula">
            Puissance = Or Personnel + Influence Accumulée + (Statut de Ministère × Stabilité Finale)
          </div>
          <p class="formula-note">Le joueur ayant la <strong>Puissance Politique</strong> la plus élevée est déclaré vainqueur.</p>
        </div>
      </div>
    </section>

    <!-- SECTION DYNAMIQUE -->
    <section id="dynamique" class="section section-dark">
      <div class="container">
        <div class="section-label light">02 — Mécanique</div>
        <h2>Dynamique Cognitive &amp; Charge de Travail</h2>
        <p class="section-intro light-text">Ici, aucune jauge artificielle ne limite vos actions. Le jeu est conçu pour générer une véritable <em>charge mentale</em>.</p>

        <div class="pillars-grid">
          <div class="pillar">
            <div class="pillar-num">I</div>
            <h4>Canaux secrets</h4>
            <p>Les informations ne circulent jamais ouvertement. Chaque confidence a un prix — ou un risque.</p>
          </div>
          <div class="pillar">
            <div class="pillar-num">II</div>
            <h4>Crises physiques</h4>
            <p>Les dossiers s'accumulent en main sous forme de cartes. Ignorer une crise trop longtemps, c'est la laisser grossir.</p>
          </div>
          <div class="pillar">
            <div class="pillar-num">III</div>
            <h4>Pression du Roi</h4>
            <p>Fermez un robinet trop longtemps et la colère royale vous poussera à l'erreur — ou à la démission.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION CONFIGURATIONS -->
    <section id="config" class="section">
      <div class="container">
        <div class="section-label">03 — Avant de jouer</div>
        <h2>Configurations par Nombre de Joueurs</h2>
        <p class="section-intro">Le Royaume s'adapte à votre cour. Les rôles sont introduits progressivement selon le nombre de joueurs.</p>

        <div class="config-tabs">
          {% for nb, conf in configs.items() %}
          <button class="config-tab {% if nb == 3 %}active{% endif %}" data-nb="{{ nb }}">{{ nb }} joueurs</button>
          {% endfor %}
        </div>

        <div class="config-panels">
          {% for nb, conf in configs.items() %}
          <div class="config-panel {% if nb == 3 %}active{% endif %}" data-nb="{{ nb }}">
            <p class="config-note">{{ conf.note }}</p>
            <div class="config-roles">
              {% for rid in conf.roles %}
              {% set role = roles_by_id[rid] %}
              <div class="config-role-chip">
                <span class="chip-icon">{{ role.icon }}</span>
                <span>{{ role.nom }}</span>
              </div>
              {% endfor %}
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </section>

    <!-- SECTION ROLES -->
    <section id="roles" class="section section-dark">
      <div class="container">
        <div class="section-label light">04 — Les Ministères</div>
        <h2>Les Rôles &amp; Leurs Vannes</h2>
        <p class="section-intro light-text">Chaque rôle contrôle un flux indispensable. Servez le Royaume — ou prospérez à ses dépens.</p>

        <div class="roles-grid">
          {% for role in roles %}
          <div class="role-card" data-role="{{ role.id }}">
            <div class="role-header">
              <span class="role-icon">{{ role.icon }}</span>
              <div>
                <h3>{{ role.nom }}</h3>
                <span class="role-badge">dès {{ role.min_joueurs }} joueurs</span>
              </div>
            </div>
            <div class="role-flux">
              <strong>Le Flux :</strong> {{ role.flux }}
            </div>
            <div class="role-voies">
              <div class="voie serviteur">
                <div class="voie-label">🕊️ Voie du Serviteur</div>
                <p>{{ role.serviteur }}</p>
              </div>
              <div class="voie fourbe">
                <div class="voie-label">🗡️ Voie du Fourbe</div>
                <p>{{ role.fourbe }}</p>
              </div>
            </div>
            <div class="robinets">
              <div class="robinet ouvrir">
                <div class="robinet-label">OUVRIR LE ROBINET</div>
                <p>{{ role.ouvrir }}</p>
              </div>
              <div class="robinet fermer">
                <div class="robinet-label">FERMER LE ROBINET</div>
                <p>{{ role.fermer }}</p>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </section>

    <!-- SECTION POUVOIR ROYAL -->
    <section id="roi" class="section">
      <div class="container">
        <div class="section-label">05 — Politique de cour</div>
        <h2>Révocation &amp; Démission</h2>

        <div class="pouvoir-grid">
          <div class="pouvoir-card">
            <div class="pouvoir-icon">👑</div>
            <h3>La Révocation Royale</h3>
            <p>Le Roi peut destituer un ministre soupçonné de trahison ou d'incompétence. Le poste vacant est alors attribué à <strong>un autre joueur désigné</strong> (hors Roi), qui cumule temporairement les deux portefeuilles ou délègue l'un d'eux.</p>
          </div>
          <div class="pouvoir-card danger">
            <div class="pouvoir-icon">💀</div>
            <h3>L'Arme de la Démission</h3>
            <p>Un ministre acculé par les dettes peut annoncer sa <strong>Démission</strong>. Sa charge de travail et ses crises en cours sont immédiatement attribuées à <strong>un seul autre joueur</strong> (hors Roi, désigné par le Roi ou à la majorité). Ce chaos provoque souvent un effet domino dévastateur — c'est le chantage ultime.</p>
          </div>
        </div>

        <div class="ruin-block" style="margin-top: 2rem;">
          <span class="ruin-icon">ℹ️</span>
          <div>
            <strong>Règle de succession</strong>
            <p>Lors d'une démission ou d'une révocation, le poste n'est jamais divisé entre plusieurs joueurs : il est confié <em>en entier</em> à une seule personne. Le Roi tranche en cas de désaccord.</p>
          </div>
        </div>
      </div>
    </section>

  </main>

  <footer class="footer">
    <p>Intrigues &amp; Couronne · Version Alpha-0.1 · Tous droits réservés</p>
  </footer>

  <script>
  /* ============================================================
   INTRIGUES & COURONNE — main.js
   ============================================================ */

// ---- Config tabs ----
document.querySelectorAll('.config-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const nb = tab.dataset.nb;

    document.querySelectorAll('.config-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.config-panel').forEach(p => p.classList.remove('active'));

    tab.classList.add('active');
    document.querySelector(`.config-panel[data-nb="${nb}"]`).classList.add('active');
  });
});

// ---- Scroll reveal ----
const revealEls = document.querySelectorAll(
  '.gauge-card, .role-card, .pillar, .pouvoir-card, .config-role-chip, .ruin-block, .victory-block'
);

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

revealEls.forEach(el => {
  el.classList.add('hidden-before-reveal');
  observer.observe(el);
});

// Inject reveal styles dynamically
const style = document.createElement('style');
style.textContent = `
  .hidden-before-reveal {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .hidden-before-reveal.revealed {
    opacity: 1;
    transform: translateY(0);
  }
`;
document.head.appendChild(style);

// ---- Gauge bar animation on scroll ----
const gaugeFills = document.querySelectorAll('.gauge-fill');
const gaugeObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = el.style.width;
      el.style.width = '0%';
      requestAnimationFrame(() => {
        setTimeout(() => { el.style.width = target; }, 100);
      });
      gaugeObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

gaugeFills.forEach(el => gaugeObserver.observe(el));

// ---- Active nav highlight on scroll (optional) ----
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 200) {
      current = section.getAttribute('id');
    }
  });
  // Can be used to highlight a nav if one is added later
  // document.querySelectorAll('a[href^="#"]').forEach(a => {
  //   a.classList.toggle('active', a.getAttribute('href') === '#' + current);
  // });
}, { passive: true });
  </script>
</body>
</html>"""
ROLES = [
    {
        "id": "roi",
        "nom": "Le Roi",
        "icon": "👑",
        "flux": "Le Pouvoir Suprême et l'Arbitrage. Il tranche les conflits, nomme et révoque les ministres, et oriente la stratégie du Royaume.",
        "serviteur": "Arbitrer avec sagesse, bénir les grandes décisions collectives et maintenir l'équilibre entre les ministères pour assurer la prospérité durable.",
        "fourbe": "Favoriser secrètement un ministre en échange de pots-de-vin, révoquant ses opposants sous prétexte d'incompétence pour consolider son réseau d'obligés.",
        "ouvrir": "Arbitre équitablement, débloque les crises diplomatiques entre ministres et accorde sa faveur royale pour booster la Stabilité.",
        "fermer": "Ignore volontairement les complots, laisse les ministres s'entre-déchirer et monnaye ses décrets, risquant l'anarchie totale à la cour.",
        "min_joueurs": 2,
    },
    {
        "id": "interieur",
        "nom": "Le Ministre de l'Intérieur",
        "icon": "📜",
        "flux": "L'Information et les Rapports de Crise. Il est le seul à piocher et lire le contenu réel des cartes d'événements du Royaume avant de les remonter au Roi.",
        "serviteur": "Communiquer fidèlement les crises, utiliser son influence pour étouffer les rumeurs et stabiliser le peuple en échange de gratifications royales.",
        "fourbe": "Falsifier les rapports (ex : annoncer qu'une crise coûte 50 d'or au lieu de 20), revendre les informations secrètes ou accepter des pots-de-vin des autres ministres pour embellir leur bilan face au Roi.",
        "ouvrir": "Transmet des rapports clairs, allège la pression sur ses collègues et permet d'anticiper les dangers.",
        "fermer": "Ment sur les menaces, fait chanter un ministre menacé de destitution, mais risque de provoquer l'explosion d'une crise imprévue.",
        "min_joueurs": 2,
    },
    {
        "id": "finances",
        "nom": "Le Surintendant des Finances",
        "icon": "🏦",
        "flux": "L'Or Public et les Investissements. Il valide et distribue les fonds nécessaires aux actions de tous les autres ministères.",
        "serviteur": "Faire fructifier les caisses par des investissements sains, ce qui déclenche des Primes de Performance étatiques majeures.",
        "fourbe": "Créer des lignes budgétaires fictives, prélever des taxes abusives non déclarées et remplir sa cassette personnelle.",
        "ouvrir": "Finance généreusement les projets et les campagnes militaires de ses pairs, assurant la prospérité globale.",
        "fermer": "Bloque les budgets sous prétexte d'austérité, asphyxie un rival politique, mais risque de provoquer une banqueroute technique ou des révoltes.",
        "min_joueurs": 3,
    },
    {
        "id": "aumônier",
        "nom": "Le Grand Aumônier",
        "icon": "⛪",
        "flux": "La Légitimité et la Ferveur Populaire. Il contrôle l'absolution morale et l'humeur spirituelle des masses.",
        "serviteur": "Bénir les décrets, calmer les grognes paysannes par la foi, ce qui maintient la Stabilité générale à un niveau élevé.",
        "fourbe": "Accuser ses rivaux d'hérésie pour bloquer leurs décrets, et monnayer de lourdes « indulgences » (pots-de-vin en or personnel) pour lever la punition.",
        "ouvrir": "Accorde sa caution morale aux actions douteuses des ministres, empêchant la baisse de Stabilité du Royaume.",
        "fermer": "Lance un interdit religieux sur un ministère, gelant ses capacités, au risque de voir le peuple détruire ses propres monastères par colère.",
        "min_joueurs": 4,
    },
    {
        "id": "subsistances",
        "nom": "Le Grand Maître des Subsistances",
        "icon": "🌾",
        "flux": "Le Ravitaillement et la Logistique. Il gère les greniers à blé et les convois indispensables à tout mouvement d'envergure.",
        "serviteur": "Assurer la distribution de nourriture dans les provinces, générant des rentes commerciales passives et stables.",
        "fourbe": "Stocker et spéculer sur le grain en période de disette pour faire exploser les prix au marché noir.",
        "ouvrir": "Nourrit les armées et les chantiers, permettant aux autres ministres d'agir à coût normal.",
        "fermer": "Affame une province ou coupe les vivres aux armées d'un rival, doublant le coût de ses actions, mais risque de voir le grain pourrir ou son ministère pillé.",
        "min_joueurs": 5,
    },
    {
        "id": "connetable",
        "nom": "Le Connétable",
        "icon": "🛡️",
        "flux": "La Maréchaussée et l'Exécution des Ordres. Il commande la garde royale et assure la sécurité physique au sein de la cour.",
        "serviteur": "Protéger les ministres des complots extérieurs et exécuter promptement les décrets d'arrestation du Roi.",
        "fourbe": "Fermer les yeux sur les tentatives de vol ou d'assassinat entre ministres en échange d'une commission, ou refuser d'escorter les décrets.",
        "ouvrir": "Maintient l'ordre absolu à la cour, protège les cassettes personnelles des joueurs et applique la loi.",
        "fermer": "Laisse planer l'anarchie, rend les autres vulnérables aux cartes d'action agressives, mais risque de laisser des brigands piller ses propres casernes.",
        "min_joueurs": 6,
    },
]

CONFIGS = {
    2: {"roles": ["roi", "interieur"], "note": "Partie duelle — tension maximale entre information et pouvoir."},
    3: {"roles": ["roi", "interieur", "finances"], "note": "Le triumvirat : chaque décision pèse lourd."},
    4: {"roles": ["roi", "interieur", "finances", "aumônier"], "note": "La cour s'élargit — la foi entre en jeu."},
    5: {"roles": ["roi", "interieur", "finances", "aumônier", "subsistances"], "note": "Le ravitaillement devient une arme stratégique."},
    6: {"roles": ["roi", "interieur", "finances", "aumônier", "subsistances", "connetable"], "note": "La cour complète — chaos et gloire à portée de main."},
}

@app.route("/")
def index():
    roles_by_id = {r["id"]: r for r in ROLES}
    return render_template_string(HTML, roles=ROLES, configs=CONFIGS, roles_by_id=roles_by_id)

if __name__ == "__main__":
    app.run(debug=True)

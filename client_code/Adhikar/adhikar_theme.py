/* Adhikar Theme — modern Indian aesthetic
Soft blue / orange palette, readable fonts, accessible sizes.
  Roles used across the app: navbar, card, headline, subhead, btn-filled, btn-outline, link, loader, container
    */

    /* Import a readable web font (works in Anvil if remote allowed) */
                                   @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

                                   :root {
    /* Palette */
    --adhikar-blue-500: #2563eb;   /* primary */
    --adhikar-blue-100: #e6f0ff;   /* light bg */
    --adhikar-orange-400: #fb923c; /* accent */
    --adhikar-gray-900: #0f172a;   /* main text */
    --adhikar-gray-600: #475569;   /* secondary text */
    --adhikar-bg: #f8fafc;         /* app background */
    --adhikar-card-bg: #ffffff;
    --adhikar-border: #e6eefc;

/* Sizing */
--radius-md: 12px;
--pad-xs: 6px;
--pad-sm: 10px;
--pad-md: 16px;
--pad-lg: 24px;

/* Typography */
--font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
--headline-size: 24px;
--subhead-size: 16px;
--body-size: 14px;
--muted-size: 13px;
}

/* Global app background + base text */
  body, .anvil-role-root {
  background: var(--adhikar-bg);
color: var(--adhikar-gray-900);
font-family: var(--font-sans);
font-size: var(--body-size);
line-height: 1.45;
}

/* Utility containers */
  .anvil-role-container, .container {
  max-width: 1100px;
margin-left: auto;
margin-right: auto;
padding-left: var(--pad-md);
padding-right: var(--pad-md);
}

/* NAVBAR */
.anvil-role-navbar, .navbar {
  background: linear-gradient(90deg, rgba(37,99,235,1) 0%, rgba(59,130,246,1) 100%);
color: white;
padding: 10px 16px;
border-bottom: 1px solid rgba(255,255,255,0.06);
display: flex;
align-items: center;
justify-content: space-between;
gap: 12px;
box-shadow: 0 2px 8px rgba(16,24,40,0.04);
}

/* Logo */
.anvil-role-navbar .logo {
  display: flex;
align-items: center;
gap: 10px;
font-weight: 700;
font-size: 18px;
}

/* Inline nav links for desktop */
  .anvil-role-nav-links {
  display: flex;
gap: 12px;
align-items: center;
}

/* Card */
.anvil-role-card, .card {
  background: var(--adhikar-card-bg);
border-radius: var(--radius-md);
padding: var(--pad-md);
box-shadow: 0 6px 18px rgba(15,23,42,0.05);
border: 1px solid var(--adhikar-border);
}

/* Headings */
.anvil-role-headline, .headline {
  font-size: var(--headline-size);
font-weight: 700;
color: var(--adhikar-gray-900);
margin: 0 0 8px 0;
}

.anvil-role-subhead, .subhead {
  font-size: var(--subhead-size);
font-weight: 600;
color: var(--adhikar-gray-900);
margin: 0 0 6px 0;
}

.anvil-role-muted {
  color: var(--adhikar-gray-600);
font-size: var(--muted-size);
}

/* Buttons */
.anvil-role-btn-filled, .btn-filled, button[role="filled-button"] {
  background: var(--adhikar-blue-500);
color: white;
border: none;
padding: 10px 16px;
border-radius: 10px;
font-weight: 600;
cursor: pointer;
box-shadow: 0 6px 12px rgba(37,99,235,0.12);
}
.anvil-role-btn-filled:hover {
  transform: translateY(-1px);
}

.anvil-role-btn-outline, .btn-outline, button[role="outlined-button"] {
  background: transparent;
color: var(--adhikar-blue-500);
border: 1px solid rgba(37,99,235,0.12);
padding: 8px 14px;
border-radius: 10px;
cursor: pointer;
font-weight: 600;
}

.link, a, .anvil-role-link {
  color: var(--adhikar-blue-500);
text-decoration: none;
}
.link:hover, a:hover { text-decoration: underline; }

/* Loader / spinner */
.anvil-role-loader, .loader {
  display: inline-block;
width: 28px;
height: 28px;
border-radius: 50%;
border: 4px solid rgba(37,99,235,0.14);
border-top-color: var(--adhikar-orange-400);
animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* Cards grid for results/laws */
  .anvil-role-cards-grid {
  display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 16px;
}
@media (max-width: 900px) {
.anvil-role-cards-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 540px) {
.anvil-role-cards-grid { grid-template-columns: 1fr; }
}

/* Small helpers */
.center { text-align: center; }
.small { font-size: 12px; color: var(--adhikar-gray-600); }

/* Input styling (TextBox, TextArea placeholders) */
input, textarea, .anvil-role-input {
  font-family: var(--font-sans);
font-size: var(--body-size);
padding: 10px 12px;
border-radius: 8px;
border: 1px solid #e6eefc;
background: white;
color: var(--adhikar-gray-900);
box-shadow: none;
outline: none;
}
input:focus, textarea:focus { border-color: rgba(37,99,235,0.6); box-shadow: 0 6px 16px rgba(37,99,235,0.06); }

/* Footer */
.anvil-role-footer {
  padding: var(--pad-md);
text-align: center;
color: var(--adhikar-gray-600);
font-size: 13px;
}

/* Accessibility tweaks */
button, .link, a { -webkit-tap-highlight-color: rgba(0,0,0,0.05); }

/* Minor utility spacing */
  .space-sm { height: 8px; }
    .space-md { height: 16px; }
      .space-lg { height: 24px; }

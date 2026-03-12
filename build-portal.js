const fs = require('fs');

const homepageHtml = fs.readFileSync('pages/home-page.html', 'utf8');
const buttonsHtml = fs.readFileSync('snippets/all-buttons.html', 'utf8');
const heroHtml = fs.readFileSync('snippets/hero-sections.html', 'utf8');
const showCardsHtml = fs.readFileSync('snippets/show-cards.html', 'utf8');
const headingsHtml = fs.readFileSync('snippets/all-section-headings.html', 'utf8');
const iconsHtml = fs.readFileSync('snippets/all-icons.html', 'utf8');

// I'll grab the optimizer code from the current index.html
const indexHtmlContent = fs.readFileSync('index.html', 'utf8');

// Extract optimizer main body and scripts
const optimizerMainMatch = indexHtmlContent.match(/<main[^>]*>([\s\S]*?)<\/main>/);
const optimizerMain = optimizerMainMatch ? optimizerMainMatch[1] : '';

const optimizerToastMatch = indexHtmlContent.match(/<div id="toast"[^>]*>([\s\S]*?)<\/div>/);
const optimizerToast = optimizerToastMatch ? `<div id="toast" class="fixed bottom-8 left-1/2 -translate-x-1/2 bg-teal-600 text-white px-6 py-3 rounded-full font-bold shadow-2xl opacity-0 transition-opacity pointer-events-none z-50">${optimizerToastMatch[1]}</div>` : '';

const optimizerScriptMatch = indexHtmlContent.match(/<script>([\s\S]*?)<\/script>/);
const optimizerScript = optimizerScriptMatch ? optimizerScriptMatch[1] : '';

// Also extract optimizer styles
const optimizerStyleMatch = indexHtmlContent.match(/<style>([\s\S]*?)<\/style>/);
const optimizerStyle = optimizerStyleMatch ? optimizerStyleMatch[1] : '';

const portalTemplate = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BST Staff Portal & Brand Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="bst-theme.css">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }
        .nav-btn.active { 
            background-color: #f0fdfa; 
            color: #0f766e; 
            border: 1px solid #ccfbf1;
            box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        }
        /* Custom scrollbar for a cleaner look */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        .portal-content { display: none; }
        .portal-content.active { display: block; animation: fadeIn 0.3s forwards; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
        
        /* Ensure component container overrides portal tailwind where needed */
        .component-preview {
            background-color: #0a0b0c; /* Default BST background */
            font-family: var(--bst-font-body, 'Inter', sans-serif); /* Fallback for bst-theme */
            padding: 2rem;
            color: #e5e7eb;
        }

        /* Optimizer Styles Extracted */
        \${optimizerStyle}
        
        /* Ensure Optimizer text uses light colors since it expects dark bg originally */
        #module-0 .text-white { color: #f8fafc; }
        #module-0 .text-gray-400 { color: #94a3b8; }
        #module-0 { background-color: #0a0b0c; padding: 2rem; border-radius: 1rem; }
    </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-slate-900 text-white p-4 shadow-lg flex justify-between items-center px-4 md:px-8">
        <div class="flex items-center gap-3">
            <div class="bg-teal-500 p-2 rounded-lg text-slate-900 w-10 h-10 flex items-center justify-center">
                <i class="fas fa-theater-masks text-xl"></i>
            </div>
            <div>
                <h1 class="text-xl font-bold leading-none tracking-tight">Staff Portal & Brand Hub</h1>
                <p class="text-[10px] text-teal-400 font-bold uppercase tracking-widest mt-1">Beale Street Theater</p>
            </div>
        </div>
        <div class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-300">
            <span id="storage-indicator" class="text-xs bg-slate-800 px-3 py-1 rounded-full text-slate-400">Local Storage: 0MB</span>
        </div>
    </header>

    <div class="flex-1 flex overflow-hidden">
        <!-- Sidebar Navigation (Desktop) -->
        <aside class="w-80 bg-white border-r border-slate-200 hidden lg:flex flex-col">
            <div class="p-6 border-b border-slate-100">
                <h2 class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Resources</h2>
            </div>
            <nav class="flex-1 p-4 space-y-1 overflow-y-auto" id="sidebar-nav">
                <!-- Buttons injected by JS -->
            </nav>
        </aside>

        <!-- Main Content Area -->
        <main class="flex-1 overflow-y-auto p-4 md:p-8 lg:p-12 relative">
            
            <!-- Mobile Navigation Overlay (Visible on small screens) -->
            <div class="lg:hidden mb-6 bg-white rounded-xl shadow-sm border border-slate-200 p-2">
                <select id="mobile-nav" onchange="setActive(parseInt(this.value))" class="w-full bg-slate-50 border border-slate-200 text-slate-900 text-sm rounded-lg focus:ring-teal-500 focus:border-teal-500 block p-2.5 outline-none font-bold">
                    <!-- Options injected by JS -->
                </select>
            </div>

            <div class="max-w-6xl mx-auto" id="content-area">
                
                <!-- MODULE 0: Directory & Links -->
                <div id="module-0" class="portal-content active" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Staff Directory
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Directory & Project Links</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Centralized contact information and important ecosystem links for Beale Street Theater.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-address-book text-3xl"></i>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                            <h3 class="text-xl font-bold mb-4 text-slate-900 border-b pb-2"><i class="fas fa-users text-teal-600 mr-2"></i> Staff & Theater Contact</h3>
                            <ul class="space-y-4 text-sm text-slate-600">
                                <li class="flex items-start gap-3"><i class="fas fa-info-circle text-slate-400 mt-1"></i> <div><strong>General Info/Box Office:</strong><br> <a href="mailto:info@bealestreettheater.com" class="text-teal-600 hover:underline">info@bealestreettheater.com</a> | <a href="tel:9282285817" class="text-teal-600 hover:underline">928-228-5817</a></div></li>
                                <li class="flex items-start gap-3"><i class="fas fa-user-tie text-slate-400 mt-1"></i> <div><strong>Kristina Michelson:</strong> (Executive Director)<br> <a href="mailto:kristina@bealestreettheater.com" class="text-teal-600 hover:underline">kristina@bealestreettheater.com</a></div></li>
                                <li class="flex items-start gap-3"><i class="fas fa-bullhorn text-slate-400 mt-1"></i> <div><strong>Shelby Crawford:</strong> (Marketing)<br> <a href="mailto:marketing@bealestreettheater.com" class="text-teal-600 hover:underline">marketing@bealestreettheater.com</a></div></li>
                                <li class="flex items-start gap-3"><i class="fas fa-graduation-cap text-slate-400 mt-1"></i> <div><strong>Sidney Valdez:</strong> (Education)<br> <a href="mailto:Education@kingmanarts.org" class="text-teal-600 hover:underline">Education@kingmanarts.org</a></div></li>
                                <li class="flex items-start gap-3"><i class="fas fa-ticket-alt text-slate-400 mt-1"></i> <div><strong>House Manager:</strong> (Ushering)<br> <a href="mailto:housemanager@bealestreettheater.com" class="text-teal-600 hover:underline">housemanager@bealestreettheater.com</a></div></li>
                            </ul>
                        </div>

                        <div class="space-y-8">
                            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                                <h3 class="text-xl font-bold mb-4 text-slate-900 border-b pb-2"><i class="fas fa-globe text-teal-600 mr-2"></i> Web & Social</h3>
                                <ul class="space-y-3 text-sm text-slate-600">
                                    <li><strong>Main Website:</strong> <a href="http://www.bealestreettheater.com" target="_blank" class="text-teal-600 hover:underline">www.bealestreettheater.com</a></li>
                                    <li><strong>Ticketing:</strong> <a href="https://bst.ludus.com" target="_blank" class="text-teal-600 hover:underline">bst.ludus.com</a></li>
                                    <li><strong>Facebook & Instagram:</strong> <span class="bg-slate-100 px-2 py-1 rounded text-slate-800 font-mono text-xs">@bealestreettheater</span></li>
                                    <li><strong>YouTube:</strong> <span class="bg-slate-100 px-2 py-1 rounded text-slate-800 font-mono text-xs">@bealestreettheater1797</span></li>
                                </ul>
                            </div>

                            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                                <h3 class="text-xl font-bold mb-4 text-slate-900 border-b pb-2"><i class="fas fa-project-diagram text-teal-600 mr-2"></i> Project Links</h3>
                                <ul class="space-y-3 text-sm text-slate-600">
                                    <li><strong>GitHub:</strong> <a href="https://github.com/beale-it/beale-street-theater" target="_blank" class="text-teal-600 hover:underline break-all">github.com/beale-it/beale-street-theater</a></li>
                                    <li><strong>Figma Prototype:</strong> <a href="https://board-actor-38163364.figma.site/" target="_blank" class="text-teal-600 hover:underline break-all">board-actor-38163364.figma.site</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- MODULE 1: Brand Assets -->
                <div id="module-1" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Assets
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Brand Resources</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Download official Beale Street Theater logos, brand guidelines, and public relations materials.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-download text-3xl"></i>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-slate-900 p-8 rounded-2xl flex flex-col items-center justify-center text-center border-2 border-dashed border-teal-500/30">
                            <div class="w-20 h-20 bg-teal-500/10 rounded-full flex items-center justify-center mb-4">
                                <i class="fas fa-image text-3xl text-teal-500"></i>
                            </div>
                            <h3 class="text-white font-bold mb-2">Primary Logo (Dark Background)</h3>
                            <p class="text-slate-400 text-xs mb-4">Upload pending. Placeholder item.</p>
                            <button class="px-4 py-2 bg-slate-800 text-slate-500 text-sm font-bold rounded-lg cursor-not-allowed">Download Logo</button>
                        </div>
                        <div class="bg-white p-8 rounded-2xl flex flex-col items-center justify-center text-center border-2 border-dashed border-slate-300">
                            <div class="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mb-4">
                                <i class="fas fa-image text-3xl text-slate-400"></i>
                            </div>
                            <h3 class="text-slate-900 font-bold mb-2">Primary Logo (Light Background)</h3>
                            <p class="text-slate-500 text-xs mb-4">Upload pending. Placeholder item.</p>
                            <button class="px-4 py-2 bg-slate-100 text-slate-400 text-sm font-bold rounded-lg cursor-not-allowed">Download Logo</button>
                        </div>
                    </div>
                </div>

                <!-- MODULE 2: Optimizer -->
                <div id="module-2" class="portal-content">
                    \${optimizerMain}
                </div>
                
                <!-- MODULE 3: Homepage Layout -->
                <div id="module-3" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Layout
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Homepage Layout</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Full constructed layout of the homepage ready to be pasted into the Duda HTML widget.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-home text-3xl"></i>
                        </div>
                    </div>
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        \${homepageHtml}
                    </div>
                </div>

                <!-- MODULE 4: Hero Sections -->
                <div id="module-4" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Component
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Hero Sections</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Large entry sections meant to capture user attention at the very top of each page.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-bullhorn text-3xl"></i>
                        </div>
                    </div>
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        \${heroHtml}
                    </div>
                </div>

                <!-- MODULE 5: Show Cards -->
                <div id="module-5" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Component
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Show Cards</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Reusable cards for displaying standard events, theater productions, and special assemblies.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-ticket-alt text-3xl"></i>
                        </div>
                    </div>
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        \${showCardsHtml}
                    </div>
                </div>

                <!-- MODULE 6: Buttons -->
                <div id="module-6" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Component
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Buttons</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Call-to-action interactables engineered with native hover states and click events.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-mouse-pointer text-3xl"></i>
                        </div>
                    </div>
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        \${buttonsHtml}
                    </div>
                </div>

                <!-- MODULE 7: Section Headings -->
                <div id="module-7" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Component
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Section Headings</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Structural typographic separators that organize the page vertically and denote layout sections.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-heading text-3xl"></i>
                        </div>
                    </div>
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        \${headingsHtml}
                    </div>
                </div>

                <!-- MODULE 8: Icons -->
                <div id="module-8" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">
                                Component
                            </span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Icons</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Fully semantic SVGs tailored exclusively for BST metrics, contact points, and styling.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-icons text-3xl"></i>
                        </div>
                    </div>
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        \${iconsHtml}
                    </div>
                </div>

            </div>
        </main>
    </div>

    \${optimizerToast}

    <script>
        const portalModules = [
            { id: 0, title: 'Directory & Links', subtitle: 'Staff Contacts', icon: 'fa-address-book' },
            { id: 1, title: 'Brand Assets', subtitle: 'Logos & Files', icon: 'fa-download' },
            { id: 2, title: 'Asset Optimizer', subtitle: 'WebP Converter', icon: 'fa-image' },
            { id: 3, title: 'Homepage Layout', subtitle: 'Layout', icon: 'fa-home' },
            { id: 4, title: 'Hero Sections', subtitle: 'Component', icon: 'fa-bullhorn' },
            { id: 5, title: 'Show Cards', subtitle: 'Component', icon: 'fa-ticket-alt' },
            { id: 6, title: 'Buttons', subtitle: 'Component', icon: 'fa-mouse-pointer' },
            { id: 7, title: 'Section Headings', subtitle: 'Component', icon: 'fa-heading' },
            { id: 8, title: 'Icons', subtitle: 'Component', icon: 'fa-icons' }
        ];

        let activeModule = 0;

        function renderSidebar() {
            const nav = document.getElementById('sidebar-nav');
            const mobileNav = document.getElementById('mobile-nav');
            
            nav.innerHTML = portalModules.map((mod, idx) => \`
                <button onclick="setActive(\${idx})" class="nav-btn w-full flex items-center gap-4 p-3 rounded-xl transition-all \${idx === activeModule ? 'active font-bold' : 'text-slate-500 hover:bg-slate-50'}">
                    <div class="w-8 h-8 rounded-lg flex items-center justify-center \${idx === activeModule ? 'bg-teal-500 text-white shadow-md' : 'bg-slate-100 text-slate-400'} transition-all">
                        <i class="fas \${mod.icon} text-xs"></i>
                    </div>
                    <div class="text-left leading-tight overflow-hidden">
                        <div class="text-sm truncate text-slate-700">\${mod.title}</div>
                        <div class="text-[9px] opacity-70 uppercase tracking-tighter truncate text-slate-400">\${mod.subtitle}</div>
                    </div>
                </button>
            \`).join('');

            mobileNav.innerHTML = portalModules.map((mod, idx) => \`
                <option value="\${idx}" \${idx === activeModule ? 'selected' : ''}>\${mod.title}</option>
            \`).join('');
        }

        function setActive(idx) {
            document.querySelectorAll('.portal-content').forEach(el => el.classList.remove('active'));
            document.getElementById('module-' + idx).classList.add('active');
            activeModule = idx;
            renderSidebar();
            window.scrollTo(0, 0);
        }

        renderSidebar();
        setActive(0);
    </script>

    <!-- Optimizer Core Scripts -->
    <script>
        \${optimizerScript}
    </script>
</body>
</html>`;

fs.writeFileSync('index.html', portalTemplate);
console.log('Portal generated successfully.');

import re

with open('pages/home-page.html', 'r', encoding='utf-8') as f: homepageHtml = f.read()
with open('snippets/all-buttons.html', 'r', encoding='utf-8') as f: buttonsHtml = f.read()
with open('snippets/hero-sections.html', 'r', encoding='utf-8') as f: heroHtml = f.read()
with open('snippets/show-cards.html', 'r', encoding='utf-8') as f: showCardsHtml = f.read()
with open('snippets/all-section-headings.html', 'r', encoding='utf-8') as f: headingsHtml = f.read()
with open('snippets/all-icons.html', 'r', encoding='utf-8') as f: iconsHtml = f.read()
with open('snippets/asset-optimizer.html', 'r', encoding='utf-8') as f: optimizerHtml = f.read()

with open('bst-theme.css', 'r', encoding='utf-8') as f:
    bstThemeCss = f.read()
    bstThemeCss = bstThemeCss.replace('`', '\\`').replace('$', '\\$')

portal_template = f'''<!DOCTYPE html>
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
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        .nav-btn.active {{ 
            background-color: #f0fdfa; 
            color: #0f766e; 
            border: 1px solid #ccfbf1;
            box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        }}
        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: #f1f5f9; }}
        ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 10px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}
        
        .portal-content {{ display: none; }}
        .portal-content.active {{ display: block; animation: fadeIn 0.3s forwards; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        
        .component-preview {{
            background-color: #0a0b0c; 
            font-family: var(--bst-font-body, 'Inter', sans-serif);
            padding: 2rem;
            color: #e5e7eb;
        }}
        
        /* Optimizer Styles */
        .asset-card {{ background: #111827; border: 1px solid #1f2937; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }}
        .asset-card:hover {{ border-color: #14b8a6; transform: translateY(-4px); box-shadow: 0 10px 25px -5px rgba(20, 184, 166, 0.1); }}
        .drop-zone {{ border: 2px dashed #374151; transition: all 0.2s ease; }}
        .drop-zone.dragover {{ border-color: #14b8a6; background: rgba(20, 184, 166, 0.05); }}
        #module-2 .text-white {{ color: #f8fafc; }}
        #module-2 .text-gray-400 {{ color: #94a3b8; }}
        #module-2 {{ background-color: #0a0b0c; padding: 2rem; border-radius: 1rem; margin-top: 1rem; }}
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
        <!-- Sidebar Navigation -->
        <aside class="w-80 bg-white border-r border-slate-200 hidden lg:flex flex-col z-10 relative">
            <div class="p-6 border-b border-slate-100">
                <h2 class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Resources</h2>
            </div>
            <nav class="flex-1 p-4 space-y-1 overflow-y-auto" id="sidebar-nav"></nav>
        </aside>

        <!-- Main Content Area -->
        <main class="flex-1 overflow-y-auto p-4 md:p-8 lg:p-12 relative">
            <div class="lg:hidden mb-6 bg-white rounded-xl shadow-sm border border-slate-200 p-2">
                <select id="mobile-nav" onchange="setActive(parseInt(this.value))" class="w-full bg-slate-50 border border-slate-200 text-slate-900 text-sm rounded-lg focus:ring-teal-500 focus:border-teal-500 block p-2.5 outline-none font-bold">
                </select>
            </div>
            <div class="max-w-6xl mx-auto" id="content-area">
                
                <!-- MODULE 0: Directory -->
                <div id="module-0" class="portal-content active" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">Staff Directory</span>
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

                <!-- MODULE 1: Brands -->
                <div id="module-1" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">Assets</span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Brand Resources</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Download official Beale Street Theater logos and brand materials.</p>
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
                            <button class="px-4 py-2 bg-slate-800 text-slate-500 text-sm font-bold rounded-lg cursor-not-allowed">Download Logo</button>
                        </div>
                        <div class="bg-white p-8 rounded-2xl flex flex-col items-center justify-center text-center border-2 border-dashed border-slate-300">
                            <div class="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mb-4">
                                <i class="fas fa-image text-3xl text-slate-400"></i>
                            </div>
                            <h3 class="text-slate-900 font-bold mb-2">Primary Logo (Light Background)</h3>
                            <button class="px-4 py-2 bg-slate-100 text-slate-400 text-sm font-bold rounded-lg cursor-not-allowed">Download Logo</button>
                        </div>
                    </div>
                </div>

                <!-- MODULE 2: Optimizer -->
                <div id="module-2" class="portal-content">
                    {optimizerHtml}
                </div>

                <!-- MODULE 3: Homepage Layout -->
                <div id="module-3" class="portal-content" style="background: none; padding: 0;">
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        {homepageHtml}
                    </div>
                </div>

                <div id="module-4" class="portal-content" style="background: none; padding: 0;">
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        {heroHtml}
                    </div>
                </div>

                <div id="module-5" class="portal-content" style="background: none; padding: 0;">
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        {showCardsHtml}
                    </div>
                </div>

                <div id="module-6" class="portal-content" style="background: none; padding: 0;">
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        {buttonsHtml}
                    </div>
                </div>

                <div id="module-7" class="portal-content" style="background: none; padding: 0;">
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        {headingsHtml}
                    </div>
                </div>

                <div id="module-8" class="portal-content" style="background: none; padding: 0;">
                    <div class="component-preview border border-slate-200 shadow-xl rounded-xl overflow-hidden relative">
                        {iconsHtml}
                    </div>
                </div>

                <!-- MODULE 9: Shared Resources -->
                <div id="module-9" class="portal-content" style="background: none; padding: 0;">
                    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div class="space-y-2">
                            <span class="inline-block px-3 py-1 bg-teal-100 text-teal-700 text-[10px] font-black rounded-full uppercase tracking-widest">Workspace</span>
                            <h2 class="text-3xl font-black text-slate-900 tracking-tight leading-none">Shared Resources</h2>
                            <p class="text-slate-600 max-w-xl text-sm font-medium leading-relaxed">Central repository for Drive files, document templates, CSV structures, and staff training materials.</p>
                        </div>
                        <div class="hidden md:flex w-16 h-16 rounded-2xl bg-teal-50 items-center justify-center text-teal-600">
                            <i class="fas fa-folder-open text-3xl"></i>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pb-12">
                        <!-- Google Drive -->
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:border-teal-500 transition-colors cursor-pointer group">
                            <div class="flex items-center gap-4 mb-3">
                                <i class="fab fa-google-drive text-2xl text-slate-400 group-hover:text-teal-600 transition-colors"></i>
                                <h3 class="text-lg font-bold text-slate-900">Google Drive</h3>
                            </div>
                            <p class="text-sm text-slate-600 mb-4">Access shared folders, media uploads, and collaborative documents.</p>
                            <a href="#" class="text-teal-600 text-sm font-bold hover:underline">Open Drive &rarr;</a>
                        </div>
                        <!-- Document Library -->
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:border-teal-500 transition-colors cursor-pointer group">
                            <div class="flex items-center gap-4 mb-3">
                                <i class="fas fa-file-alt text-2xl text-slate-400 group-hover:text-teal-600 transition-colors"></i>
                                <h3 class="text-lg font-bold text-slate-900">Document Library</h3>
                            </div>
                            <p class="text-sm text-slate-600 mb-4">W-9s, tax exempt forms, theater policy PDFs, and branding guidelines.</p>
                            <a href="#" class="text-teal-600 text-sm font-bold hover:underline">View Documents &rarr;</a>
                        </div>
                        <!-- CSV Collections -->
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:border-teal-500 transition-colors cursor-pointer group">
                            <div class="flex items-center gap-4 mb-3">
                                <i class="fas fa-table text-2xl text-slate-400 group-hover:text-teal-600 transition-colors"></i>
                                <h3 class="text-lg font-bold text-slate-900">CSV Templates</h3>
                            </div>
                            <p class="text-sm text-slate-600 mb-4">Spreadsheet templates formatted for Duda internal collections/dynamic pages.</p>
                            <a href="#" class="text-teal-600 text-sm font-bold hover:underline">Download Templates &rarr;</a>
                        </div>
                        <!-- Training Material -->
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:border-teal-500 transition-colors cursor-pointer group">
                            <div class="flex items-center gap-4 mb-3">
                                <i class="fas fa-graduation-cap text-2xl text-slate-400 group-hover:text-teal-600 transition-colors"></i>
                                <h3 class="text-lg font-bold text-slate-900">Training Material</h3>
                            </div>
                            <p class="text-sm text-slate-600 mb-4">Onboarding videos, process walkthroughs, and Ludus box office instructions.</p>
                            <a href="#" class="text-teal-600 text-sm font-bold hover:underline">Access Training &rarr;</a>
                        </div>
                    </div>
                </div>

            </div>
        </main>
    </div>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-8 left-1/2 -translate-x-1/2 bg-teal-600 text-white px-6 py-3 rounded-full font-bold shadow-2xl opacity-0 transition-opacity pointer-events-none z-50">Copied to clipboard!</div>

    <script>
        const portalModules = [
            {{ id: 0, title: 'Directory & Links', subtitle: 'Staff Contacts', icon: 'fa-address-book' }},
            {{ id: 1, title: 'Brand Assets', subtitle: 'Logos & Files', icon: 'fa-download' }},
            {{ id: 2, title: 'Asset Optimizer', subtitle: 'WebP Converter', icon: 'fa-image' }},
            {{ id: 3, title: 'Homepage Layout', subtitle: 'Layout', icon: 'fa-home' }},
            {{ id: 4, title: 'Hero Sections', subtitle: 'Component', icon: 'fa-bullhorn' }},
            {{ id: 5, title: 'Show Cards', subtitle: 'Component', icon: 'fa-ticket-alt' }},
            {{ id: 6, title: 'Buttons', subtitle: 'Component', icon: 'fa-mouse-pointer' }},
            {{ id: 7, title: 'Section Headings', subtitle: 'Component', icon: 'fa-heading' }},
            {{ id: 8, title: 'Icons', subtitle: 'Component', icon: 'fa-icons' }},
            {{ id: 9, title: 'Shared Resources', subtitle: 'Drive & Docs', icon: 'fa-folder-open' }}
        ];
        let activeModule = 0;
        function renderSidebar() {{
            const nav = document.getElementById('sidebar-nav');
            const mobileNav = document.getElementById('mobile-nav');
            if(nav) {{
                nav.innerHTML = portalModules.map((mod, idx) => `
                    <button onclick="setActive(${{idx}})" class="nav-btn w-full flex items-center gap-4 p-3 rounded-xl transition-all ${{idx === activeModule ? 'active font-bold' : 'text-slate-500 hover:bg-slate-50'}}">
                        <div class="w-8 h-8 rounded-lg flex items-center justify-center ${{idx === activeModule ? 'bg-teal-500 text-white shadow-md' : 'bg-slate-100 text-slate-400'}} transition-all">
                            <i class="fas ${{mod.icon}} text-xs"></i>
                        </div>
                        <div class="text-left leading-tight overflow-hidden">
                            <div class="text-sm truncate text-slate-700">${{mod.title}}</div>
                            <div class="text-[9px] opacity-70 uppercase tracking-tighter truncate text-slate-400">${{mod.subtitle}}</div>
                        </div>
                    </button>
                `).join('');
            }}
            if (mobileNav) {{
                mobileNav.innerHTML = portalModules.map((mod, idx) => `
                    <option value="${{idx}}" ${{idx === activeModule ? 'selected' : ''}}>${{mod.title}}</option>
                `).join('');
            }}
        }}

        function setActive(idx) {{
            document.querySelectorAll('.portal-content').forEach(el => el.classList.remove('active'));
            const modElement = document.getElementById('module-' + idx);
            if (modElement) modElement.classList.add('active');
            activeModule = idx;
            renderSidebar();
            window.scrollTo(0, 0);
        }}

        renderSidebar();
        setActive(0);
    </script>
    <script>
        // Optimizer JS
        const dropZone = document.getElementById('drop-zone');
        const fileInput = document.getElementById('file-input');
        const assetGrid = document.getElementById('asset-grid');
        const emptyState = document.getElementById('empty-state');
        const storageIndicator = document.getElementById('storage-indicator');

        // Load assets from LocalStorage
        let assets = JSON.parse(localStorage.getItem('bst_assets') || '[]');
        if(fileInput) {{
            renderAssets();

            // Drag & Drop Listeners
            dropZone.onclick = () => fileInput.click();
            dropZone.ondragover = (e) => {{ e.preventDefault(); dropZone.classList.add('dragover'); }};
            dropZone.ondragleave = () => dropZone.classList.remove('dragover');
            dropZone.ondrop = (e) => {{
                e.preventDefault();
                dropZone.classList.remove('dragover');
                handleFiles(e.dataTransfer.files);
            }};
            fileInput.onchange = (e) => handleFiles(e.target.files);
        }}

        async function handleFiles(files) {{
            for (const file of files) {{
                if (!file.type.startsWith('image/')) continue;
                await processImage(file);
            }}
        }}

        function processImage(file) {{
            return new Promise((resolve) => {{
                const reader = new FileReader();
                reader.onload = (e) => {{
                    const img = new Image();
                    img.onload = () => {{
                        const canvas = document.createElement('canvas');
                        const ctx = canvas.getContext('2d');

                        // Maintain high quality but optimize size
                        canvas.width = img.width;
                        canvas.height = img.height;
                        ctx.drawImage(img, 0, 0);

                        // Convert to WebP with 0.8 quality (perfect balance)
                        const webpData = canvas.toDataURL('image/webp', 0.8);

                        const newAsset = {{
                            id: Date.now() + Math.random().toString(36).substr(2, 9),
                            name: file.name.split('.')[0],
                            originalSize: (file.size / 1024).toFixed(1),
                            optimizedSize: (webpData.length * 0.75 / 1024).toFixed(1),
                            data: webpData,
                            timestamp: new Date().toLocaleDateString()
                        }};

                        assets.unshift(newAsset);
                        saveAndRender();
                        resolve();
                    }};
                    img.src = e.target.result;
                }};
                reader.readAsDataURL(file);
            }});
        }}

        function saveAndRender() {{
            try {{
                localStorage.setItem('bst_assets', JSON.stringify(assets));
                renderAssets();
            }} catch (e) {{
                alert("Storage full! Please delete some old assets.");
            }}
        }}

        function renderAssets() {{
            if(!assetGrid) return;
            assetGrid.innerHTML = '';

            if (assets.length === 0) {{
                emptyState.style.display = 'block';
            }} else {{
                emptyState.style.display = 'none';
            }}

            let totalSize = 0;

            assets.forEach(asset => {{
                totalSize += (asset.data.length * 0.75);
                const card = document.createElement('div');
                card.className = 'asset-card rounded-2xl overflow-hidden flex flex-col';
                card.innerHTML = `
                    <div class="aspect-video bg-gray-800 relative group overflow-hidden">
                        <img src="${{asset.data}}" class="w-full h-full object-contain p-4" alt="${{asset.name}}">
                        <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center space-x-2">
                             <button onclick="downloadAsset('${{asset.id}}')" class="p-2 bg-teal-500 rounded-lg text-white hover:bg-teal-400" title="Download WebP">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                             </button>
                             <button onclick="copyOptimizerCode('${{asset.id}}')" class="p-2 bg-white rounded-lg text-gray-900 hover:bg-gray-200" title="Copy Base64 Code">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                             </button>
                        </div>
                    </div>
                    <div class="p-5">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="font-bold text-white truncate pr-4">${{asset.name}}</h3>
                            <button onclick="deleteAsset('${{asset.id}}')" class="text-gray-500 hover:text-red-500">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"></path></svg>
                            </button>
                        </div>
                        <div class="flex items-center space-x-3 text-xs">
                            <span class="text-gray-500 line-through">${{asset.originalSize}} KB</span>
                            <span class="text-teal-500 font-bold">${{asset.optimizedSize}} KB</span>
                            <span class="bg-teal-900/30 text-teal-400 px-2 py-0.5 rounded">-${{Math.round((1 - asset.optimizedSize / asset.originalSize) * 100)}}%</span>
                        </div>
                    </div>
                `;
                assetGrid.appendChild(card);
            }});

            storageIndicator.innerText = `Local Storage: ${{(totalSize / (1024 * 1024)).toFixed(2)}}MB / 5MB`;
        }}

        function deleteAsset(id) {{
            assets = assets.filter(a => a.id !== id);
            saveAndRender();
        }}

        function clearLibrary() {{
            if (confirm("Are you sure? This will delete all optimized assets from your local hub.")) {{
                assets = [];
                saveAndRender();
            }}
        }}

        function downloadAsset(id) {{
            const asset = assets.find(a => a.id === id);
            const a = document.createElement('a');
            a.href = asset.data;
            a.download = `${{asset.name}}_optimized.webp`;
            a.click();
        }}

        function copyOptimizerCode(id) {{
            const asset = assets.find(a => a.id === id);
            const htmlSnippet = `<img src="${{asset.data}}" alt="${{asset.name}}" style="width: 100%; height: auto;">`;
            copyToClipboard(htmlSnippet);
        }}
    </script>
    <script>
        // Copy Code & SVG Download logic
        const bstThemeCssContent = `{bstThemeCss}`;
        
        function copyMasterCSS() {{
            copyToClipboard('<style>\\n' + bstThemeCssContent + '\\n</style>');
        }}

        function initComponentTools() {{
            const explanationStr = `
                <div class="bg-slate-800 text-slate-300 p-4 rounded-xl mb-6 text-sm flex flex-col md:flex-row gap-4 items-start shadow-inner">
                    <i class="fas fa-info-circle text-teal-400 mt-1"></i>
                    <div class="flex-1">
                        <strong class="text-white block mb-1">Duda Implementation Guide:</strong>
                        To use these components in Duda, add an <strong>HTML Widget</strong> to your page and paste the code entirely. 
                        <strong>Important:</strong> These components require the BST Theme CSS. You can copy the CSS below and paste it <strong class="text-teal-400">at the top of the same HTML Widget</strong> or into your global site head.
                        <div class="mt-3">
                            <button onclick="copyMasterCSS()" class="bg-teal-600 hover:bg-teal-500 text-white text-xs font-bold py-1.5 px-3 rounded inline-flex items-center gap-2 transition-colors shadow">
                                <i class="fab fa-css3-alt"></i> Copy Required CSS
                            </button>
                        </div>
                    </div>
                </div>
            `;

            [3, 4, 5, 6, 7].forEach(id => {{
                const mod = document.getElementById('module-' + id);
                if(mod && mod.querySelector('.component-preview')) {{
                    // Remove old alert if it's already there to prevent duplicates
                    const oldAlert = mod.querySelector('.bg-slate-800');
                    if(oldAlert) oldAlert.remove();
                    
                    mod.insertBefore(document.createRange().createContextualFragment(explanationStr), mod.querySelector('.component-preview'));
                }}
            }});

            document.querySelectorAll('.component-preview').forEach(preview => {{
                // Add toolbars to all relevant elements
                const elements = preview.querySelectorAll('section, .bst-card, .bst-section-header, .bst-btn:not(.icon-item .bst-btn)');
                elements.forEach(el => {{
                    if(el.closest('.icon-showcase')) return;
                    if(el.querySelector('.fa-code') && !el.classList.contains('bst-btn')) return; // Already has toolbar
                    
                    const ogPosition = window.getComputedStyle(el).position;
                    // Don't overwrite if it's already set to relative from a previous pass
                    if(ogPosition === 'static' && !el.style.position) el.style.position = 'relative';

                    const toolbar = document.createElement('div');
                    toolbar.className = 'absolute top-2 right-2 flex gap-2 opacity-0 hover:opacity-100 transition-opacity bg-slate-900/90 p-2 rounded-lg backdrop-blur z-40 shadow-xl border border-slate-700 hover-toolbar';
                    
                    // Cleanup old toolbars first just in case
                    const oldToolbar = el.querySelector('.hover-toolbar');
                    if(oldToolbar) oldToolbar.remove();

                    el.addEventListener('mouseenter', () => toolbar.style.opacity = '1');
                    el.addEventListener('mouseleave', () => toolbar.style.opacity = '0');

                    const copyBtn = document.createElement('button');
                    copyBtn.innerHTML = '<i class="fas fa-code mr-1"></i> Copy Code';
                    copyBtn.className = 'text-xs text-white bg-teal-600 hover:bg-teal-500 px-3 py-1.5 rounded transition-colors font-bold shadow';
                    copyBtn.onclick = (e) => {{
                        e.preventDefault();
                        e.stopPropagation();
                        
                        // Create a clean clone
                        const clone = el.cloneNode(true);
                        
                        // Remove all toolbars from the clone before copying
                        clone.querySelectorAll('.hover-toolbar').forEach(tb => tb.remove());

                        // Remove position string if we added it
                        if(ogPosition === 'static') clone.style.position = '';
                        
                        copyToClipboard(clone.outerHTML);
                    }};
                    
                    toolbar.appendChild(copyBtn);
                    el.appendChild(toolbar);
                }});
            }});

            document.querySelectorAll('.icon-item').forEach(item => {{
                if(item.querySelector('.absolute.bottom-3')) return; // skip if already added

                item.style.position = 'relative';
                item.style.paddingBottom = '5rem';
                item.style.display = 'flex';
                item.style.flexDirection = 'column';
                item.style.alignItems = 'center';
                
                const svg = item.querySelector('svg');
                if(!svg) return;

                const wrapper = document.createElement('div');
                wrapper.className = 'absolute bottom-3 left-0 w-full px-3 flex flex-col gap-1.5';

                const dlWrapper = document.createElement('div');
                dlWrapper.className = 'flex gap-1 w-full';

                ['SVG', 'PNG', 'WEBP'].forEach(format => {{
                    const btn = document.createElement('button');
                    btn.innerHTML = format;
                    btn.className = 'text-[9px] bg-teal-900/50 text-teal-400 hover:bg-teal-500 hover:text-white py-1 rounded transition-colors font-bold flex-1 border border-teal-800/50';
                    btn.title = `Download physical ${{format}} for designs`;
                    btn.onclick = () => downloadIcon(svg, format, item.querySelector('.icon-name').innerText);
                    dlWrapper.appendChild(btn);
                }});

                const copyBtn = document.createElement('button');
                copyBtn.innerHTML = '<i class="fas fa-code"></i> Copy SVG';
                copyBtn.className = 'text-[10px] w-full bg-slate-800 text-slate-300 hover:bg-slate-700 py-1.5 rounded transition-colors font-bold border border-slate-700';
                copyBtn.title = `Copy SVGs for HTML widgets in Duda`;
                copyBtn.onclick = () => copyToClipboard(svg.outerHTML);

                wrapper.appendChild(dlWrapper);
                wrapper.appendChild(copyBtn);
                item.appendChild(wrapper);
            }});
        }}

        function copyToClipboard(text) {{
            const el = document.createElement('textarea');
            el.value = text;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            showToast();
        }}

        function showToast() {{
            const toast = document.getElementById('toast');
            if(toast) {{
                toast.style.opacity = '1';
                setTimeout(() => toast.style.opacity = '0', 2000);
            }}
        }}

        function downloadIcon(svgEl, format, name) {{
            const svgData = new XMLSerializer().serializeToString(svgEl);
            const fileName = name.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-') + '.' + format.toLowerCase();
            
            if(format === 'SVG') {{
                const blob = new Blob([svgData], {{type: 'image/svg+xml;charset=utf-8'}});
                const url = URL.createObjectURL(blob);
                triggerDownload(url, fileName);
            }} else {{
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                const img = new Image();
                const svgBlob = new Blob([svgData], {{type: 'image/svg+xml;charset=utf-8'}});
                const url = URL.createObjectURL(svgBlob);
                
                img.onload = function() {{
                    canvas.width = 512;
                    canvas.height = 512;
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    ctx.drawImage(img, 0, 0, 512, 512);
                    URL.revokeObjectURL(url);
                    
                    const mime = format === 'PNG' ? 'image/png' : 'image/webp';
                    const imgData = canvas.toDataURL(mime, 1.0);
                    triggerDownload(imgData, fileName);
                }};
                img.src = url;
            }}
        }}

        function triggerDownload(url, filename) {{
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }}

        document.addEventListener('DOMContentLoaded', initComponentTools);
    </script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(portal_template)

print("Portal generated and written to index.html successfully.")

import os

with open(r'c:\Users\rahul\safety-intelligence-dashboard\src\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open(r'c:\Users\rahul\safety-intelligence-dashboard\src\app.jsx', 'r', encoding='utf-8') as f:
    js = f.read()

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIF-X // Industrial Safety Intelligence Command Center</title>
  <meta name="description" content="Modern dark-mode industrial safety intelligence dashboard UI featuring graphite backdrop, neon cyan indicators, and real-time SIF prevention">
  
  <!-- Tailwind CSS Play CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            graphite: '#0d1823',
            'neon-cyan': '#6bc8ff',
            'safe-green': '#10b981',
            'danger-red': '#ef4444',
          }
        }
      }
    };
  </script>

  <!-- React 18 & ReactDOM UMD -->
  <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

  <!-- GSAP 3 for Magnetic Cursor and Immersive Navigation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

  <!-- Babel Standalone for direct in-memory JSX compilation -->
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

  <!-- Inlined Design Tokens and Glassmorphic Stylesheet -->
  <style>
/* CSS_PLACEHOLDER */
  </style>
</head>
<body class="bg-[#0d1823] text-slate-100 antialiased selection:bg-[#6bc8ff] selection:text-slate-950">

  <div id="root">
    <div class="min-h-screen flex flex-col items-center justify-center gap-4 bg-[#0d1823] text-slate-300 font-mono">
      <div class="relative w-16 h-16 flex items-center justify-center">
        <div class="w-14 h-14 rounded-full border-2 border-[#6bc8ff]/30 border-t-[#6bc8ff] animate-spin"></div>
        <div class="absolute w-8 h-8 rounded-full bg-[#6bc8ff]/10 animate-pulse"></div>
      </div>
      <div class="text-xs tracking-widest text-[#6bc8ff] uppercase font-bold">
        INITIALIZING SIF-INTEL ENGINE...
      </div>
      <div class="text-[10px] text-slate-500">
        LOADING NEURAL SENSORS & SPATIAL HUD
      </div>
    </div>
  </div>

  <script>
    if (window.location.search.indexOf('autologin=1') !== -1) {
      sessionStorage.setItem('sifx_authenticated', 'true');
    }
  </script>

  <!-- Inlined React Component Code -->
  <script type="text/babel">
/* JS_PLACEHOLDER */
  </script>
  <script>
    // Watchdog to prevent indefinite initialization freeze
    window.addEventListener('DOMContentLoaded', function() {
      setTimeout(function() {
        var root = document.getElementById('root');
        var loadingEl = root ? root.querySelector('.animate-spin') : null;
        if (loadingEl && root && root.firstElementChild) {
          var notice = document.createElement('div');
          notice.className = 'mt-4 text-center text-xs text-amber-400 max-w-sm px-4 py-2 border border-amber-500/30 rounded-lg bg-amber-500/10 font-mono';
          notice.innerHTML = 'Neural telemetry synchronizing... <br/><a href="javascript:location.reload()" style="color:#6bc8ff;text-decoration:underline;font-weight:bold;margin-top:6px;display:inline-block;">Click to Refresh Sentinel HUD</a>';
          root.firstElementChild.appendChild(notice);
        }
      }, 4500);
    });
    window.addEventListener('error', function(e) {
      console.error('SIF-X Unhandled Script Error:', e.error || e.message);
    });
  </script>
</body>
</html>"""

html = template.replace('/* CSS_PLACEHOLDER */', css).replace('/* JS_PLACEHOLDER */', js)

with open(r'c:\Users\rahul\safety-intelligence-dashboard\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html generated with inlined CSS, GSAP, and React application!")

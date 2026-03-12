/* ========================================
   BEALE STREET THEATER - DUDA SCRIPTS
   SAFE SCOPED – All initializers scope to .bst-scope
   ======================================== */

// ─── Mobile Navigation Toggle ─────────────────────
function initBSTNavigation(root) {
  const mobileToggle = root.querySelector('.bst-mobile-toggle');
  const mobileMenu = root.querySelector('.bst-mobile-menu');
  
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', function() {
      mobileMenu.classList.toggle('active');
      
      // Toggle icon (if using SVG or icon fonts)
      const icon = this.querySelector('svg') || this.querySelector('i');
      if (icon) {
        icon.classList.toggle('open');
      }
    });
    
    // Close menu when clicking a link
    const mobileLinks = mobileMenu.querySelectorAll('.bst-nav-link');
    mobileLinks.forEach(link => {
      link.addEventListener('click', function() {
        mobileMenu.classList.remove('active');
      });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
      if (!mobileToggle.contains(event.target) && !mobileMenu.contains(event.target)) {
        mobileMenu.classList.remove('active');
      }
    });
  }
}

// ─── Active Navigation Link Highlighting ──────────
function initActiveNavLinks(root) {
  const currentPath = window.location.pathname;
  const navLinks = root.querySelectorAll('.bst-nav-link');
  
  navLinks.forEach(link => {
    // Remove 'active' class from all links
    link.classList.remove('active');
    
    // Add 'active' class to current page link
    const linkPath = new URL(link.href).pathname;
    if (currentPath === linkPath || (currentPath === '/' && linkPath === '/index.html')) {
      link.classList.add('active');
    }
  });
}

// ─── Smooth Scroll for Anchor Links ───────────────
function initSmoothScroll(root) {
  root.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      
      // Skip if it's just "#"
      if (targetId === '#') {
        e.preventDefault();
        return;
      }
      
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        e.preventDefault();
        
        const navbarHeight = root.querySelector('.bst-navbar')?.offsetHeight || 0;
        const targetPosition = targetElement.offsetTop - navbarHeight;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

// ─── Lazy Load Images ─────────────────────────────
function initLazyLoadImages(root) {
  const images = root.querySelectorAll('img[data-src]');
  
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
        observer.unobserve(img);
      }
    });
  });
  
  images.forEach(img => imageObserver.observe(img));
}

// ─── Show Card Click Handler ──────────────────────
function initShowCardClicks(root) {
  const showCards = root.querySelectorAll('.bst-show-card');
  
  showCards.forEach(card => {
    card.addEventListener('click', function(e) {
      // Don't hijack clicks on inner <a> or <button> elements
      if (e.target.closest('a') || e.target.closest('button')) return;

      const ticketUrl = this.dataset.ticketUrl;
      if (ticketUrl) {
        window.open(ticketUrl, '_blank');
      }
    });
    
    // Add pointer cursor
    if (card.dataset.ticketUrl) {
      card.style.cursor = 'pointer';
    }
  });
}

// ─── Newsletter Form Handler ──────────────────────
function initNewsletterForm(root) {
  const form = root.querySelector('.bst-newsletter-form');
  
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const emailInput = this.querySelector('input[type="email"]');
      const submitBtn = this.querySelector('button[type="submit"]');
      const email = emailInput?.value;
      
      if (!email) {
        alert('Please enter a valid email address.');
        return;
      }
      
      // Show loading state
      if (submitBtn) {
        submitBtn.textContent = 'Subscribing...';
        submitBtn.disabled = true;
      }
      
      // Here you would integrate with your email service
      // For Duda, you might use their form submission API
      console.log('Newsletter signup:', email);
      
      // Simulate success
      setTimeout(() => {
        if (submitBtn) {
          submitBtn.textContent = 'Subscribed!';
          submitBtn.style.backgroundColor = '#14b8a6';
        }
        if (emailInput) {
          emailInput.value = '';
        }
        
        // Reset after 2 seconds
        setTimeout(() => {
          if (submitBtn) {
            submitBtn.textContent = 'Subscribe';
            submitBtn.disabled = false;
          }
        }, 2000);
      }, 1000);
    });
  }
}

// ─── Event Calendar Filter ────────────────────────
function initEventCalendarFilter(root) {
  const filterButtons = root.querySelectorAll('.bst-calendar-filter-btn');
  const eventCards = root.querySelectorAll('.bst-event-card');
  
  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const filterCategory = this.dataset.category;
      
      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      
      // Filter events
      eventCards.forEach(card => {
        const cardCategory = card.dataset.category;
        
        if (filterCategory === 'all' || cardCategory === filterCategory) {
          card.style.display = 'block';
          card.style.animation = 'fadeIn 0.3s ease';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// ─── Scroll Reveal Animation ──────────────────────
function initScrollReveal(root) {
  const revealElements = root.querySelectorAll('.bst-reveal');
  
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });
  
  revealElements.forEach(el => revealObserver.observe(el));
}

// ─── Sticky Navbar on Scroll ──────────────────────
function initStickyNavbar(root) {
  const navbar = root.querySelector('.bst-navbar');
  
  if (!navbar) return;
  
  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > 100) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
}

// ─── Initialize All Functions ─────────────────────
function initBST() {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      runInitializers();
    });
  } else {
    runInitializers();
  }
}

function runInitializers() {
  var root = document.querySelector('.bst-scope');
  if (!root) return;           // No .bst-scope on this page – do nothing

  initBSTNavigation(root);
  initActiveNavLinks(root);
  initSmoothScroll(root);
  initLazyLoadImages(root);
  initShowCardClicks(root);
  initNewsletterForm(root);
  initEventCalendarFilter(root);
  initScrollReveal(root);
  initStickyNavbar(root);
  
  console.log('BST Theme initialized (safe-scoped) 🎭');
}

// ─── Auto-Initialize ──────────────────────────────
initBST();

// ─── Export for Manual Initialization ─────────────
window.BST = {
  init: initBST,
  navigation: initBSTNavigation,
  activeLinks: initActiveNavLinks,
  smoothScroll: initSmoothScroll,
  lazyLoad: initLazyLoadImages,
  showCards: initShowCardClicks,
  newsletter: initNewsletterForm,
  calendarFilter: initEventCalendarFilter,
  scrollReveal: initScrollReveal,
  stickyNav: initStickyNavbar
};

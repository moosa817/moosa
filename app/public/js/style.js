// Whenever the user explicitly chooses light mode
// localStorage.theme = 'dark'


// dark theme
// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark')
} else {
  document.documentElement.classList.remove('dark')
}




const checkbox = document.getElementById('checkbox');



checkbox.addEventListener('change', () => {

  if (document.documentElement.classList.contains('dark')) {
    localStorage.theme = 'light'
    document.documentElement.classList.remove('dark')


  }
  else {
    localStorage.theme = 'dark'
    document.documentElement.classList.add('dark')


  }
})

if (localStorage.theme === 'dark') {
  $('#checkbox').attr("checked", true);
}

// side btn of sidebar





// animate on scroll
const animatedElements = document.querySelectorAll("[data-aos]");

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.intersectionRatio > 0) {
      entry.target.classList.add("aos-animate");
    } else {
      entry.target.classList.remove("aos-animate");
    }
  });
});

animatedElements.forEach(element => {
  observer.observe(element);
});


// typing animation
function typeWriterEffect(element, speed) {
  const text = element.textContent.trim();
  element.textContent = '';
  let i = 0;

  function type() {
    if (i < text.length) {
      element.textContent += text.charAt(i);
      i++;
      setTimeout(type, speed);
    } else {
      document.getElementById('cursor').style.display = 'none'
    }
  }

  setTimeout(type, speed);
}

const typingContainer = document.querySelector('#typing-container');
const paragraphs = typingContainer.querySelectorAll('p');

paragraphs.forEach(paragraph => {
  typeWriterEffect(paragraph, 29);
});





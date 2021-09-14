const toggleBtn = document.querySelector('.header__toggleBtn');
const menu = document.querySelector('.header__menu');
const accounts = document.querySelector('.header__account');

toggleBtn.addEventListener('click', () => {
  console.log('click');
  menu.classList.toggle('active');
  accounts.classList.toggle('active');
});
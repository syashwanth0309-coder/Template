const menu = document.querySelector('.menu');
const links = document.querySelector('.nav-links');
menu.addEventListener('click', () => { const open = menu.getAttribute('aria-expanded') !== 'true'; menu.setAttribute('aria-expanded', String(open)); links.classList.toggle('open', open); });
links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { links.classList.remove('open'); menu.setAttribute('aria-expanded','false'); }));
const skills = [...document.querySelectorAll('.skill')];
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
 const category = button.dataset.filter;
 document.querySelectorAll('.filter').forEach(tab => { tab.classList.toggle('active', tab === button); tab.setAttribute('aria-pressed', String(tab === button)); });
 let count = 0;
 skills.forEach(card => { const match = category === 'All' || card.dataset.groups.split('|').includes(category); if(match) count++; card.classList.toggle('dimmed', !match); card.classList.toggle('glowing', match && category !== 'All'); });
 document.getElementById('filter-status').textContent = category === 'All' ? 'Showing all skills.' : `${count} skills highlighted in ${category}.`;
}));
document.querySelectorAll('[data-track]').forEach(button => button.addEventListener('click', () => { const track = document.getElementById(button.dataset.track); track.scrollBy({ left:(track.querySelector('.work-card').getBoundingClientRect().width + 20) * Number(button.dataset.dir), behavior:matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' }); }));
const data = JSON.parse(document.getElementById('portfolio-data').textContent);
const dialog = document.getElementById('details');
let opener;
document.querySelectorAll('.work-card').forEach(card => card.addEventListener('click', () => {
 const item = data[card.dataset.kind][Number(card.dataset.index)];
 for (const key of ['title','category','date','description','tech']) document.getElementById(`dialog-${key}`).textContent = item[key];
 opener = card; dialog.showModal(); document.body.classList.add('modal-open');
}));
document.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { const r = dialog.getBoundingClientRect(); if(event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); });
dialog.addEventListener('close', () => { document.body.classList.remove('modal-open'); if(opener) opener.focus(); });

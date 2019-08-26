$(document).ready( () => {
  let frm = $('.form');
  frm.submit( e => {
    let target = e.target.classList[0];
    $(`.${target} .button`).text('Загрузка...');
    $(`.${target} .button`).attr('disabled', true);
    e.preventDefault(); // не обновляем страницу
    let data = {};
    data.name = $(`.${target} [name="name"]`).val(); // считываем значение id
    data.phone = $(`.${target} [name="phone"]`).val();
    let url = frm.attr('action');
    let csrf_token = $(`.${target} [name="csrfmiddlewaretoken"]`).val();
    data['csrfmiddlewaretoken'] = csrf_token;
    $.ajax({
      url: url,
      type: 'POST',
      data: data,
      cache: true,
      success: data => {
        console.log('ok');
        $(`.${target} [name="name"]`).val('');
        $(`.${target} [name="phone"]`).val('');
        if (data['result']=='ok'){
          $(`.${target} .button`).text('Отправить');
          $(`.${target} .button`).attr('disabled', false);
          alert('Заявка получена');
        }
        if (data['result']=='error'){
          $(`.${target} .button`).text('Отправить');
          $(`.${target} .button`).attr('disabled', false);
          $(`.${target} [name="phone"]`).addClass('error');
          console.log(data.response.phone); //сообщение об ошибке
        }
      },
      error: () => {
        $(`.${target} .button`).text('Отправить');
        $(`.${target} .button`).attr('disabled', false);
        console.log('error');
      }
    });
  });
});

$('[name="phone"]').click( () => {
  $('[name="phone"]').removeClass('error');
});

$('.slider').slick({
  infinite: true,
  speed: 500,
  autoplay: true,
  autoplaySpeed: 5000,
  prevArrow: '<button class="slider__slick-prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow: '<button class="slider__slick-next"><i class="fas fa-chevron-right"></i></button>',
});

$('.lic__slider').slick({
  infinite: true,
  speed: 500,
  autoplay: true,
  autoplaySpeed: 5000,
  dots: true,
  dotsClass: 'slick-dots lic__slick-dots',
  prevArrow: '<button class="lic__slick-prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow: '<button class="lic__slick-next"><i class="fas fa-chevron-right"></i></button>',
});

//about page
document.querySelectorAll('.about__button').forEach(button => {
  button.addEventListener('click', e => {
    e.preventDefault();
    const atr = button.getAttribute('data-content');
    document.querySelectorAll('.about__content').forEach(content =>{
      if (content.getAttribute('data-content') === atr) {
        content.classList.remove('hidden');
      } else {
        content.classList.add('hidden');
      }
    });
  });
});

//active menu item
document.querySelector('.nav__link[href="' + window.location.pathname + '"]').classList.add('nav__link--active');


document.querySelector('.header__nav-button').addEventListener('click', e => {
  e.preventDefault();
  document.querySelector('.main-nav').classList.toggle('main-nav--show');
});

document.querySelector('.header__button').addEventListener('click', e => {
  e.preventDefault();
  document.querySelector('.pop-up').classList.remove('hidden');
});

document.querySelector('.pop-up__close').addEventListener('click', e => {
  e.preventDefault();
  document.querySelector('.pop-up').classList.add('hidden');
});

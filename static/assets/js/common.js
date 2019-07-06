$(document).ready(function(){
  var frm = $('#form');
  frm.submit(function(e){
    e.preventDefault(); // не обновляем страницу
    var data = {};
    data.name = $('#name').val(); // считываем значение id
    data.phone = $('#phone').val();
    var url = frm.attr('action');
    var csrf_token = $('#form [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = csrf_token;
    $.ajax({
      url: url,
      type: 'POST',
      data: data,
      cache: true,
      success: function(data){
        console.log('ok');
        $('#name').val('');
        $('#phone').val('');
        if (data['result']=='ok'){
          alert('Заявка получена');
        }
        if (data['result']=='error'){
          $('#phone').addClass('app__input--error');
          console.log(data.response.phone); //сообщение об ошибке
        }
      },
      error: function(){
        console.log('error');
      }
    });
  });
});

$('#phone').click(function(){
  $('#phone').removeClass('app__input--error');
});

$('#name').click(function(){
  $('#name').removeClass('app__input--error');
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
    e.preventDefault;
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
$(document).ready(function(){
    var frm = $('#form');
    frm.submit(function(e){
        e.preventDefault(); // не обновляем страницу
        var data = {};
        data.name = $('#name').val(); // считываем значение id
        data.phone = $('#phone').val();
        var url = frm.attr("action");
        var csrf_token = $('#form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(){
                console.log('ok');
                $('#name').val('');
                $('#phone').val('');
            },
            error: function(){
                console.log("error");
            }
        })
    })
});

$('.slider').slick({
  infinite: true,
  speed: 500,
  autoplay: true,
  autoplaySpeed: 5000,
  //адаптивная высота
  prevArrow: '<button class="slick-arrow__slick-prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow: '<button class="slick-arrow__slick-next"><i class="fas fa-chevron-right"></i></button>',
});

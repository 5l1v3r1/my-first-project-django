$(document).ready(function(){
    $('.search_input').on('input',function(e){
        let action = $('#form-search-articles').attr('action');
        let input = $(this).val();
        if(input != '' || input != undefined){
            $.ajax({
                type:'get',
                url:action,
                data: {search:input},
                success:function(res){
                    $('.dropdown-list').html('');
                    $('.dropdown').addClass('open');
                    for(let i in res){
                        $('.dropdown-list').append('<li><a href="/'+res[i].fields.category+'/'+res[i].fields.slug+'/">'+ res[i].fields.name +'</a></li>');
                    }
                }
            });
        }
    });
    $(document).on('click','.open-search-form',function(e){
        $('#form-search-articles').removeClass('d-none');
        $(this).addClass('d-none');
    });

      $('.main_slider').slick({
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          fade: true,
          autoplay:true,
          autoplaySpeed:3000,
      });
      $('#review_form').submit(function(e){
          e.preventDefault();
          let email = $('.email-review').val();

          if(email != '' || email != undefined){
            $.ajax({
                url:$(this).attr('action'),
                type:'post',
                data:$(this).serialize(),
                success:function(res){
                    alert('Успешно сохранено');
                    $('#review_block').html('');
                    for(let i in res){
                        $('#review_block').append(
                            '<div class="col-xl-12 mt-2">   <div class="card">   <div class="card-header d-flex justify-content-between">    <span>'+res[i].fields.name+'</span>  <small>'+res[i].fields.email+'</small> </div> <div class="card-body"> <p class="card-text">'+res[i].fields.text+'</p></div> </div> </div>'
                        );
                    }
                }
            });
          }

      });
    if(window.location.pathname == '/contacts/'){
        let coordin = $('.coordin_map').val();
        coordin = coordin.split(',');
        ymaps.ready(function () {
            var myMap = new ymaps.Map('map', {
                    center: [coordin[0], coordin[1].replace(/\s/g, '')],
                    zoom: 13
                });
                myMap.geoObjects.add(new ymaps.Placemark([coordin[0], coordin[1].replace(/\s/g, '')], {
                    balloonContent: 'цвет <strong>носика Гены</strong>',
                    iconCaption: 'Очень длиннный, но невероятно интересный текст'
                }, {
                    preset: 'islands#greenDotIconWithCaption'
                }))
        });
    }
});
$(document).ready(function(){
        $('.summernote').summernote({
            tabsize: 2,
            height: 350
        });

      $('.summernote-mainpage').summernote({
            tabsize: 2,
            height: 550
      });
      $('#create_review_form').submit(function(e){
        e.preventDefault();
        let name_review = $('.name-review').val();
        let email_review = $('.email-review').val();
        let text_review = $('.text-review').val();
        let anonym = $(".anonym-review").prop("checked");
        let action = $(this).attr('action');
        let token = $('[name = "csrfmiddlewaretoken"]').val();
        if(anonym){
            name_review = 'Анонимно';
        }
        if(email_review != '' || email_review != undefined && text_review != '' || text_review != undefined){
            $.ajax({
                type:'post',
                url:action,
                data:{name:name_review, anonym:anonym, email:email_review, text:text_review, csrfmiddlewaretoken:token},
                success:function(res){
                    location.replace('/account/reviews/');
                }
            });
        }
      });

      $('#update_review_form').submit(function(e){
        e.preventDefault();
        let name_review = $('.name-review').val();
        let email_review = $('.email-review').val();
        let text_review = $('.text-review').val();
        let anonym = $(".anonym-review").prop("checked");
        let action = $(this).attr('action');
        let token = $('[name = "csrfmiddlewaretoken"]').val();
        if(anonym){
            name_review = 'Анонимно';
        }
        if(email_review != '' || email_review != undefined && text_review != '' || text_review != undefined){
            $.ajax({
                type:'post',
                url:action,
                data:{name:name_review, anonym:anonym, email:email_review, text:text_review, csrfmiddlewaretoken:token},
                success:function(res){
                    location.replace('/account/reviews/');
                }
            });
        }
      });

})
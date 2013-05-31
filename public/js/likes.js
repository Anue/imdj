;(function($){

    function add_text($el) {
        var pk = $el.data('pk');
        var count = $el.data('count');
        var txt = count == 0 || count > 1 ? " Likes " : " Like ";
        var $span = $("<span class='like-wrapper'/>");
        $span.text(count + txt);
        $el.wrap($span);
    };

    function make_liked($el) {
        var pk = $el.data('pk');
        var count = parseInt($el.data('count')) - 1;
        var txt;
        switch(count){
            case 0: txt = ""; break;
            case 1: txt = " (and 1 other)"; break;
            default: txt = " (plus " + count  + " others)";
        };
        var $new = "<span class='like-wrapper'>You Like this" + txt + "</span>";
        var $wrapper = $el.parent();
        if ($wrapper.hasClass('like-wrapper')) {
            $wrapper.after($new);
            $wrapper.remove();
        } else {
            $el.after($new);
            $el.remove();
        }
    };

    $.fn.likeBtn = function() {
        var $el = $(this);
        var pk = $el.data('pk');
        var count = $el.data('count');
        if (!$.cookie("liked_movie_" + pk)) {
            add_text($el);
            $el.click(function() {
                $.post($el.attr('href'), {pk: pk}, function(data) {
                    if (data.success) {
                        $el.data('count', data.count);
                        make_liked($el);
                    }
                });
                return false;
            });
        } else {
            make_liked($el);
        }
        $el.show('fast');
    };

})(jQuery);
